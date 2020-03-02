import sqlite3

con = sqlite3.connect(r"e:\classroom\python\jan27\hr.db")
cur = con.cursor()

id = input("Enter job id :")
title = input("Enter job title :")
minsal = input("Enter min salary :")

cur.execute("insert into jobs values(?,?,?)", (id, title, minsal))
con.commit()
print("Added job successfully!")

cur.close()
con.close()
