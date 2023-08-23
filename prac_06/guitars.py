from prac_06.guitar import Guitar

guitar_list = [Guitar("Gibson L-5 CES", 1922, 16035.4), Guitar("Line 6 JTV-59", 2010, 1512.9)]

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar_inf = Guitar(name, year, cost)
    guitar_list.append(guitar_inf)
    print(f"{guitar_inf} added.")
    print()
    name = input("Name: ")

print("\n...snip...\n")
print("These are my guitars:")

for i, guitar in enumerate(guitar_list, 0):
    guitar_list[i].get_age()
    if guitar_list[i].is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print(f"Guitar {i+1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

