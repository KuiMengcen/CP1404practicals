total_price = 0
Number_of_items = int(input("Number of items: "))
while Number_of_items < 0:
    print("Invalid number of items!")
    Number_of_items = int(input("Number of items: "))
for i in range(Number_of_items):
    Price_of_item = float(input("Price of item: "))
    total_price += Price_of_item

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {Number_of_items} items is ${total_price :.2f}")