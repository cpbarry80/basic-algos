
def sqrt(number):

    """
    Calculate the floored square root of a number
    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number < 0:
        return None

    if (number == 0) or (number == 1):
        return number

    range_start = 0
    range_end = number // 2

    while range_start <= range_end:
        middle = (range_end + range_start) // 2
        proposed_root = middle * middle
        if proposed_root == number:
            return middle
        elif proposed_root < number:
            range_start = middle + 1
            result = middle
        else:
            range_end = middle - 1
    return result


print('Normal Cases:')
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass \n" if (5 == sqrt(27)) else "Fail \n")
print('Edge Cases:')
print("Pass" if (None == sqrt(-1)) else "Fail")
print("Pass" if (54443 == sqrt(2964040249)) else "Fail")