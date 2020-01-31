
sum = count = 0
while True:
    num = int(input("Enter a number [0 top stop] :"))
    if num == 0:
        break

    if num < 0:    # positive
        continue

    sum += num
    count += 1

print("Average = ", sum / count)
