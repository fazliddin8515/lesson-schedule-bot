import sqlite3
from queries import create_lessons_table_query

connection = sqlite3.connect("databese.sqlite")
cursor = connection.cursor()

cursor.execute(create_lessons_table_query)
