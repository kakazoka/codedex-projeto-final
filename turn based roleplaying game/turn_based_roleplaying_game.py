import random
import time

class Player:
    def __init__(self, name, class_choice):
        self.name = name
        if class_choice == 1:
            self.class_choice = 'Archer'
            self.speed = 8
            self.attack = 6
            self.attack_power = 7
            self.defense = 5
        elif class_choice == 2:
            self.class_choice = 'Mage'
            self.speed = 6
            self.attack = 5
            self.attack_power = 9
            self.defense = 6
        elif class_choice == 3:
            self.class_choice = 'Warrior'
            self.speed = 5
            self.attack = 7
            self.attack_power = 8
            self.defense = 9
        self.health = 100

    def attack_enemy(self, enemy):
        total_damage = random.randint(self.attack - 2, self.attack + 2) + random.randint(self.attack_power - 2, self.attack_power + 2)
        enemy.take_damage(total_damage)
        return total_damage

    def heal(self):
        heal_amount = random.randint(30, 50)
        self.health += heal_amount
        if self.health > 100:
            self.health = 100
        return heal_amount

    def is_alive(self):
        return self.health > 0

class Enemy:
    def __init__(self, enemy_type):
        self.enemy_type = enemy_type
        if enemy_type == 'Goblin':
            self.speed = 7
            self.attack = 5
            self.attack_power = 6
            self.defense = 4
        elif enemy_type == 'Orc':
            self.speed = 4
            self.attack = 8
            self.attack_power = 7
            self.defense = 6
        elif enemy_type == 'Skeleton':
            self.speed = 5
            self.attack = 6
            self.attack_power = 5
            self.defense = 5
        self.health = 50

    def attack_player(self, player):
        total_damage = random.randint(self.attack - 2, self.attack + 2) + random.randint(self.attack_power - 2, self.attack_power + 2)
        player.health -= total_damage
        return total_damage

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

def choose_class():
    print('\nChoose your class:')
    print('1. Archer')
    print('2. Mage')
    print('3. Warrior')
    while True:
        choice = input('Enter the number corresponding to your choice: ')
        if choice.isdigit() and int(choice) in [1, 2, 3]:
            return int(choice)
        else:
            print('Invalid input. Please enter a number between 1 and 3.')

def choose_enemy():
    enemy_types = ['Orc', 'Goblin', 'Skeleton']
    enemy_type = random.choice(enemy_types)
    return Enemy(enemy_type)

def choose_action():
    print('Choose your action:')
    print('1. Attack')
    print('2. Heal')
    while True:
        choice = input('Enter the number corresponding to your choice: ')
        if choice.isdigit() and int(choice) in [1, 2]:
            return int(choice)
        else:
            print('Invalid input. Please enter 1 or 2.')

def player_turn(player, enemy):
    action = choose_action()
    if action == 1:
        damage_dealt = player.attack_enemy(enemy)
        print(f'{player.name} attacked the {enemy.enemy_type} and dealt {damage_dealt} damage!')
    elif action == 2:
        heal_amount = player.heal()
        print(f'{player.name} healed for {heal_amount} health points.')
    else:
        print('Invalid action. Try again.')

def enemy_turn(enemy, player):
    damage_dealt = enemy.attack_player(player)
    print(f'The {enemy.enemy_type} attacked {player.name} and dealt {damage_dealt} damage!')

def main():
    player_name = input('Enter your name: ')
    print(f'\nYou\'re {player_name}, tasked with saving the kingdom of Astoria from relentless monster attacks.')
    print('Choose your path as a skilled archer, masterful mage or formidable warrior and venture into perilous realms filled with menacing foes with your unique abilities and talents.')
    print('Whether striking with deadly precision, unleashing devastating spells or  wielding a mighty blade, prove your bravery, and loyalty in a quest to restore peace.')
    class_choice = choose_class()
    player = Player(player_name, class_choice)

    print(f'\n=== {player.class_choice} Stats ===')
    print(f'Health: {player.health}')
    print(f'Speed: {player.speed}')
    print(f'Attack: {player.attack}')
    print(f'Attack Power: {player.attack_power}')
    print(f'Defense: {player.defense}')

    battles_won = 0
    while battles_won < 5:
        enemy = choose_enemy()
        print(f'\nA wild {enemy.enemy_type.capitalize()} appears!')
        print(f'\n=== {enemy.enemy_type.capitalize()} Stats ===')
        print(f'Health: {enemy.health}')

        while player.is_alive() and enemy.is_alive():
            print(f'\n=== {player.name}\'s Turn ===')
            player_turn(player, enemy)

            if enemy.is_alive():
                print('\n=== Enemy\'s Turn ===')
                enemy_turn(enemy, player)

            print(f'\n{player.name}\'s health left: {player.health}')
            print(f'{enemy.enemy_type}\'s health left: {enemy.health}')

        if player.is_alive():
            battles_won += 1
            print(f'{player.name} defeated {enemy.enemy_type}!')
        else:
            print('\nDefeat befalls the valiant. {player.name}\'s quest ended by the merciless grip of darkness.')
            break

        time.sleep(2)

    if battles_won == 5:
        print('\n{player.name} restored peace to Astoria.}')

if __name__ == '__main__':
    main()
