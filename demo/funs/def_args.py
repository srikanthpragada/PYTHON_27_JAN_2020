def show_message(msg="Hello", count=1):
    for i in range(1, count + 1):
        print("Message : ", msg)


show_message("Hi", 5)
show_message("Great")
show_message()
show_message(count=3)
show_message(count=2,msg="Good Bye")
