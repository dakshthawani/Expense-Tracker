# statement = []
import Functions
while True:
    print("1. View all expenses")
    print("2. Add an expense")
    print("3. Delete an expense")
    print("4. Update an expense")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        Functions.viewing_all()
    elif choice == '2':
        Functions.adding()
    elif choice == '3':
        Functions.deletion()
    elif choice == '4':
        Functions.updating()
    elif choice == '5':
        print("Goodbye!")
        break


