import pymysql
import csv
import pandas as pd

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()

data = pd.read_csv('hasil_crawling.csv', encoding='unicode_escape')
df = pd.DataFrame(data, columns=['tanggal', 'pengguna', 'tweets'])

for row in df.itertuples():
    cursor.execute(
        'INSERT INTO tweets_tdata(date, user, tweets) VALUES (%s, %s, %s)', (row.tanggal, row.pengguna, row.tweets))

db.commit()
cursor.close()
