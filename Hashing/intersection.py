def intersection(a, b):
    set_a = set(a)
    return [item for item in b if item in set_a]


print(intersection([1, 2, 3, 4, 5], [2, 5, 6, 7, 8, 9]))


# My solution
# def intersection(a, b):
#  e = {}
#  result =[]
#  for i in a:
#    e[i] = 0
#  for i in b:
#    if i in e:
#      e[i] += 1
#      result.append(i)
#  return result

# brute force
# def intersection(a, b):
#  result = []
#  for item in b:
#    if item in a:
#      result.append(item)
#  return result
