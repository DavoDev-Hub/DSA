def pairs(elements):
    arr = []
    for i in range(0, len(elements)):
        for e in range(i + 1, len(elements)):
            p = [elements[i], elements[e]]
            arr.append(p)
    return arr


print(pairs(["a", "b", "c"]))
