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

    # def add_game(self, word, status, bad_guesses, missed_letters, score):
    def add_game(self, word, status, bad_guesses, missed_letters):
        # game_record = {"word": word, "status": status, "bad_guesses": bad_guesses,
        #                "missed_letters": missed_letters, "score": score}
        game_record = {"word": word, "status": status, "bad_guesses": bad_guesses,
                       "missed_letters": missed_letters}
        self.games.append(game_record)

    def print_scores(self):
        print("++")
        print("++ Game Report")
        print("++\n")
        print("Game         Word        Status          Bad Guesses         Missed Letters          Score")
        print("----         ----        ------          -----------         --------------          -----")
        for i, game in enumerate(self.games, start=1):
            print(
                str(i) + "            " + str(game["word"]) + "        " + str(game["status"]) + "         " + str(game[
                                                                                                                       "bad_guesses"]) + "                   " +
                str(game["missed_letters"]))
        print("\n")

    def calculate_scores(self):
        pass
