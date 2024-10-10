"""A module that provides functions related to temperature conversions.

Functions:

    cels_to_fahr(deg_c)
        Return deg_c degrees Celsius in degrees Fahrenheit.

    fahr_to_cels(deg_f)
        Return deg_f degrees Fahrenheit in degrees Celsius.

Author: R. Linley
Date: 2024-01-14

Modified by:
Section: 00
Student number: 
"""


def cels_to_fahr(deg_c):
    """Return deg_c degrees Celsius in degrees Fahrenheit."""
    return (deg_c * 9/5) + 32


def fahr_to_cels(deg_f):
    """Return deg_f degrees Fahrenheit in degrees Celsius."""
    return (deg_f - 32) * 5/9


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
    

