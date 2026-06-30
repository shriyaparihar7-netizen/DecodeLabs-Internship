import random
import string

while True:
    print("\n----- Password Generator -----")
    print("1. Generate Password")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        length = int(input("Enter Password Length: "))

        characters = string.ascii_letters + string.digits

        password = ""

        for i in range(length):
            password = password + random.choice(characters)

        print("Generated Password:", password)

    elif choice == "2":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")