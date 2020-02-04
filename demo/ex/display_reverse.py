
nums = []  # Empty list

while True:
    n = int( input("Enter a number[0 to stop] :"))
    if n == 0:
        break

    nums.append(n)  # Adding a number to list

for n in reversed(nums):   #  nums[::-1]:
    print(n)

print(nums)