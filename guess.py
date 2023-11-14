import StringDatabase


class Guess:
    pass


def play_mode():
    print("Play mode...\n")
    print("++")
    print("++ The great guessing game")
    print("++\n")

    random_word = StringDatabase.random_word(StringDatabase.words)

    print("Current guess: ----")
    print("Letters guessed: ")
    while True:
        print("g = guess, t = tell me, l for a letter, and q to quit")
        user_input = input("Enter Option: ").lower()

        if user_input == 'g':
            guess = input("Enter your guess: ")
            # Process the guess
            print(f"You guessed: " + guess)
        elif user_input == 't':
            print(f"The word is: " + random_word)
        elif user_input == 'l':
            letter = input("Enter a letter: ")
            # Process the letter input
            print("You entered the letter: " + letter)
        elif user_input == 'q':
            print("Quitting game...")
            break
        else:
            print("Invalid option. Please choose again.")


def test_mode():
    print("Test mode...\n")
    print("++")
    print("++ The great guessing game")
    print("++\n")

    random_word = StringDatabase.random_word(StringDatabase.words)
    print("Current Word: " + random_word)
    print("Current Guess: ----")
    print("Letters guessed: ")
    while True:
        print("g = guess, t = tell me, l for a letter, and q to quit")
        user_input = input("Enter Option: ").lower()

        if user_input == 'g':
            guess = input("Enter your guess: ")
            # Process the guess
            print(f"You guessed: " + guess)
        elif user_input == 't':
            print(f"The word is: " + random_word)
        elif user_input == 'l':
            letter = input("Enter a letter: ")
            # Process the letter input
            print("You entered the letter: " + letter)
        elif user_input == 'q':
            print("Quitting game...")
            break
        else:
            print("Invalid option. Please choose again.")
