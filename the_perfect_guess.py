from random import randint, choice

def play_game(high_score = None):
    # Difficulty levels

    level = input("Choose difficulty (easy/medium/hard): ").lower()

    if level == "easy":
        n = randint(0, 30)
        max_attempts = 6
    elif level == "medium":
        n = randint(0,50)
        max_attempts = 8
    elif level == "hard":
        n = randint(0,100)
        max_attempts = 10
    else:
        print("❌ Invalid input! Please type (easy/medium/hard).")

    a = -1
    guesses = 1
    
    print(f"\n🎮 Guess the number! You have {max_attempts} attempts.")
    
    while(a != n and guesses < max_attempts):
        try:
            a = int(input("👉 Enter your guess: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        if (a>n):
            print("📉 Lower number please..")
            guesses += 1

        elif(a<n):
            print("📈 Higher number please..")
            guesses += 1
        
        else:
            print(f"🎉 You guessed it! The number {n} in {guesses} attempts.")
            if (high_score is None or guesses < high_score):
                high_score = guesses
                print("🏆 New High Score!")
                break
        
        # Give hints (hot/cold)
        diff = abs(a - n)
        if diff <= 5:
            print("🔥 Very close!")
        elif diff <= 10:
            print("🙂 Close!")
        else:
            print("❄️ Far away...")
        
        fun_msgs = ["Keep going!", "You’ll get it!", "Almost there!", "Not this time!"]
        print(choice(fun_msgs))

high_score = None
while True:
    high_score = play_game(high_score)

    while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again in ["y" ,"n" ,"no" ,"yes"]:
            break
        else:
            print("❌ Invalid input! Please type 'y' or 'n'.")

        if (play_again == "n" or play_game == "no"):
            print(f"\n👋 Thanks for playing! Your best score was {high_score} attempts.")
            break





