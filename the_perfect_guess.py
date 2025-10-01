from random import randint, choice

def play_game(high_score=None):
    # Difficulty levels
    level = input("Choose difficulty (easy/medium/hard): ").lower()

    if level == "easy":
        n = randint(0, 30)
        max_attempts = 6
    elif level == "medium":
        n = randint(0, 50)
        max_attempts = 8
    elif level == "hard":
        n = randint(0, 100)
        max_attempts = 10
    else:
        print("❌ Invalid input! Please type (easy/medium/hard).")
        return high_score   # don’t lose the old score

    a = -1
    guesses = 1
    
    print(f"\n🎮 Guess the number! You have {max_attempts} attempts.")
    
    while a != n and guesses <= max_attempts:
        try:
            a = int(input("👉 Enter your guess: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        if a > n:
            print("📉 Lower number please..")
        elif a < n:
            print("📈 Higher number please..")
        else:
            print(f"🎉 You guessed it! The number {n} in {guesses} attempts.")
            if high_score is None or guesses < high_score:
                high_score = guesses
                print("🏆 New High Score!")
            return high_score  # ✅ return updated best score

        # Give hints (hot/cold)
        # diff = abs(a - n)
        # if diff <= 5:
        #     print("🔥 Very close!")
        # elif diff <= 10:
        #     print("🙂 Close!")
        # else:
        #     print("❄️ Far away...")

        # # Fun messages
        # fun_msgs = ["Keep going!", "You’ll get it!", "Almost there!", "Not this time!"]
        # print(choice(fun_msgs))

        guesses += 1

    # ❌ If game ends without guessing, just keep the old high_score
    print(f"❌ Out of attempts! The number was {n}.")
    return high_score


# Game Loop
high_score = None
while True:
    high_score = play_game(high_score)

    while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again in ["y", "yes", "n", "no"]:
            break
        else:
            print("❌ Invalid input! Please type 'y' or 'n'.")

    if play_again in ["n", "no"]:
        if high_score is None:
            print("\n👋 Thanks for playing! You didn't set a high score yet.")
        else:
            print(f"\n👋 Thanks for playing! Your best score was {high_score} attempts.")
        break
