st = input("Enter a string :")

for c in st:
    if c.isdigit():
        print("String has digit")
        break

else: # executed when for terminates
    print("String has no digit")
