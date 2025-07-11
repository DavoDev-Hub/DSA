def max_value(nums):
    max = float("-inf")
    for n in nums:
        if n > max:
            max = n
    return max


nums = [1, 5, 8, 77, 24, 95]

max = max_value(nums)
print(max)
