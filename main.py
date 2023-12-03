from src.spammer import Spammer


def main():
    spammer = Spammer()
    spammer.show_response = False
    spammer.spam()


if __name__ == "__main__":
    main()
