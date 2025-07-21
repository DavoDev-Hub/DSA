def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0

        count[char] += 1

    best = None

    for char in s:
        if best is None or count[char] > count[best]:
            best = char
    print(best)


most_frequent_char("wdaavoow")

# Posible solution
# def most_frequent_char(s):
#     count = {}
#     for char in s:
#         if char not in count:
#             count[char] = 0
#
#         count[char] += 1
#
#     max_key = max(count, key=count.get)
#
#     return max_key
#
#
# s = "beookeepeoro"
# result = most_frequent_char(s)
# print(result)
