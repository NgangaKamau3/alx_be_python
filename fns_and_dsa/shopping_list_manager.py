def display_menu():
    """A simple interface for managing a shopping list.
       Users can add items, remove items and view the current list of items. 
       The script shouls start with an empty shopping list and provide a menu-driven interface for user interaction.
       The user interface uses a loop to continuously prompt the user for actions to perform until they choose to exit.
       For adding an item, the user is prompted to enter the item name. 
       For removing an item, the user is prompted to enter the item name to be removed.
       The current shopping list can be displayed at any time.
       The script should handle cases where the user tries to remove an item that is not in the list gracefully.
"""
    shopping_list = []
    
    while True:
        print("\nShopping List Manager")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Shopping List")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")
        
        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")
        
        elif choice == '3':
            if shopping_list:
                print("Current Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is currently empty.")
        
        elif choice == '4':
            print("Exiting Shopping List Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option (1-4).")
