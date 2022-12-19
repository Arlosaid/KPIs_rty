from fastapi import FastAPI
import json 
from syncmssql.connect import connect_to_mssql
from controller import get_all_log
import pyodbc

app = FastAPI()

SERVER = 'amrnmcvpdb07'
DATABASE = 'QUISRTY'
USER = 'user'
PASSWORD = 'user'

cursor = connect_to_mssql(server = SERVER, database = DATABASE, username = USER, password = PASSWORD)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/log")
def get_log():
    log = get_all_log(cursor)
    print(log)
    print(type(log))
    return {}