"""This program allows the user to perform conversions between
measurement systems for:

    temperatures
    *** Add your conversion module names here ***

Author: R. Linley
Date: 2024-01-14

Modified by: Techmeng Aing
Section: 002
Student number: 20464661
"""

import menu
import get_number
import temperatures
import distances
2
def main():
    """Program execution starts here."""
    main_menu_choices = ["Temperatures", "Distances"]
    temperatures_menu_choices = [
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius",
        "Celsius to Kelvin",
        "Kelvin to Celsius",
        "Fahrenheit to Kelvin",
        "Kelvin to Fahrenheit"
    ]
    distances_menu_choices = [
        "Miles to Kilometers",
        "Kilometers to Miles",
        "Feet to Meters",
        "Meters to Feet",
        "Inches to Centimeters",
        "Centimeters to Inches"
    ]

    while True:
        choice = menu.do_menu("Choose a conversion type:", main_menu_choices)
        print()

        if choice is None:
            break

        if choice == 1:
            while True:
                choice = menu.do_menu("Choose a temperature conversion", temperatures_menu_choices)
                if choice is None:
                    break
                handle_temperature_choice(choice)
            print()

        elif choice == 2:
            while True:
                choice = menu.do_menu("Choose a distance conversion", distances_menu_choices)
                if choice is None:
                    break
                handle_distance_choice(choice)
            print()

def handle_temperature_choice(choice):
    if choice == 1:
        cels = get_number.input_float("\nDegrees Celsius: ")
        print(f"{cels} degrees Celsius is {temperatures.cels_to_fahr(cels):.1f} degrees Fahrenheit.")
    elif choice == 2:
        fahr = get_number.input_float("\nDegrees Fahrenheit: ")
        print(f"{fahr} degrees Fahrenheit is {temperatures.fahr_to_cels(fahr):.1f} degrees Celsius.")
    elif choice == 3:
        cels = get_number.input_float("\nDegrees Celsius: ")
        print(f"{cels} degrees Celsius is {temperatures.cels_to_kelv(cels):.1f} Kelvin.")
    elif choice == 4:
        kelv = get_number.input_float("\nKelvin: ")
        print(f"{kelv} Kelvin is {temperatures.kelv_to_cels(kelv):.1f} degrees Celsius.")
    elif choice == 5:
        fahr = get_number.input_float("\nDegrees Fahrenheit: ")
        print(f"{fahr} degrees Fahrenheit is {temperatures.fahr_to_kelv(fahr):.1f} Kelvin.")
    elif choice == 6:
        kelv = get_number.input_float("\nKelvin: ")
        print(f"{kelv} Kelvin is {temperatures.kelv_to_fahr(kelv):.1f} degrees Fahrenheit.")

def handle_distance_choice(choice):
    if choice == 1:
        miles = get_number.input_float("\nMiles: ")
        print(f"{miles} miles is {distances.miles_to_kiloms(miles):.1f} kilometers.")
    elif choice == 2:
        kilom = get_number.input_float("\nKilometers: ")
        print(f"{kilom} kilometers is {distances.kiloms_to_miles(kilom):.1f} miles.")
    elif choice == 3:
        feet = get_number.input_float("\nFeet: ")
        print(f"{feet} feet is {distances.feet_to_metres(feet):.1f} meters.")
    elif choice == 4:
        meters = get_number.input_float("\nMeters: ")
        print(f"{meters} meters is {distances.metres_to_feet(meters):.1f} feet.")
    elif choice == 5:
        inches = get_number.input_float("\nInches: ")
        print(f"{inches} inches is {distances.inches_to_centims(inches):.1f} centimeters.")
    elif choice == 6:
        centims = get_number.input_float("\nCentimeters: ")
        print(f"{centims} centimeters is {distances.centims_to_inches(centims):.1f} inches.")

if __name__ == "__main__":
    main()