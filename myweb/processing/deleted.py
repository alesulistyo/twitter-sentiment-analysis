import pymysql

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()
cursor.execute('DELETE FROM temp')
db.commit()
cursor.close()
