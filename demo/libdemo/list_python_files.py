import os

for (dirname, dirs, files) in os.walk(r"e:\classroom\python\jan27\demo"):
    for f in files:
        if f.endswith(".py"):
            print(dirname + "\\" + f)
