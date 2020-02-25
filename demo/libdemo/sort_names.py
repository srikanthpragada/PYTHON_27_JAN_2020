f = open(r"e:\classroom\python\jan27\names.txt", "rt")
for name in sorted(f.readlines()):
    print(name, end='')

f.close()
