# Number freq
freq = {}
while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)
