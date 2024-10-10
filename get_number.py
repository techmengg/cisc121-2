"""This module provides functions to control keyboard input for numbers.

Functions:

    input_int(prompt)
        Return an integer entered by the user in response to prompt.

    input_float(prompt)
        Return a float entered by the user in response to prompt.

Author: R. Linley
Date: 2024-01-14
"""


def input_int(prompt):
    """
    Return an integer as entered by the user in response to the printed
    prompt. Repeat as necessary until the user enters an  integer.

    Parameters:
    
        prompt: A str. Message to the user suggesting the type of input
            required.

    Returns:
    
        An integer provided by the user via the keyboard.
    """

    # Repeat as necessary until valid user input received.
    while True:
        try:
            # Put prompt on the screen and get the user's (string) input.
            # A ValueError is triggered if the string cannot be
            # converted to an integer.
            user_input_int = int(input(prompt))
            # This will raise an exception if the cast to int fails
            # and exection will branch to the except ValueError, below.
            
            # If execution gets this far, all is well. Return the user's
            # input as an integer value.
            return user_input_int # Breaks out of the input loop.
        
        # Handle invalid input
        except ValueError:
            print("You must enter an integer value. Try again.")

def input_float(prompt):
    """
    Return a floating-point value as entered by the user in response to the
    printed prompt. Repeat as necessary until the user enters a float.

    Parameters:
    
        prompt: A str. Message to the user suggesting the type of input
            required.

        minimum_value (optional, default None): If not None, a float 
            specifying the lowest acceptable input value.

        maximum_value (optional, default None): If not None, a float 
            specifying the highest acceptable input value.

    Returns:
    
        A float provided by the user via the keyboard.

    Note:

        Integer input is allowed.
    """

    # Repeat as necessary until valid user input received.
    while True:
        try:
            # Put prompt on the screen and get the user's (string) input.
            # A ValueError is triggered if the string cannot be
            # converted to a float.
            user_input_float = float(input(prompt))
            # This will raise an exception if the cast to float fails
            # and exection will branch to the except ValueError, below.

            # If execution gets this far, all is well. Return the user's
            # input as a float value.
            return user_input_float  # Breaks out of the input loop.
        
        # Handle invalid input
        except ValueError:
            print('You must enter a floating-point value. Try again.')


if __name__ == '__main__':
    # Test code for this module.

    # Testing integer input.
    # Suggested test values:
    #   non-numeric strings, including the empty string
    #       These should all be rejected by input_int().
    #   non-integer numbers
    #       These should all be rejected by input_int().
    #   integers
    #       These should all be accepted by input_int().

    print('Testing input_int():\n')
    while True:
        i = input_int('Enter an integer: ')
        if isinstance(i, int):  # Is i an integer?
            print(f'input_int() worked. {i} returned.')
        else:
            # Ideally, execution should never get here.
            print('input_int() failed.')
        if input('Run again (y/n): ')[0] in ['N','n']:
            break
            
    # Testing floating-point number input.
    # Suggested test values:
    #   non-numeric strings, including the empty string
    #       These should all be rejected by input_float().
    #   non-floating-point numbers
    #       These should all be rejected by input_float().
    #   integers
    #       These should all be accepted by input_float().
    #   floating-point numbers
    #       These should all be accepted by input_float().

    print('Testing input_float():\n')
    while True:
        f = input_float('Enter a floating-point number: ')
        if isinstance(f, float):  # Is f a floating-point number?
            print(f'input_float() worked. {f} returned.')
        else:
            # Ideally, execution should never get here.
            print('input_float() failed.')
        if input('Run again (y/n): ')[0] in ['N','n']:
            break
            