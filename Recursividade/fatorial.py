def fat(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fat(n - 1)


def mult(x, y):
    if x == 0:
        return 0
    elif x == 1:
        return y
    else:
        return y + mult(x - 1, y)