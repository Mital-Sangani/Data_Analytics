import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    scores = {"Player 1": 0, "Player 2": 0}
    players = ["Player 1", "Player 2"]
    turn = 0
    
    while True:
        current_player = players[turn]
        input(f"\n{current_player}, press Enter to roll the dice... ")
        
        dice = roll_dice()
        print(f"{current_player} rolled: {dice}\n")
        
        if dice == 6:
            if scores[current_player] == 0:
                scores[current_player] = 6  
            else:
                scores[current_player] += 6

            print(f"🎉 {current_player} got 6! Rolling again... Score: {scores[current_player]} 🎉\n")
            
            if scores[current_player] >= 100:
                print(f"🏆 Congratulations {current_player}! You reached 100 points. Game Over! 🏆\n")
                break
        else:
            scores[current_player] += dice  
            print(f"✅ {current_player}'s new score: {scores[current_player]}\n")
            print(f"❌ {current_player} didn't roll a 6. Turn over! ❌\n")
            turn = 1 - turn  # Switch turn between 0 and 1

play_game()
