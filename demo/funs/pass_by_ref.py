def zero(n):
    print("Address n = ", id(n))
    n = 0
    print("Address n = ", id(n))


def add_zero(lst):
    lst.append(0)


a = 100
print("Address a = ", id(a))
zero(a)
print(a)

l = [1, 2, 3]
add_zero(l)
print(l)
