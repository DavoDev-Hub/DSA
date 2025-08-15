def anagrams(s1, s2):
    return char_counter(s1) == char_counter(s2)


def char_counter(s):
    counter = {}
    for char in s:
        if char not in counter:
            counter[char] = 0
        counter[char] += 1
    return counter


s1 = "cats"
s2 = "sact"

result = anagrams(s1, s2)
print(result)
