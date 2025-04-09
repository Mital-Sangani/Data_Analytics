import random

def shuffle_word(word):
    return "".join(random.sample(word, len(word)))

def word_scramble_game():
    words = ["python", "computer", "keyboard", "developer", "programming", "language", "internet"]
    
    while True:
        secret_word = random.choice(words)
        scrambled_word = shuffle_word(secret_word)
        
        print("\n🔠 Welcome to Word Scramble! 🔠\n")
        print(f"Unscramble this word: {scrambled_word}")
        
        attempts = 3
        while attempts > 0:
            user_guess = input("Your guess: ").strip().lower()
            if user_guess == secret_word:
                print("🎉 Correct! You unscrambled it! 🎉\n")
                break
            else:
                attempts -= 1
                print(f"❌ Wrong! {attempts} attempts left.")
        
        if user_guess != secret_word:
            print(f"😢 Out of attempts! The correct word was: {secret_word}\n")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing! 👋\n")
            break

# Start the game
word_scramble_game()
