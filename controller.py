def get_all_log(cursor):
    cursor.execute("select top 100 Id_Log, Fecha from amrnmcvpdb07.quisrty.dbo.logrty")
    row_headers = [x[0] for x in cursor.description ]
    rv = cursor.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    
    
    return json_data