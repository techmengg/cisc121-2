"""This module facilitates the presentation of text-based menus and
processing of user choices via the keyboard.

Functions:

    do_menu(title, choices)
        Print a text menu, return an int representing the user's choice
        or None if the user enters "x" or "X" to exit.

Author: R. Linley
Date: 2024-01-14
"""


def do_menu(title, choices):
    """
    Display a text menu of choices and return the user's choice (from
    keyboard input).

    All but the last choice are customizeable and are numbered 1, 2, and
    so on.  The last choice is always "X. Exit."  For example:

        ***********
        * My Menu *
        ***********
        Make a choice:

        1. Do something
        2. Do something else
        3. Do some other thing

        X. Exit

        Your choice: 

    Parameters:

        title: A str representing a title for the menu.  (In the example
            above, "My Menu" is the value of title.) If this value is the
            empty string, no title will appear.

        choices: A list of strings representing the menu choices,
            excluding "Exit".  These are presented in order of occurrence in
            the list.  As menu item numbers are generated automatically,
            these should not appear in the list.  (In the example above, the
            list ["Do something", "Do something else",
            "Do some other thing"] is the value of choices.)

    Returned value:

        An integer representing the user's choice if the user selects a
        numbered choice, or None if the user selects "x" or "X" to exit.    
    """

    # Make a list of the valid choice numbers (starting at 1).
    num_choices = len(choices)
    valid_choices = list(range(1, num_choices+1))

    # Input loop
    while True: # Loop until the user makes a valid choice.

        # Print the menu title with an asterisks border if title isn't empty.
        if title:
            title_border = "*" * (len(title) + 4)
            print(f"{title_border}\n* {title} *\n{title_border}")
            print("Make a choice:\n")

        # Print numbered choices.
        for choice_num in valid_choices:
            print(f"{choice_num}. {choices[choice_num-1]}")
        print("X. Exit\n")
        choice = input("Your choice: ")
        try:
            choice = int(choice) # Non-int input throws a ValueError.
            if (choice in valid_choices):
                return choice
        except:  # Execution branches here on non-int input. 
            pass  # Take no action on non-int input.
        if choice in ["x","X"]: # If so...
            return None  # Done here. The user wants out.
        
        # Still here? User made an invalid choice, so...
        print(f"\nInvalid choice ({choice}).\n")
        print("Valid choices: ", end="")
        if num_choices > 0:
            # Print a list of valid choices.
            print(str(list(valid_choices))[1:-1], end="")
            print(" and ", end="")
        print("X (to exit).\n\nTry again.\n")
        

if __name__ == "__main__":
    # Test code for this module.

    # If this module is being executed directly, and not by means of an
    # import, then this code will execute. Otherwise, it won't.

    # Test with an empty title, empty menu (just to make sure the code
    # won't break).
    while True:
        choice = do_menu("",[])
        if choice is None:
            break
        else:
            # Since there are no choices, execution should
            # never be able to get here.
            print(f"Problem: a choice of {choice} was \
                  returned from an empty menu.")
    print()
            
    # Test with a single item menu.
    menu = ["Only choice"]
    while True:
        choice = do_menu("One-choice menu", menu)
        if choice is None:
            break
        print(f"\nYou chose: {choice} ({menu[choice - 1]})\n")
    print()
            
    # Test with multiple menu items.        
    menu = ["This", "That", "The other thing"]
    while True:
        choice = do_menu("Three-choices menu", menu)
        if choice is None:
            break
        print(f"\nYou chose: {choice} ({menu[choice - 1]})\n")

    print("\nTests complete.")
    
    
    
