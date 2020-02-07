# Tel dir with multiple mobile numbers per person
dir = {}
while True:
    name = input("Enter name [end to stop] : ")
    if name == 'end':
        break

    mobile = input("Enter mobile number :")
    if name in dir:
        dir[name].add(mobile)  # add to existing set
    else:
        dir[name] = {mobile}   # add new key and a set

for name,numbers in dir.items():
    print(f"{name:10}  {','.join(numbers)}")

