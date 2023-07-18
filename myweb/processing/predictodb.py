import pymysql
import pandas as pd

data = pd.read_csv(
    r'hasil_predict.csv')
df = pd.DataFrame(data, columns=['tweets', 'polarity'])
df2 = df.rename(columns={'polarity': 'auto'})

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()

for row in df2.itertuples():
    cursor.execute(
        'INSERT INTO predict_temp (tweets, auto) VALUES (%s, %s)', (row.tweets, row.auto))

cursor.execute(
    "UPDATE mywebdb.predict_temp SET auto='Positif' WHERE auto='[1]'")
cursor.execute(
    "UPDATE mywebdb.predict_temp SET auto='Netral' WHERE auto='[0]'")
cursor.execute(
    "UPDATE mywebdb.predict_temp SET auto='Negatif' WHERE auto='[-1]'")

db.commit()
cursor.close()
