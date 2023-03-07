def rearrange_digits(input_list, first_layer = False):
    """
        Rearrange Array Elements so as to form two number such that their sum is maximum.
        Args:
           input_list(list): Input List
           first_layer(bool): placeholder to know if we are in the first layer of the recursion (special case)
        Returns:
           (int),(int): Two maximum sums
        """

    if len(input_list) <= 1:
        return input_list

    center = len(input_list) // 2
    left = input_list[:center]
    right = input_list[center:]

    left = rearrange_digits(left)
    right = rearrange_digits(right)
    return merge(left, right, first_layer)


def merge(left, right, first_layer = False):
    merged = []
    left_index = 0
    right_index = 0

    if first_layer:  # this is a edge case to handle if this is the last merge
        num_max_left = ''
        num_max_right = ''
        num_to_left = True

        # alternating back and forth between the two sides the array was split
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                if num_to_left:
                    num_max_left = str(right[right_index]) + num_max_left
                else:
                    num_max_right = str(right[right_index]) + num_max_right
                right_index += 1
            else:
                if num_to_left:
                    num_max_left = str(left[left_index]) + num_max_left
                else:
                    num_max_right = str(left[left_index]) + num_max_right
                left_index += 1

            num_to_left = not num_to_left  # Distribute the numbers on each of the list

        # complete going thru the remaining index (one for left and one for right)
        while left_index < len(left):
            if num_to_left:
                num_max_left = str(left[left_index]) + num_max_left
            else:
                num_max_right = str(left[left_index]) + num_max_right

            left_index += 1
            num_to_left = not num_to_left

        while right_index < len(right):
            if num_to_left:
                num_max_left = str(right[right_index]) + num_max_left
            else:
                num_max_right = str(right[right_index]) + num_max_right

            right_index += 1
            num_to_left = not num_to_left

        return [int(num_max_left), int(num_max_right)]

    else:  # merge the two
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                merged.append(right[right_index])
                right_index += 1
            else:
                merged.append(left[left_index])
                left_index += 1

        merged += left[left_index:]
        merged += right[right_index:]
        return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


print('Normal Cases:')
list_num = [1, 2, 3, 4, 5]
result = rearrange_digits(list_num, True)
if result == [531, 42]:
    print('Pass')
else:
    print("Fail")

list_num = [4, 6, 2, 5, 9, 8]
result = rearrange_digits(list_num, True)
if result == [852, 964]:
    print('Pass')
else:
    print("Fail")

list_num = [1, 2, 3]
result = rearrange_digits(list_num, True)
if result == [31, 2]:
    print('Pass')
else:
    print("Fail")

print('Edge Cases:')
list_num = [1, 1, 1]
result = rearrange_digits(list_num, True)
if result == [11, 1]:
    print('Pass')
else:
    print("Fail")

list_num = [1]
result = rearrange_digits(list_num, True)
if result == [1]:
    print('Pass')
else:
    print("Fail")

list_num = []
result = rearrange_digits(list_num, True)
if result == []:
    print('Pass')
else:
    print("Fail")