import re
import csv
import joblib
import pickle
import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

with open('model_analisis.pkl', 'rb') as handle:
    model = pickle.load(handle)

with open('count_vectorized1.pkl', 'rb') as h:
    cvec = pickle.load(h)

with open('tfid_transform1.pkl', 'rb') as t:
    tfid = pickle.load(t)

new_X_test = []

header = ['tweets', 'polarity']
with open('hasil_predict.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

with open('C:\\xampp\\temp.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)
    for i, line in enumerate(reader):
        hasil = line[0].split(',')[0]
        # print(hasil)

        transform_cvec = cvec.transform([hasil])
        transform_tfid = tfid.transform(transform_cvec)

        predict_result = model.predict(transform_tfid)
        with open('hasil_predict.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([hasil, predict_result])
