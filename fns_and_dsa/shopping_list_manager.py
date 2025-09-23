def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            addedItem = input("Enter the item to add: ")
            shopping_list.append(addedItem)
            print(f"{addedItem} is added to your shopping list")
            pass
        elif choice == '2':
            removedItem = input("Enter the item to remove: ")
            if removedItem in shopping_list:
                shopping_list.remove(removedItem)
                print(f"{removedItem} is removed from your shopping list")
            else:
                print(f"{removedItem} was never part of your shopping list")
            pass
        elif choice == '3':
            print("Your Shopping List")
            for item in shopping_list:
                print(item)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()