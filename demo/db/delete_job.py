import sqlite3

con = sqlite3.connect(r"e:\classroom\python\jan27\hr.db")
cur = con.cursor()

id = input("Enter job id :")
cur.execute("delete from jobs where id = ?", (id,))
if cur.rowcount == 1:
    con.commit()
    print("Deleted job successfully!")
else:
    print("Sorry! Job id not found!")

cur.close()
con.close()
