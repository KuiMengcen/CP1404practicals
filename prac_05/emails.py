def main():
    email_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n)")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email, name in email_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()

