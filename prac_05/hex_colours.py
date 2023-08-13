COLOR_NAME = {"Green1": "#00ff00", "Lemon": "#fff700",
              "Iris": "#5a4fcf", "Ivory1": "#fffff0",
              "Melon": "#febaad", "Mint": "#3eb489",
              "Ochre": "#cc7722", "Pink": "#ffc0cb",
              "Black": "#000000", "Gray99": "#fcfcfc"}
print(COLOR_NAME)
choice = input("Enter a color name: ").title()
while choice != "":
    print("The code for \"{}\" is {}".format(choice, COLOR_NAME.get(choice)))
    choice = input("Enter a color name: ").title()
print("Thank you")

