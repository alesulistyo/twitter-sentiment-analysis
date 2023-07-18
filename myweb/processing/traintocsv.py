import pymysql

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()
cursor.execute(
    'INSERT INTO tocsv(tweets, manual) SELECT tweets, manual FROM processing_training')
db.commit()
cursor.close()
