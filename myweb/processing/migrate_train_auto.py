import pymysql

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()
cursor.execute(
    'UPDATE processing_training INNER JOIN predict_temp ON processing_training.tweets=predict_temp.tweets SET processing_training.auto=predict_temp.auto WHERE processing_training.tweets=predict_temp.tweets')
db.commit()
cursor.close()
