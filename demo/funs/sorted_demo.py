names = ["Xy", "Abcdef", "Pqrs", "Def", "Aaa"]

# for n in sorted(names, key=len):
#     print(n)

for n in sorted(names, key=lambda s: s[::-1]):
    print(n)
