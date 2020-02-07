s1 = input("Enter first string :")
s2 = input("Enter second string :")

common = set(s1) & set(s2)
for ch in common:
    print(ch)
