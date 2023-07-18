import pymysql
import sys

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()
x = int(sys.argv[1])
cursor.execute('UPDATE preprocessing_predata AS pr,(SELECT id, result FROM preprocessing_predata WHERE `usage`=1 LIMIT %s) AS d SET `usage`=2 WHERE d.id = pr.id', (x))
cursor.execute(
    'INSERT INTO temp(tweets) SELECT result FROM preprocessing_predata WHERE `usage`=2')
db.commit()
cursor.close()
