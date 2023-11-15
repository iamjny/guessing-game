import sys
from StringDatabase import StringDatabase
from guess import Guess

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a game mode ('play' or 'test'). Exiting game...")
    else:
        mode = sys.argv[1]
        if mode not in ["play", "test"]:
            print("Invalid game mode. Exiting game...")
        else:
            string_database = StringDatabase('four_letters.txt')
            game = Guess(string_database)
            game.play(mode)
