import os
import mysql.connector
from dotenv import load_dotenv
from queries import create_lessons_table_query

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

connection = mysql.connector.connect(
    user = DB_USER, 
    password = DB_PASS, 
    host = DB_HOST, 
    database = DB_NAME
)

cursor = connection.cursor()

cursor.execute(create_lessons_table_query)
