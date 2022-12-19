import pyodbc

def connect_to_mssql(server, database, username, password):
    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
        print("Conexión a MSSQL realizada exitosamente")
        cursor = cnxn.cursor()
        print("Cursors MSSQL creado exitosamente, ahora puedes ejecutar consultas")
        return cursor
    except:
        print("Error")
        return