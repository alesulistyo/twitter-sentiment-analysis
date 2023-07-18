import pymysql

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()
cursor.execute(
    'INSERT INTO validation_val_data(accuracy, `precision`, recall, f1) SELECT accuracy, `precision`, recall, f1 FROM processing_val_ovr')
db.commit()
cursor.close()
