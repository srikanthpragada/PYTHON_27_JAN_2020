sum = 0
count = 0
while True:
    try:
        v = int(input("Enter a number [0 to stop] :"))
        if v == 0:
            break
        sum += v
        count += 1
    except ValueError:
        pass

if count > 0:
    print("Average = ", sum / count)
