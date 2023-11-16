
class Game:
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
