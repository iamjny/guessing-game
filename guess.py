import os

from game import Game


class Guess:
    def __init__(self, string_database):
        self.string_database = string_database
        self.random_word = None
        self.current_guess = ['-'] * 4
        self.correct_guesses = set()
        self.guessed_letters = []

        self.bad_guess_count = 0
        self.missed_letter_count = 0
        self.game_instance = Game()

    # Generate new word for when the game is completed and moves on to the next
    def generate_word(self):
        self.random_word = self.string_database.random_word()
        self.current_guess = ['-'] * len(self.random_word)
        self.correct_guesses.clear()
        self.guessed_letters.clear()

        # To make sure the next word doesn't contain the same bad_guess_count and missed_letter_count
        self.bad_guess_count = 0
        self.missed_letter_count = 0

    # Displays the correct play/test mode menu
    def menu(self, mode):
        print("++")
        print("++ The great guessing game")
        print("++\n")

        if mode == "play":
            print("Current Guess: " + ''.join(self.current_guess))
        elif mode == "test":
            print("Current word: " + self.random_word)
            print("Current Guess: " + ''.join(self.current_guess))

    # Menu options
    def play(self, mode):
        self.generate_word()

        while True:
            self.menu(mode)
            print("Letters guessed: " + ' '.join(self.guessed_letters))
            print("g = guess, t = tell me, l for a letter, and q to quit")
            user_input = input("\nEnter Option: ").lower()

            if user_input == 'g':
                guess = input("\nEnter your guess: ").lower()
                self.input_guess(guess)
            elif user_input == 't':
                self.tell_word()
                input("Press Enter to continue...")

                self.game_instance.add_game(
                    self.random_word,
                    "Gave up",
                    self.bad_guess_count,
                    self.missed_letter_count,
                    self.game_instance.calculate_score(self.current_guess, self.random_word, self.missed_letter_count,
                                                       self.bad_guess_count, True)
                )

                self.generate_word()
                os.system('clear')
            elif user_input == 'l':
                letter = input("\nEnter a letter: ")
                self.input_letter(letter)
            elif user_input == 'q':
                os.system('clear')
                self.game_instance.print_scores()
                break
            else:
                print("\nInvalid option. Please choose again.\n\n")
                input("Press Enter to continue...")
                os.system('clear')

    # When user chooses option 'g', user will be able to guess the word
    def input_guess(self, guess):
        if guess == self.random_word:
            print("\n@@")
            print("@@ FEEDBACK: You're right Einstein!")
            print("@@\n\n")

            self.game_instance.add_game(
                self.random_word,
                "Success",
                self.bad_guess_count,
                self.missed_letter_count,
                self.game_instance.calculate_score(self.current_guess, self.random_word, self.missed_letter_count,
                                                   self.bad_guess_count, False)
            )

            self.generate_word()
            input("Press Enter to continue...")
            os.system('clear')
        else:
            print("\n@@")
            print("@@ FEEDBACK: Try again, loser!")
            print("@@\n\n")

            self.bad_guess_count += 1

            input("Press Enter to continue...")
            os.system('clear')

    # When user chooses option 't', the game will print the correct word
    def tell_word(self):
        print("\n@@")
        print(f"@@ FEEDBACK: You really should have guessed this... '" + self.random_word + "'")
        print("@@\n\n")

    # When user chooses option 'l', user will be able to guess a letter that might be in the word
    def input_letter(self, letter):
        # If letter input has already been inputted, then the game will
        # ask user to keep trying to guess
        if letter in self.guessed_letters:
            print("\n@@")
            print("@@ FEEDBACK: You've already used this letter, silly! Try again!")
            print("@@\n\n")
            input("Press Enter to continue...")
            os.system('clear')
            return

        self.guessed_letters.append(letter)

        # If user inputs a correct letter, game will congratulate user and
        # add said letter to correct guesses
        if letter in self.random_word and letter not in self.correct_guesses:
            print("\n@@")
            print("@@ FEEDBACK: Woo hoo, you found 1 letter!")

            self.correct_guesses.add(letter)

            for i in range(len(self.random_word)):
                if self.random_word[i] == letter:
                    self.current_guess = list(self.current_guess)
                    self.current_guess[i] = letter
                    self.current_guess = ''.join(self.current_guess)

            # If user has guessed all correct letters, game will congratulate user
            # and change word (to start new game)
            if all(letter in self.correct_guesses for letter in self.random_word):
                print("@@ FEEDBACK: You also guessed all letters in '" + self.random_word + "'!")
                print("@@\n\n")

                self.game_instance.add_game(
                    self.random_word,
                    "Success",
                    self.bad_guess_count,
                    self.missed_letter_count,
                    self.game_instance.calculate_score(self.current_guess, self.random_word, self.missed_letter_count,
                                                       self.bad_guess_count, False)
                )

                self.generate_word()
            else:
                print("@@\n\n")

            input("Press Enter to continue...")
            os.system('clear')
        else:
            print("\n@@")
            print("@@ FEEDBACK: Not a single match, loser!")
            print("@@\n\n")

            self.missed_letter_count += 1

            input("Press Enter to continue...")
            os.system('clear')
