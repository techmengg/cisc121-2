"""A module that provides functions related to temperature conversions.

Functions:

    cels_to_fahr(deg_c)
        Return deg_c degrees Celsius in degrees Fahrenheit.

    fahr_to_cels(deg_f)
        Return deg_f degrees Fahrenheit in degrees Celsius.

Author: R. Linley
Date: 2024-01-14

Modified by: Techmeng Aing
Section: 002
Student number: 20464661
"""


def cels_to_fahr(deg_c):
    """Return deg_c degrees Celsius in degrees Fahrenheit."""
    return (deg_c * 9/5) + 32


def fahr_to_cels(deg_f):
    """Return deg_f degrees Fahrenheit in degrees Celsius."""
    return (deg_f - 32) * 5/9

def cels_to_kelv(deg_c):  # Modification Starts Here:
    """Return deg_c degrees Celsius in Kelvin."""
    return deg_c + 273.15

def kelv_to_cels(kelv):
    """Return kelv Kelvin in degrees Celsius."""
    return kelv - 273.15

def fahr_to_kelv(deg_f):
    """Return deg_f degrees Fahrenheit in Kelvin."""
    return (deg_f - 32) * 5/9 + 273.15

def kelv_to_fahr(kelv):
    """Return kelv Kelvin in degrees Fahrenheit."""
    return (kelv - 273.15) * 9/5 + 32

if __name__ == '__main__':
    # Test code for module.
    print(cels_to_fahr(100))  # 212.0
    print(fahr_to_cels(212))  # 100.0
    print(cels_to_fahr(0))  # 32.0
    print(fahr_to_cels(32))  # 0.0
    print(fahr_to_cels(0))  # -17.8 (approximately)
    print(cels_to_fahr(-17.8))  # 0.0 (approximately)
    print(cels_to_fahr(fahr_to_cels(0)))  # 0.0
    print(fahr_to_cels(cels_to_fahr(1)))  # 1.0 (approximately)

    print(cels_to_kelv(0))  # 273.15 | ADDED
    print(kelv_to_cels(273.15))  # 0.0 | ADDED
    print(fahr_to_kelv(32))  # 273.15 | ADDED
    print(kelv_to_fahr(273.15))  # 32.0 | ADDED
    

