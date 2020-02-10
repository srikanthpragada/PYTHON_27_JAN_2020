def even_odd_count(*nums):
    evens = odds = 0
    for v in nums:
        if v % 2 == 0:
            evens += 1
        else:
            odds += 1

    return (evens, odds)

# Unpack tuple returned by function
neven, nodd = even_odd_count(10, 20, 11, 15, 56, 67, 99)
print(neven, nodd)
