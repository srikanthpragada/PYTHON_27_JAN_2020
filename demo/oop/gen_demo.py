# Generator that generates numbers from 1 to 5
def numbers():
    for i in range(1, 6):
        yield i


def chars(st):
    for ch in st:
        if ch.isalpha():
            yield ch


for v in numbers():
    print(v)

for c in chars("Abc123Xyz"):
    print(c)
