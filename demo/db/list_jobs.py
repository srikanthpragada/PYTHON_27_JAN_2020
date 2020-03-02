import sqlite3

con = sqlite3.connect(r"e:\classroom\python\jan27\hr.db")
cur = con.cursor()
cur.execute("select * from jobs order by minsal desc")

for job in cur.fetchall():
     print(f"{job[0]:10} {job[1]:30} {job[2]:10}")

cur.close()
con.close()
