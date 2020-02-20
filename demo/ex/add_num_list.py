#  Second parameter - other - can be either a int or a list of values
def add(n, other):
    if isinstance(other,int):
        return n + other

    sum = n
    for v in other:
        sum += v

    return sum


print( add(10,20))
print( add(10, (1,2,3)))

