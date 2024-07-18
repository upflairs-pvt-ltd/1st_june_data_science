import sqlite3 
# to create a database and to create a table
conn = sqlite3.connect('insurance.db')

query = """
create table project 
(age integer ,gender integer , bmi integer , children integer , region varchar(5),
smoker integer , health integer , prediction varchar(10))"""

cur = conn.cursor()  # cursor sql 
cur.execute(query)
print("Your database and your table is created!")
cur.close()
conn.close()

