"""This program allows the user to perform conversions between
measurement systems for:

    temperatures
    *** Add your conversion module names here ***

Author: R. Linley
Date: 2024-01-14

Modified by:
Section: 00
Student number: 
"""

import menu
import get_number
import temperatures


def main():
    """Program execution starts here."""

    # Set up main menu and sub-menus.
    main_menu_choices = ["Temperatures"]
    temperatures_menu_choices = [
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius"
    ]
    
    # Loop until user wants to quit.
    while True:
        choice = menu.do_menu("Choose a conversion type:",
                              main_menu_choices)
        print()
        
        # Did the user choose "Exit?"
        if choice is None:
            # Yes, then exit.
            break

        # User chose temperature conversions.
        if choice == 1:  

            # Loop until user wants to return to the main menu.
            while True:
                choice = menu.do_menu("Choose a temperature conversion",
                                      temperatures_menu_choices)
                
                # Did the user choose "Exit?"
                if choice is None:
                    break

                # Celsius to Fahrenheit chosen.
                if choice == 1:  
                    cels = get_number.input_float("\nDegrees Celsius: ")
                    print((f"\n{cels} degrees Celsius is "
                           f"{temperatures.cels_to_fahr(cels):.1f} "
                           "degrees Fahrenheit."))
                    
                # Fahrenheit to Celsius chosen.
                else:  
                    fahr = get_number.input_float("\nDegrees Fahrenheit: ")
                    print((f"\n{fahr} degrees Fahrenheit is "
                           f"{temperatures.fahr_to_cels(fahr):.1f} "
                           "degrees Celsius."))
                    
                print()
            print()


if __name__ == "__main__":
    main()
