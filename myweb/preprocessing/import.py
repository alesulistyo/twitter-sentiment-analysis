import pymysql
import csv
import pandas as pd

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()

data = pd.read_csv('hasil_preprocessing.csv', encoding='unicode_escape')
df = pd.DataFrame(
    data, columns=['tweets', 'tweets_normal', 'tokenization', 'stopword_removal', 'stemming', 'hasil'])

for row in df.itertuples():
    cursor.execute('INSERT INTO preprocessing_predata(original, casefolding, tokenization, stopword, stemming, result) VALUES (%s, %s, %s, %s, %s, %s)',
                   (row.tweets, row.tweets_normal, row.tokenization, row.stopword_removal, row.stemming, row.hasil))
db.commit()
cursor.close()
