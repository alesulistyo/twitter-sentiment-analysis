import warnings
from io import StringIO
import re
import sys
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
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report

df = pd.read_csv('C:\\xampp\\temp.csv',
                 encoding='unicode_escape')


def convert(polarity):
    if polarity == "Positif":
        return 1
    elif polarity == "Netral":
        return 0
    else:
        return -1


df['label'] = df['manual']
df['polarity'] = df['label'].apply(convert)

X = df['tweets']
y = df['polarity']

bow_transformer = CountVectorizer()
# print(df['hasil'].shape)
X = bow_transformer.fit_transform(df['tweets'])

# print(X.toarray())
#print('Shape of Sparse Matrix: ', X.shape)
#print('Amount of Non-Zero occurences: ', X.nnz)

filename1 = 'count_vectorized1.pkl'
pickle.dump(bow_transformer, open(filename1, 'wb'))

tf_transform = TfidfTransformer(use_idf=False).fit(X)
X = tf_transform.transform(X)
# print(X.shape)

filename1 = 'tfid_transform1.pkl'
pickle.dump(tf_transform, open(filename1, 'wb'))

density = (100.0 * X.nnz / (X.shape[0] * X.shape[1]))
#print('Density: {}'.format((density)))

x = int(sys.argv[1])/100
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=x, random_state=42)

nb = MultinomialNB()
nb.fit(X_train, y_train)
pred = nb.predict(X_test)

warnings.filterwarnings('ignore')

classification = classification_report(y_test, pred)
s = StringIO(classification)
with open('classification.csv', 'w') as f:
    for line in s:
        f.write(line)

accuracy = accuracy_score(y_test, pred)
a = np.asarray([accuracy])
np.savetxt("accuracy.csv", a, comments='',
           delimiter=",", fmt='%.2f', header='accuracy')

precision = precision_score(y_test, pred, average='macro')
p = np.asarray([precision])
np.savetxt("precision.csv", p, comments='',
           delimiter=",", fmt='%.2f', header='precision')

recall = recall_score(y_test, pred, average='macro')
r = np.asarray([recall])
np.savetxt("recall.csv", r, comments='',
           delimiter=",", fmt='%.2f', header='recall')

f1 = f1_score(y_test, pred, average='macro')
f = np.asarray([f1])
np.savetxt("f1.csv", f, comments='', delimiter=",", fmt='%.2f', header='f1')

final = df[['tweets', 'label', 'polarity']]
final.to_csv('hasil_processing.csv', encoding='utf-8', index=False)

model = LogisticRegression()
model.fit(X_train, y_train)

filename = 'model_analisis.pkl'
pickle.dump(model, open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)

loaded_model.predict(X_test)
