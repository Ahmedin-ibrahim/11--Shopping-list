try:
    with open("shopping.txt", "r") as file:
        shopping_list = file.read().splitlines()
except FileNotFoundError:
    shopping_list = []


while True:
    print("\n===== MY SHOPPING LIST =====")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Show shopping list")
    print("4. Quit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        item = input("Enter item to add: ").strip()

        if item:
            shopping_list.append(item)

            with open("shopping.txt", "w") as file:
                file.write("\n".join(shopping_list))

            print(item, "added successfully!")

    elif choice == "2":
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            print("\nYour Shopping List:")

            for number, item in enumerate(shopping_list, start=1):
                print(number, ".", item)

            try:
                number = int(input("Enter the item number to remove: "))

                if 1 <= number <= len(shopping_list):
                    removed_item = shopping_list.pop(number - 1)

                    with open("shopping.txt", "w") as file:
                        file.write("\n".join(shopping_list))

                    print(removed_item, "removed successfully!")
                else:
                    print("Invalid item number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "3":
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            print("\n===== YOUR SHOPPING LIST =====")

            for number, item in enumerate(shopping_list, start=1):
                print(number, ".", item)

    elif choice == "4":
        print("Thank you for using the shopping list!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3 or 4.")
