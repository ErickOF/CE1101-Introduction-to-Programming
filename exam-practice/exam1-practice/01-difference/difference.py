def check_in_number(dig: int, num: int):
    if num == 0:
        return False
    elif num % 10 == dig:
        return True
    else:
        return check_in_number(dig, num // 10)

def difference_aux(num1: int, num2: int, factor: int = 1):
    if num1 == 0:
        return 0
    else:
        dig: int = num1 % 10
        
        if check_in_number(dig, num2):
            return difference_aux(num1 // 10, num2, factor)
        else:
            return dig * factor + difference_aux(num1 // 10, num2, factor * 10)

def difference(num1: int, num2: int):
    # Check that both numbers are ineg
    if not (isinstance(num1, int) and isinstance(num2, int)):
        raise ValueError("Both numbers must be integers")
    else:
        return (difference_aux(num1, num2), difference_aux(num2, num1))


if __name__ == '__main__':
    assert(difference(1234, 254) == (13, 5))
    assert(difference(1468, 866124) == (0, 2))
    print("All test passed")
