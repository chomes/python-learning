#! /usr/bin/python3
import sys

shopping_list: list[str] = []


def view_list() -> None:
    print(f"You have {len(shopping_list)} items in your list, here's what you have so far")
    for item in shopping_list:
        print(item)



def help_menu() -> None:
    print("""
    If you want to add an item simply type the item and it will be added
    to the shopping list.

    If you want to print your current list, type "print"

    If you want to leave, type "quit"/"exit"

    If you want to see this again type "help"

    """)



def main() -> None:
    help_menu()
    while True:
        potential_item: str = input("> ").lower()
        if potential_item in ("q", "quit", "exit"):
            print("Bye!")
            sys.exit()
        elif potential_item == "print":
            view_list()
        elif potential_item in ("h", "help"):
            help_menu()
        else:
            print(f"Adding {potential_item} to the list!")
            shopping_list.append(potential_item)


if __name__ == "__main__":
    main()
