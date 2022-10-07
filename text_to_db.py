import sqlite3
from scrap_text import lst_text


conn = sqlite3.connect('mydata.db')
cursor = conn.cursor()

cursor.executemany("INSERT INTO texts (jokes) VALUES (?)", lst_text)
conn.commit()

cursor.close()