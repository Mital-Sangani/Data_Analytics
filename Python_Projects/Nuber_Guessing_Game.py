import random  # 🎲 Importing random module

computer = random.randint(1, 100)  # 🔢 Generating a random number between 1 to 100
status = True  # ✅ While loop initialization

for i in range(1, 10):  # 🔁 Loop will run until status is True
    while status:
        if i <= 8:
            user = int(input("🎯 Enter Your Guess (1 to 100): "))  # Accepting user input
            if user < computer:  # Condition to check if user's guess is lower than computer's number
                print("📢 HINT: Guess a Higher Number ⬆️")
            elif user > computer:  # Condition to check if user's guess is higher than computer's number
                print("📢 HINT: Guess a Lower Number ⬇️")
            else:  # Condition when user guesses correctly
                print("🎉 ************** CONGRATULATIONS, YOU WON THE GAME! ************** 🎉")
                print("🏆 ******************** You Finished LEVEL-1 ********************* 🏆")
                print("")
                choice = input("👉 Do You Want To Play Level-2? (yes or no): ")
                
                if choice.lower() == "yes":  # If user chooses to continue to Level-2
                    print("\n📜 ********** RULES FOR LEVEL-2 ********** 📜")
                    print("1️⃣ You will now guess a number between 100 and 200.")
                    print("2️⃣ You have only 7 attempts.")
                    print("3️⃣ If you guess wrong, hints will be provided.\n")
                    
                    computer = random.randint(100, 200)  # Generating new random number for Level-2
                    for n in range(1, 8):  # Loop for Level-2 attempts
                        if n <= 6:
                            user = int(input("🎯 Enter Your Guess (100 to 200): "))
                            if user < computer:
                                print("📢 HINT: Guess a Higher Number ⬆️")
                            elif user > computer:
                                print("📢 HINT: Guess a Lower Number ⬇️")
                            else:
                                print("🎉 ************** CONGRATULATIONS, YOU WON THE GAME! ************** 🎉")
                                print("🏆 ******************** You Finished LEVEL-2 ********************* 🏆")
                                print("")
                                choice = input("👉 Do You Want To Play Level-3? (yes or no): ")
                                
                                if choice.lower() == "yes":  # If user chooses to continue to Level-3
                                    print("\n📜 ********** RULES FOR LEVEL-3 ********** 📜")
                                    print("1️⃣ You will now guess a number between 100 and 300.")
                                    print("2️⃣ You have only 5 attempts.")
                                    print("3️⃣ If you guess wrong, hints will be provided.\n")
                                    
                                    computer = random.randint(100, 300)  # Generating new random number for Level-3
                                    for r in range(1, 6):  # Loop for Level-3 attempts
                                        if r <= 4:
                                            user = int(input("🎯 Enter Your Guess (100 to 300): "))
                                            if user < computer:
                                                print("📢 HINT: Guess a Higher Number ⬆️")
                                            elif user > computer:
                                                print("📢 HINT: Guess a Lower Number ⬇️")
                                            else:
                                                print("🎉 ************** CONGRATULATIONS, YOU WON THE GAME! ************** 🎉")
                                                print("🏆 ******************** You Finished LEVEL-3 ********************* 🏆")
                                                status = False  # Ending the game after Level-3 win
                                                break
                                        else:  # When user exhausts attempts in Level-3
                                            print(f"❌ Game Over! The Correct Number was {computer} ❌")
                                            status = False
                                            break
                                else:  # If user does not want to play Level-3
                                    status = False
                                    print("👋 ******************** Bye Bye... ********************* 👋")
                                    break
                        else:  # When user exhausts attempts in Level-2
                            print(f"❌ Game Over! The Correct Number was {computer} ❌")
                            status = False
                            break
                else:  # If user does not want to play Level-2
                    status = False
                    print("👋 ******************** Bye Bye... ********************* 👋")
                    break
            i += 1  # Incrementing attempt counter
        else:  # When user exhausts attempts in Level-1
            print(f"❌ Game Over! The Correct Number was {computer} ❌")
            status = False
            break
