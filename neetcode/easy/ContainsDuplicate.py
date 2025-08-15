def hasDuplicate(nums):
    return len(set(nums)) != len(nums)


print(hasDuplicate([1, 2, 3, 1]))
