
ms = "This is fine"
ss = "is"

pos = -1
while True:
    pos = ms.find(ss,pos+1)
    if pos == -1:
        break
    else:
        print(pos)