import os

def print_file(filename):
    print("\n" +  filename)
    print("=" * len(filename))
    with open(filename, "r") as f:
     lineno = 1
     for line in f.readlines():
        print(f"{lineno:03} : {line}", end='')
        lineno += 1


for (dirname, dirs, files) in os.walk(r"e:\classroom\python\jan27\demo"):
    for f in files:
        if f.endswith(".py"):
            print_file(dirname + "\\" + f)
