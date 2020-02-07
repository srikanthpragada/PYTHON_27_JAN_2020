# Count char freq
st = input("Enter a string :")

for ch in sorted(set(st)):
    print(ch, st.count(ch))

