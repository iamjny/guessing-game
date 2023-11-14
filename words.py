import sys
import guess


def menu():
    mode = sys.argv[1]

    if mode == "play":
        guess.play_mode()
    elif mode == "test":
        guess.test_mode()
    else:
        print("Invalid game mode...quitting program...")


if __name__ == "__main__":
    menu()
