import pymysql

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()
cursor.execute('DELETE FROM tweets_tdata WHERE `usage`=2')
db.commit()
cursor.close()
