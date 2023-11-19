class Game:
    letter_frequencies = {
        'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25,
        'e': 12.70, 'f': 2.23, 'g': 2.02, 'h': 6.09,
        'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03,
        'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93,
        'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06,
        'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15,
        'y': 1.97, 'z': 0.07
    }

    def __init__(self):
        self.games = []

    def add_game(self, word, status, bad_guesses, missed_letters, score):
        game_record = {"word": word, "status": status, "bad_guesses": bad_guesses,
                       "missed_letters": missed_letters, "score": score}
        self.games.append(game_record)

    def print_scores(self):
        print("++")
        print("++ Game Report")
        print("++\n")
        print("Game         Word        Status          Bad Guesses         Missed Letters          Score")
        print("----         ----        ------          -----------         --------------          -----")

        # If user quits without completing game, it will still print the scoreboard but with no rows and a final
        # score of 0.
        # Else, print the normal scoreboard
        if not self.games:
            print("             " + "            " + "                " + "                              " +
                  "              0")
        else:
            for i, game in enumerate(self.games, start=1):
                print(
                    str(i) + "            " + str(game["word"]) + "        " + str(game["status"]) + "         " + str(
                        game["bad_guesses"]) + "                   " +
                    str(game["missed_letters"]) + "                       " + str(game["score"]))
            print("\n")

    def calculate_score(self, guess_word, real_word, bad_letter_guesses, bad_word_guesses, give_up=False):
        if give_up:
            # Calculate the sum of letter frequencies for covered letters and turn it into negative
            # when user gives up (selection option 't')
            covered_letters = set(real_word) - set(''.join(guess_word).replace("-", ""))

            return -sum(self.letter_frequencies[letter] for letter in covered_letters)

        if bad_letter_guesses == 0 and bad_word_guesses == 0:
            # If no bad letter guesses and no bad word guesses, return the sum of all letter frequencies
            return sum(self.letter_frequencies[letter] for letter in real_word)

        missing_letters = [letter for letter in real_word if letter not in guess_word]

        # Calculate the score for missing letters
        score = sum(self.letter_frequencies[letter] for letter in missing_letters)

        if bad_letter_guesses != 0:
            # First calculation with sum of missing letters divide by missed letters
            calculation_1 = score / bad_letter_guesses
        else:
            # Edge case not mentioned in instructions or by prof:
            # In the scenario where user makes more than 1 bad word guesses but 0 letter guesses,
            # I have decided that the program will just calculate the sum of letter frequencies
            # of all letters (since no letter guesses have been made / they're all covered)
            # without dividing by # missed letter guesses (since you cannot divide by 0).
            score_no_letter = sum(self.letter_frequencies[letter] for letter in real_word)
            return score_no_letter

        # Second calculation where you take off 10% for every bad word guesses from
        # the first calculation right above
        discount_percentage = 0.1
        discount = discount_percentage * bad_word_guesses
        calculation_2 = calculation_1 - (calculation_1 * discount)

        return calculation_2
