import re
import csv
import sys
import nltk
import string
import pymysql
import numpy as np
import pandas as pd
import preprocessor as p
import mysql.connector
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import CountVectorizer
from sqlalchemy import create_engine


db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()
x = int(sys.argv[1])
cursor.execute('UPDATE tweets_tdata AS t,(SELECT id, date, user, tweets FROM tweets_tdata WHERE `usage`=1 LIMIT %s) AS d SET `usage`=2 WHERE d.id = t.id', (x))
db.commit()
cursor.close()


db_connection_str = 'mysql+pymysql://root:@localhost/mywebdb'
db_connection = create_engine(db_connection_str)
df = pd.read_sql(
    'SELECT date, user, tweets FROM tweets_tdata WHERE `usage`=2', con=db_connection)


def cleaning(text):  # Cleaning
    text = p.clean(text)
    return text


df['tweets_bersih'] = df['tweets'].apply(lambda x: cleaning(x))


def remove_num(text):  # Case Folding - Removing Number
    text = re.sub(r"\d+", "", text)
    return text


df['tweets_bersih'] = df['tweets_bersih'].apply(lambda x: remove_num(x))


def remove_punct(text):  # Case Folding - Removing Punctuation
    text = re.sub(r'[^a-zA-z0-9]', ' ', str(text))
    text = re.sub(r'\b\w{1-2}\b', ' ', text)
    text = re.sub(r'\s\s+', ' ', text)
    return text


df['tweets_bersih'] = df['tweets_bersih'].apply(lambda x: remove_punct(x))


# Case Folding - Lowercase
df['tweets_bersih'] = df['tweets_bersih'].str.lower()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mywebdb"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM jargon")
jargons = mycursor.fetchall()
jargondict = {}
for jar in jargons:
    slang = jar[1]
    normal = jar[2]
    myjargon = {slang: normal}
    jargondict.update(myjargon)


tweets_cf = df['tweets_bersih']
tweets_split = []
for tc in tweets_cf:
    tc_split = tc.split()
    tweets_split.append(tc_split)


def replace_vals(tweets_split, jargondict):
    new_list = []
    for item in tweets_split:
        if isinstance(item, list):
            new_list.append(replace_vals(item, jargondict))
        elif item in jargondict:
            new_list.append(jargondict.get(item))
        else:
            new_list.append(item)
    return new_list


text = replace_vals(tweets_split, jargondict)


def fit_replace(text):
    text = np.array(text)
    text = ' '.join(list(text))
    return text


df['tweets_normal'] = text
df['tweets_normal'] = df['tweets_normal'].apply(fit_replace)


def tokenization(text):  # Tokenizing
    text = re.split('\W+', text)
    return text


df['tokenization'] = df['tweets_normal'].apply(
    lambda x: tokenization(x.lower()))


# Stopword Removal
stopword = nltk.corpus.stopwords.words('indonesian')


def remove_stopwords(text):
    text = [word for word in text if word not in stopword]
    return text


df['stopword_removal'] = df['tokenization'].apply(remove_stopwords)


def fit_stopwords(text):
    text = np.array(text)
    text = ' '.join(text)
    return text


df['stopword_removal'] = df['stopword_removal'].apply(fit_stopwords)


# Stemming
factory = StemmerFactory()
stemmer = factory.create_stemmer()


def stemming(text):
    text = stemmer.stem(text)
    return text


df['stemming'] = df['stopword_removal'].apply(stemming)


df['hasil'] = df['stemming']
res = df[['tweets', 'tweets_normal', 'tokenization',
          'stopword_removal', 'stemming', 'hasil']]
res.to_csv('hasil_preprocessing.csv', encoding='utf-8', index=False)
