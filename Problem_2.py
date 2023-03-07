def recursive_binary_search(array, target, start_index, end_index):
    if start_index > end_index:
        return -1

    middlespot = (start_index + end_index) // 2
    middle = array[middlespot]
    if middle == target:
        return middlespot
    index_left_side = recursive_binary_search(array, target, start_index, middlespot - 1)
    index_right_side = recursive_binary_search(array, target, middlespot + 1, end_index)
    return max(index_left_side, index_right_side)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(array): Input array to search
       number (int): target to search
    Returns:
       int: Index or -1
    """

    return recursive_binary_search(input_list, number, 0, len(input_list)-1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


print('Normal Cases:')
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
print('\n')
print('Edge Cases:')
test_function([[], -1])
test_function([[1], 0])