MINIMUM_LENGTH = 0


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print('*' * len(password))


def get_password():
    password = input(f"Please enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Error password")
        password = input(f"Please enter password: ")
    return password


main()





