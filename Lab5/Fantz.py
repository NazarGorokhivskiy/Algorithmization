string = '110011011'
number = 5

array_of_powered_numbers = []


def create_array_of_binary_numbers(n):
    i = 0
    binary_number = ""

    while binary_number.__len__() <= 100:
        powered_number = pow(n, i)
        binary_number = bin(powered_number)[2:]
        array_of_powered_numbers.append(binary_number)
        i += 1


def find_min_divide_count(str):
    start_index = 1

    divide_count = 0

    while start_index <= str.__len__():
        # if there is a match
        if str[:start_index] in array_of_powered_numbers:
            # if the whole string matches powered number, the minimum number of dividing is 1
            if start_index is str.__len__():
                return 1

            divide_count_of_right_str_part = find_min_divide_count(str[start_index:])

            # otherwise check if right part can be divided and assign
            if divide_count_of_right_str_part is not 0:
                if divide_count is 0 or divide_count > divide_count_of_right_str_part + 1:
                    divide_count = divide_count_of_right_str_part + 1

        start_index += 1

    return divide_count


create_array_of_binary_numbers(number)
print(find_min_divide_count(string))
