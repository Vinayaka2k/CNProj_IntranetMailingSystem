import sqlite3
conn = sqlite3.connect('a.db')

#conn.execute('''CREATE TABLE CLIENT
#	(CFROM TEXT NOT NULL,
#	CTO TEXT NOT NULL,
#	CMESSAGE TEXT NOT NULL );''')

# conn.execute("INSERT INTO CLIENT VALUES ('Pauler', 'Sea', 'Comma')");
'''
cfrom = 'aa'
cto = 'bb'
message = 'cc'

conn.execute("INSERT INTO CLIENT VALUES (?,?,?)",(cfrom,cto,message));
'''
# cto = 'bb'
cursor = conn.execute("SELECT * FROM CLIENT")

for row in cursor:
   print(row[0])
   print(row[1])
   print(row[2])
   print('-------\n')
conn.commit()  
conn.close()
