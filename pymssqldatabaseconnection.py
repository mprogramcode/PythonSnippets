

#pymssql needs to be installed on the computer for this import statement to work
import pymssql

conn = pymssql.connect(server=r'127.0.0.1', user=r'ComputerName\Username', password=r'userpassword', database=r'databasename')

#Set this only if debuging queries is required
setattr(conn._conn, 'debug_queries', True)

cursor = conn.cursor()

#excute many takes a list of values each insert statement values need to be stored in a tuple
cursor.executemany(
    "INSERT INTO [table1] VALUES (%s, %s)",
    [('John Smith', 4),
     ('Jane Doe', 2),
     ("Jim smith", 1),
     ("Mike", 3),
     ('Mike T.', 3)])

conn.commit()

conn.close()    
