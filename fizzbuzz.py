def fizz_buzz(n):
    array = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            array.append("fizzbuzz")
        elif i % 3 == 0:
            array.append("fizz")
        elif i % 5 == 0:
            array.append("buzz")
        else:
            array.append(i)
    return array


result = fizz_buzz(11)

print(result)
