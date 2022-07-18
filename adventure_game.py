import time
import random

# Assign a random enemy
enemy_list = ['gorgon', 'troll', 'pirate', 'dragon']
enemy = ''

# Set initial weapon of the user to be a dagger
weapon = 'dagger'


# Print Statements
# Statements that appear first whenever the game starts
def opening_statements(enemy, weapon):
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + enemy + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) " + weapon + ".")


# Statements that prompt user input
def input_statements():
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")


# Statements that show after a user chooses to advance to house
def house_statements(enemy):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a " +
                enemy + ".")
    print_pause("Eep! This is the " + enemy + "'s house!")
    print_pause("The " + enemy + " attacks you!")


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


# Statements when user already has sword
def have_sword():
    print_pause("You've been here before, and gotten all the" +
                " good stuff. It's just an empty cave now.")


# Statements when user finds a sword
def finds_sword(weapon):
    print_pause("It turns out to be only a small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You discard your silly old " + weapon +
                " and take the sword with you.")


# Statements when user is about to be defeated
def defeat_statements(enemy, weapon):
    print_pause("You do your best...")
    print_pause("But your " + weapon + " is no match for the " +
                enemy + ".")
    print_pause("You have been defeated!")


# Print a message then pause for a while
def print_pause(msg):
    print(msg)
    time.sleep(1.5)


# Taking user's input and validating it
def user_input(prompt, values):
    while True:
        choice = input(prompt).lower()
        if choice in values:
            return choice


# Decide function definition
def decide():
    input_statements()
    choose_house_or_weapon()


# User either advances to the house or chooses a weapon
def choose_house_or_weapon():
    choice = user_input("Please enter 1 or 2.\n", ['1', '2'])
    if choice == '1':
        advance_to_house()
    else:
        change_weapon()


# When the user choose 1: advance to house
def advance_to_house():
    house_statements(enemy)
    fight_or_run_away()


# When the user choose 2: change the weapon
def change_weapon():
    global weapon
    print_pause("You peer cautiously into the cave.")
    have_sword() if weapon == 'sword' else finds_sword(weapon)
    weapon = 'sword'
    print_pause("You walk back out to the field.")
    decide()


# When the User Chooses 1: Fight the enemy
def fight():
    if weapon == 'sword':
        success_statements(enemy, weapon)
    else:
        defeat_statements(enemy, weapon)
    play_again()


# When the user choose 2: Run away from the enemy
def run_away():
    print_pause("You run back into the field. Luckily, you don't seem to" +
                " have been followed.")
    decide()


# Function to fight or run away
def fight_or_run_away():
    choice = user_input("Would you like to (1) fight or (2) run away?\n",
                        ['1', '2'])
    fight() if choice == '1' else run_away()


# Play again prompt
def play_again():
    choice = user_input("Would you like to play again? (y/n)\n",
                        ['y', 'n'])
    if choice == 'y':
        global weapon
        print_pause("Excellent! Restarting the game...")
        weapon = 'dagger'
        start_game()
    else:
        end_game()


# Print information about the adventure
def start_game():
    global enemy
    enemy = random.choice(enemy_list)
    opening_statements(enemy, weapon)
    decide()


# End the game
def end_game():
    print("Thanks for playing! See you next time.")


# Start the adventure game
start_game()
