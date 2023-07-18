import pymysql
import pandas as pd

acc = pd.read_csv(
    r'accuracy_auto.csv')
df1 = pd.DataFrame(acc, columns=['accuracy'])

prec = pd.read_csv(
    r'precision_auto.csv')
df2 = pd.DataFrame(prec, columns=['precision'])

rec = pd.read_csv(
    r'recall_auto.csv')
df3 = pd.DataFrame(rec, columns=['recall'])

f1 = pd.read_csv(
    r'f1_auto.csv')
df4 = pd.DataFrame(f1, columns=['f1'])

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()

for row in df1.itertuples():
    cursor.execute(
        "UPDATE `mywebdb`.`processing_val_auto` SET `accuracy`='%s' WHERE  `id`=1", (row.accuracy))

for row in df2.itertuples():
    cursor.execute(
        "UPDATE `mywebdb`.`processing_val_auto` SET `precision`='%s' WHERE  `id`=1", (row.precision))

for row in df3.itertuples():
    cursor.execute(
        "UPDATE `mywebdb`.`processing_val_auto` SET `recall`='%s' WHERE  `id`=1", (row.recall))

for row in df4.itertuples():
    cursor.execute(
        "UPDATE `mywebdb`.`processing_val_auto` SET `f1`='%s' WHERE  `id`=1", (row.f1))

db.commit()
cursor.close()
