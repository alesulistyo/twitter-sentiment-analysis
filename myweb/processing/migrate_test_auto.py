import pymysql

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()
cursor.execute(
    'UPDATE processing_testing INNER JOIN predict_temp ON processing_testing.tweets=predict_temp.tweets SET processing_testing.auto=predict_temp.auto WHERE processing_testing.tweets=predict_temp.tweets')
db.commit()
cursor.close()
