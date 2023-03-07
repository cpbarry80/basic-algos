import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    found_max = - float("inf")
    found_min = float("inf")

    for this_int in ints:
        if this_int > found_max:
            found_max = this_int
        if this_int < found_min:
            found_min = this_int

    return (found_min, found_max)

print('Normal Cases:')
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(-44, 44)]
random.shuffle(l)
print("Pass" if ((-44, 43) == get_min_max(l)) else "Fail")

print('Edge Cases:')
l = [i for i in range(888, 889)]
random.shuffle(l)
print("Pass" if ((888, 888) == get_min_max(l)) else "Fail")

l = []  # an empty list
print("Pass" if (None == get_min_max(l)) else "Fail")

l = [i for i in range(-44, -1)]
random.shuffle(l)
print("Pass" if ((-44, -2) == get_min_max(l)) else "Fail")