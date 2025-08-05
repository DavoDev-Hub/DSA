def pair_product(numbers, target_product):
    prev_nums = {}
    for index, num in enumerate(numbers):
        complement = target_product / num
        if complement in prev_nums:
            return (prev_nums[complement], index)
        prev_nums[num] = index


result = pair_product([3, 2, 5, 4, 1], 8)
print(result)


# brute force solution
# for i in range (0, len(numbers)):
#    for j in range(i+1, len(numbers))
#      if numbers[i] * numbers[j] == target_sum
#        return(i,j)
