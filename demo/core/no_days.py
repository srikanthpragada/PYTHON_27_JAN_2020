
month = int (input("Enter month [1-12] :"))

if month == 2:
    year = int (input("Enter year :"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        nodays = 29
    else:
        nodays = 28
elif month in [4,6,9,11]:
    nodays = 30
else:
    nodays = 31

print("No. of days = ",nodays)

