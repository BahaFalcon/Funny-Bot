import sqlite3

conn = sqlite3.connect('mydata.db')

image_table = "CREATE TABLE IF NOT EXISTS memos (id INTEGER NOT NULL PRIMARY KEY, image TEXT)"
text_table = "CREATE TABLE IF NOT EXISTS texts (id INTEGER NOT NULL PRIMARY KEY, jokes TEXT)"
cursor = conn.cursor()

cursor.execute(image_table)
cursor.execute(text_table)

conn.close()
