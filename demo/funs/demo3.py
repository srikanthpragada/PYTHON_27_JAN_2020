def mathop(op, a, b):
    return op(a, b)


def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


print(mathop(add, 10, 20))
print(mathop(add, 'A', 'B'))
print(mathop(mul, 10, 20))


