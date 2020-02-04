st = input("Enter a string :")

found = False
for c in st:
    if c.isdigit():
        print("String has digit")
        found = True
        break


if not found:
    print("String has no digit")
