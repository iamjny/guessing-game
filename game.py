class Game:
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
