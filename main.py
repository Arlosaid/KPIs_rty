from fastapi import FastAPI, Response
import json 
from syncmssql.connect import connect_to_mssql
from controller import get_all_log
import pyodbc
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


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
    
    return {"log":log}