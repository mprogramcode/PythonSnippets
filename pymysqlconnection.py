
#Creates a connection to a Mysql Database
def SQLLookupQRData(UserTextInputData):

    try:
        #Create Connection to the database
        conn = pymysql.connect(host=r'127.0.0.1', user=r'username', password=r'password', db=r'databasename')

    except Exception as e:
        print("Exeception occured:{}".format(e))
        conn.close()

    try:                                 
        # Create a cursor object
        cursorObject = conn.cursor()                                     

        # SQL query string
        sqlQuery = "select col from qrdatatable where id = " + "'" + UserTextInputData + "'"

        # Execute the sqlQuery
        cursorObject.execute(sqlQuery)

        #Fetch all the rows
        rows = cursorObject.fetchall()

        #Remove (,) from str 
        CleanedStr = str(rows[0])
        CleanedStr = CleanedStr.replace("('", "")
        CleanedStr = CleanedStr.replace("',)", "")
    
        return CleanedStr

    except Exception as e:
        print("Exeception occured:{}".format(e))

    finally:
        conn.close()
