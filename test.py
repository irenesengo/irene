import pypyodbc

connection=connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
'Server=localhost;'
'Database=master;'
'encrypt=yes;'
'TrustServerCertificate=yes;'
'UID=sa;'
'PWD=Password@123',autocommit = True)

cursor = connection.cursor()
SQLCommand = ("CREATE DATABASE Customer;")
cursor.execute(SQLCommand)
print('done')

connection.close()

connection=connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
'Server=localhost;'
'Database=Customer;'
'encrypt=yes;'
'TrustServerCertificate=yes;'
'UID=sa;'
'PWD=Password@123',autocommit = True)

cursor = connection.cursor()
SQLCommand = ("CREATE TABLE test(ID INT);")
cursor.execute(SQLCommand)
SQLCommand = ("INSERT INTO test VALUES(40);")
cursor.execute(SQLCommand)
SQLCommand = ("INSERT INTO test VALUES(42);")
cursor.execute(SQLCommand)
SQLCommand = ("SELECT * FROM test;")
cursor.execute(SQLCommand)
results = cursor.fetchone()
print('First result is:',results[0])
results = cursor.fetchone()
print('Next result is:',results[0])
print('done')