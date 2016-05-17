import sqlite3

conn = sqlite3.connect('test.db')

print "Opened database successfully"
onn = sqlite3.connect('test.db')

a= '1 '
b = '2 '
c='nihao '
d= 'gello '
e= 'fdasf %d'
f=a+b+c+d+e

VALUES =(9, 'Paul', 32, 'California', 20000.00 )
f= list(f)

print f

query='INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)'

conn.execute("INSERT INTO COMPANY  VALUES('22', '2', 'nihao', 'gello',  '%d')")
   
#conn.execute(query,VALUES)




print "Records created successfully"
conn.close()
