try:
    v = int(input("Enter number :"))
    if v % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Sorry! Invalid number.")

print("The End")