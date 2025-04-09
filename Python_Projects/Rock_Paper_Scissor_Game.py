import random

def game(user, computer):
    print(f"USER CHOICE : {user}")
    print(f"COMPUTER CHOICE : {computer}")

    if (user == "SCISSOR" and computer == "PAPER") or (user == "ROCK" and computer == "SCISSOR") or (user == "PAPER" and computer == "ROCK"):
        return "**** USER WON THE GAME ****"
    elif user == computer:
        return "**** TIE ****"
    else:
        return "**** COMPUTER WON THE GAME ****"


game_list = ["ROCK", "PAPER", "SCISSOR"]

menu = """
                    MENU
                    
                ROCK
                PAPER
                SCISSOR

       """
status = True
while status :

    print(menu)

    user_choice = input("Enter your choise : ").upper()
    computer_choice = random.choice(game_list)
    result = game(user_choice,computer_choice)
    print(f"Result : {result} \n")

    game_choice = input("Do you want to play again press 'y' for yes and press 'n' for no : ").lower()

    if game_choice == 'y' or game_choice == 'yes':
        status = True
    else:
        status = False
        print()
        print("🙏😊 THANK YOU !!! FOR PLAYING THIS GAME 😊🙏")
        print()