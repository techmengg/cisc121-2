"""A module that provides functions related to distance conversions.

Functions:
    miles_to_kiloms(mi)
        Return mi miles in kilometers.
    kiloms_to_miles(km)
        Return km kilometers in miles.
    feet_to_metres(ft)
        Return ft feet in meters.
    metres_to_feet(m)
        Return m meters in feet.
    inches_to_centims(ins)
        Return ins inches in centimeters.
    centims_to_inches(cm)
        Return cm centimeters in inches.

Arthor: Techmeng Aing
Section: 002
Student number: 20464661
"""

def miles_to_kiloms(mi):
    """Return mi miles in kilometers."""
    return mi * 1.60934

def kiloms_to_miles(km):
    """Return km kilometers in miles."""
    return km / 1.60934

def feet_to_metres(ft):
    """Return ft feet in meters."""
    return ft * 0.3048

def metres_to_feet(m):
    """Return m meters in feet."""
    return m / 0.3048

def inches_to_centims(ins):
    """Return ins inches in centimeters."""
    return ins * 2.54

def centims_to_inches(cm):
    """Return cm centimeters in inches."""
    return cm / 2.54

if __name__ == '__main__':
    # Test cases
    print(miles_to_kiloms(1))  # 1.60934
    print(kiloms_to_miles(1.60934))  # 1.0
    print(feet_to_metres(3.28084))  # 1.0
    print(metres_to_feet(1))  # 3.28084
    print(inches_to_centims(1))  # 2.54
    print(centims_to_inches(2.54))  # 1.0

