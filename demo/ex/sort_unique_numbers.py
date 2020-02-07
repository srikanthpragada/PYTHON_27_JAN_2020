
nums = set()  # empty set
while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break
    nums.add(num)

for n in sorted(nums):
    print(n)


