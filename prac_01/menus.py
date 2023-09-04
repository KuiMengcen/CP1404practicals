"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

MENU = "(H)ello\n(G)oodbey\n(Q)uit"
Name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", Name)
    elif choice == "G":
        print("Goodbye", Name)
    else:
        print("invalid message")
    print(MENU)
    choice = input(">>> ").upper()
print("finished message")









