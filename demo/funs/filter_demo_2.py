def has_space(n):
    for ch in n:
        if ch.isspace():
            return True

    return False  # Space not found


names = ["Bill", "Larry", "Ben King", "Michal Jackson"]

selnames = filter(has_space, names)

for n in selnames:
    print(n)
