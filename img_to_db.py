import sqlite3
from os import listdir
from os.path import isfile, join


mypath = '/home/baha/PycharmProjects/TeleBot/my_images/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

conn = sqlite3.connect('mydata.db')

cursor = conn.cursor()
for image_name in onlyfiles:

    raw_sql = f"""INSERT INTO memos (image) VALUES ('{mypath + image_name}')"""

    cursor.execute(raw_sql)
# cursor.executemany("INSERT INTO memos (image) VALUES (?)", onlyfiles)

conn.commit()
cursor.close()
