from typing import *


def check_in_number(dig: int, num: int) -> bool:
    """Check if a digit is in a number.

    Args:
        dig (int): digit to check.
        num (int): number to look for the digit.

    Returns:
        bool: True if the digit was in the number, False otherwise.
    """
    # When number is zero, there are no more digits in the number to compare
    if num == 0:
        return False
    # Check the digit in the number is equal to the digit to find
    elif num % 10 == dig:
        return True
    # Check the next digit in the number
    else:
        return check_in_number(dig, num // 10)

def difference_aux(num1: int, num2: int, factor: int = 1) -> Tuple[int, int]:
    """Auxiliar function that computes the results.
    Function that recives two integer numbers and get two results. The first
    result composed by digits of the first number that does not belong to the
    second number. The second result composed by digits of the second number
    that does not belong to the first number.

    Args:
        num1 (int): first number.
        num2 (int): second number.

    Returns:
        Tuple[int, int]: Tuple with the results.
    """
    # No more digits, then return 0
    if num1 == 0:
        return 0
    else:
        # Get one digit from num1
        dig: int = num1 % 10

        # Check if the digit is in num2
        if check_in_number(dig, num2):
            # Ignore it and remove the digit
            return difference_aux(num1 // 10, num2, factor)
        else:
            # Add the digit to the result
            return dig * factor + difference_aux(num1 // 10, num2, factor * 10)

def difference(num1: int, num2: int) -> Tuple[int, int]:
    """Main function where arguments are validated.
    Function that recives two integer numbers and get two results. The first
    result composed by digits of the first number that does not belong to the
    second number. The second result composed by digits of the second number
    that does not belong to the first number.

    Args:
        num1 (int): first number.
        num2 (int): second number.

    Raises:
        ValueError: If num1 and num2 are not int.

    Returns:
        Tuple[int, int]: Tuple with the results.
    """
    # Check that both numbers are integer
    if not (isinstance(num1, int) and isinstance(num2, int)):
        raise ValueError("Both numbers must be integers")
    # Get both results
    else:
        return (difference_aux(num1, num2), difference_aux(num2, num1))


if __name__ == '__main__':
    assert(difference(1234, 254) == (13, 5))
    assert(difference(1468, 866124) == (0, 2))
    print("All test passed")
