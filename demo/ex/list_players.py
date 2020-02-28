from datetime import *

f =open(r"e:\classroom\python\jan27\players.txt","rt")
today = datetime.today()
players = {}

for line in f:
    parts = line.strip().split(",")
    try:
        dob =  datetime.strptime(parts[1],"%Y%m%d")
        noyears = (today - dob).days // 365
        players[parts[0]] = noyears
    except:
        pass


for name,age in sorted(players.items(), key = lambda t : t[1]):
    print(f"{name:20} {age:2}")



