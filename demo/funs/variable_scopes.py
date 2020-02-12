g = 1


def f1():
    e = 10
    global g
    g = g + 1

    def f2():
        nonlocal e
        e = e + 1
        l = 20
        print(l, e, g)

    f2()
    print(e)

f1()
