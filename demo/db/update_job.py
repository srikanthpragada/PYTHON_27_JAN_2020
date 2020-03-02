import sqlite3

con = sqlite3.connect(r"e:\classroom\python\jan27\hr.db")
cur = con.cursor()

id = input("Enter job id :")
title = input("Enter job title :")
cur.execute("update jobs set title = ? where id = ?", (title,id))
if cur.rowcount == 1:
    con.commit()
    print("Updated job successfully!")
else:
    print("Sorry! Job id not found!")

cur.close()
con.close()
