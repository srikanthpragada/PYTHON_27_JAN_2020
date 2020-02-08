def max_value(*values):
    m = values[0]
    for v in values:
        if v > m:
            m = v

    return m


print(max_value('A', 'X', 'P'))
print(max_value(10, 10, 20, 30))
print(max_value(1, 3, 54, 2))
