def get_valid_score():
    while True:
        score = float(input("Enter a score (0-100): "))
        if 0 <= score <= 100:
            return score
        else:
            print("Invalid score. Please try again.")


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_result(score):
    status = determine_status(score)
    print(f"Status: {status}")


def show_stars(score):
    print("*" * int(score))


def main():
    print("Welcome to the Score Program!")

    score = get_valid_score()

    choice = ""

    while choice != "Q":
        print("\nMain Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Thank you for using the Score Program. Goodbye!")
        else:
            print("Invalid option. Please try again.")


main()
