import random


def calculate_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    user_score = float(input("Enter your score: "))
    user_result = calculate_result(user_score)
    print("Your result:", user_result)

    random_score = random.randint(0, 100)
    random_result = calculate_result(random_score)
    print("Random score:", random_score)
    print("Random result:", random_result)


main()
