def sum_numbers_recursive(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_numbers_recursive(numbers[1:])
    # return 5 + sum_numbers_recursive([2,9,10])
    # return 2 + sum_numbers_recursive([9,10])
    # return 9 + sum_numbers_recursive([9,10])
    # return 10 + sum_numbers_recursive([])
    # return []


print(sum_numbers_recursive([1, 2, 3, 4, 5]))
