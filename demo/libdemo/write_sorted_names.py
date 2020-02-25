sf = open(r"e:\classroom\python\jan27\names2.txt", "rt")


names = set()
for line in sf.readlines():
    # strip all whitespaces
    line = line.strip()
    # Ignore blank lines
    if len(line) == 0:
        continue

    parts = line.split(",")
    names.update(parts)  # Add new names to set

sf.close()

with open(r"e:\classroom\python\jan27\sortednames.txt", "wt") as tf:
  for name in sorted(names):
      tf.write(name + "\n")



