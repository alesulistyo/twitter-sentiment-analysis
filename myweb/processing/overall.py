from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
import pandas as pd
import numpy as np
import re

dfy = pd.read_csv('hasil_processing.csv', encoding='unicode_escape')


def convert(polarity):
    if polarity == 1:
        return 1
    elif polarity == 0:
        return 0
    else:
        return -1


dfy['polarity'] = dfy['polarity'].apply(convert)
dy = dfy.loc[:, 'polarity']
Y = dy.values

dfx = pd.read_csv('hasil_processing_auto.csv', encoding='unicode_escape')


def convert(polarity):
    if polarity == "[1]":
        return 1
    elif polarity == "[0]":
        return 0
    else:
        return -1


dfx['polarity'] = dfx['polarity'].apply(convert)
dx = dfx.loc[:, 'polarity']
X = dx.values

accuracy = accuracy_score(Y, X)
a = np.asarray([accuracy])
np.savetxt("overall_accuracy.csv", a, comments='',
           delimiter=",", fmt='%.2f', header='accuracy')

precision = precision_score(Y, X, average='macro')
p = np.asarray([precision])
np.savetxt("overall_precision.csv", p, comments='',
           delimiter=",", fmt='%.2f', header='precision')

recall = recall_score(Y, X, average='macro')
r = np.asarray([recall])
np.savetxt("overall_recall.csv", r, comments='',
           delimiter=",", fmt='%.2f', header='recall')

f1 = f1_score(Y, X, average='macro')
f = np.asarray([f1])
np.savetxt("overall_f1.csv", f, comments='',
           delimiter=",", fmt='%.2f', header='f1')
