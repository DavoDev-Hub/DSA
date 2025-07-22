def pair_sum(numbers, target_sum):
    prev = {}
    for index, n in enumerate(numbers):
        comp = target_sum - n
        if comp in prev:
            return (prev[comp], index)
        prev[n] = index


result = pair_sum([3, 2, 5, 4, 1], 8)
print(result)


# brute force solution
# for i in range (0, len(numbers)):
#    for j in range(i+1, len(numbers))
#      if numbers[i] = numbers[j] == target_sum
#        return(i,j)
