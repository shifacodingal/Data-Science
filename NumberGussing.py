import random

# Game information stored in dictionary
game = {
    "player": "",
    "secret_number": 0,
    "attempts": 0
}

# Get player name
game["player"] = input("Enter your name: ")

# Generate random number between 1 and 10
game["secret_number"] = random.randint(1, 10)

print("\nWelcome", game["player"], "!")
print("I have selected a number between 1 and 10.")
print("Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    game["attempts"] += 1

    if guess == game["secret_number"]:
        print("\n🎉 Congratulations!")
        print("You guessed the correct number.")
        print("Number of attempts:", game["attempts"])
        break

    elif guess < game["secret_number"]:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")