import random
import time

enemy_list = ['gorgon', 'troll', 'pirate', 'dragon']
enemy = ""

weapon = "dagger"


# function for print pause
def print_pause(message):
    print(message)
    time.sleep(1.5)


# function for the introductory statements
def intro(enemy, weapon):
    enemy = random.choice(enemy_list)
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + enemy + " is somewhere"
                " around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) " + weapon)


# input funtion and validate
def valid_input(prompt, values):
    result = input(prompt)
    if result.lower() in values:
        return result.lower()
    valid_input(prompt, values)


# statements to choose an input of house or cave
def house_cave():
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    choice = valid_input("\nPlease enter 1 or 2.\n", ['1', '2'])
    if choice == '1':
        house(enemy)
    else:
        cave()


# function when player goes into the house
def house(enemy):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a " +
                enemy + ".")
    print_pause("Eep! This is the " + enemy + "'s house!")
    print_pause("The " + enemy + " attacks you!")
    fight_or_field()


# function when player decides to enter cave
def cave():
    global weapon
    print_pause("You peer cautiously into the cave.")
    if weapon == 'sword':
        print_pause("You've been here before, and gotten all the" +
                    " good stuff. It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You discard your silly old " + weapon +
                    " and take the sword with you.")
        weapon = 'sword'

    print_pause("You walk back out to the field.")
    house_cave()


# function when player runs back to the field
def field():
    print_pause("You run back into the field. Luckily, you don't seem to" +
                " have been followed.")
    house_cave()


# function when player decides to fight
def fight():
    if weapon == 'sword':
        success_statements(enemy, weapon)
    else:
        defeat_statements(enemy, weapon)
    play_again()


# Function to fight or run away to the field
def fight_or_field():
    choice = valid_input("Would you like to (1) fight or (2) run away?\n",
                        ['1', '2'])
    fight() if choice == '1' else field()


# Statement when user is about to defeat opponent with sword
def success_statements(enemy, weapon):
    print_pause("As the " + enemy + " moves to attack, you unsheath" +
                " your new " + weapon + ".")
    print_pause("The " + weapon + " of Ogoroth shines brightly in your" +
                " hand as you brace yourself for the attack.")
    print_pause("But the " + enemy + " takes one look at your shiny" +
                " new toy and runs away!")
    print_pause("You have rid the town of the " + enemy +
                ". You are victorious!")


# Statements when user is about to be defeated
def defeat_statements(enemy, weapon):
    print_pause("You do your best...")
    print_pause("But your " + weapon + " is no match for the " +
                enemy + ".")
    print_pause("You have been defeated!")


# Print information about the adventure
def start_game():
    global enemy
    enemy = random.choice(enemy_list)
    intro(enemy, weapon)
    house_cave()


# Play again prompt
def play_again():
    choice = valid_input("Would you like to play again? (y/n)\n",
                         ['y', 'n'])
    if choice == 'y':
        global weapon
        print_pause("Excellent! Restarting the game...")
        weapon = 'dagger'
        start_game()
    else:
        print("Thanks for playing! See you next time.")


start_game()
