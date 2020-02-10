def factors(num):
    f = []
    for n in range(2, num // 2 + 1):
        if num % n == 0:
            f.append(n)

    return f


print(factors(356))
