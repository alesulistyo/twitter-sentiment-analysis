import pymysql
import sys

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()
#x = int(sys.argv[1])/100
cursor.execute(
    'UPDATE temp AS t, (SELECT id, tweets FROM temp WHERE `usage`=1) AS d SET `usage`=3 WHERE d.id = t.id')
cursor.execute(
    'INSERT INTO processing_testing(tweets) SELECT tweets FROM temp WHERE `usage`=3')
db.commit()
cursor.close()
