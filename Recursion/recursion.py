# Recursion
# def countdown(n):
#    if n == 0:
#        return
#    print(n)
#    countdown(n - 1)


def countdown(n):
    if n == 0:
        return
    print("entering: " + str(n))
    countdown(n - 1)
    print("returning: " + str(n))


countdown(5)
