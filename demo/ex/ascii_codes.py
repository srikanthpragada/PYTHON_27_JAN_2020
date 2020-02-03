st = input("Enter a string:")

for i in range(0, len(st)):
    print(st[i], ord(st[i]))

for ch in st:
    print(ch, ord(ch))
