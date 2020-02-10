def iseven(n):
    print("Parameter is ", n)
    return n % 2 == 0


nums = [10, 20, 25, 35, 40]

enums = filter(iseven, nums)
# print(type(enums))
for n in enums:
    print(n)
