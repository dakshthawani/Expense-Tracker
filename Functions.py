import json


def read_only(filename="expenses.json"):
    try:
        with open(filename, "r") as file_read:
            statement_read = json.load(file_read)
            return statement_read
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def write_only(new_change, filename="expenses.json"):
    with open(filename, "w") as file_write:
        json.dump(new_change, file_write)


def adding():
    try:
        description = input("Enter the description: ")
        amount = int(input("Enter the amount: "))
        category = input("Enter the Category: ")
        date = int(input("Enter the date of transaction: "))
        statement = read_only()
        statement.append({
            "description": description,
            "amount": amount,
            "category": category,
            "date": date
        })
        write_only(statement)
        print(statement)
    except ValueError:
        print("Wrong Input, Enter todo number after edit!!")


def updating():
    try:
        index_val = int(input("Enter the entry number you want to edit: "))
        statement = read_only()
        print(statement[index_val-1])
        update_choice = input("Enter the choice you want to update: ")
        statement[index_val][update_choice] = input("Enter the update now: ")
        write_only(statement)
        print("Entry updated successfully,")
    except ValueError:
        print("Wrong Input!!")
    except IndexError:
        print("Wrong input, Value out of index range!!")
    # else:
    #     print("Invalid entry number.")


def deletion():
    index_val = int(input("Enter the entry number you want to delete: "))
    statement = read_only()
    if 0 < index_val <= len(statement):
        print(statement[index_val - 1])
        alert = input("Are you sure you want to delete this entry, Y or N? ")
        if alert.title() == "Y":
            statement.pop(index_val - 1)
            write_only(statement)
            print("Entry deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Invalid entry number.")


# def view_by_category():
#     statement = read_only()
#     category = input("Enter the category to filter by: ")
#     if statement == []:
#         print("No expenses to show.")
#     else:
#         for "category": category in statement:


def viewing_all():
    statement = read_only()
    if statement == []:
        print("No expenses to show.")
    else:
        for index, i in enumerate(statement):
            print(f"{index + 1}. {i}")