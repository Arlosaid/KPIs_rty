def get_all_log(cursor):
    cursor.execute("select top 100 Id_Log, Fecha from amrnmcvpdb07.quisrty.dbo.logrty")
    log = cursor.fetchall()
    return log