import pymysql
import sys

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()
x = int(sys.argv[1])/100
cursor.execute('UPDATE temp AS t, (SELECT id, tweets FROM (SELECT ROW_NUMBER() OVER (ORDER BY id ASC) / COUNT(*) OVER() AS rn_pct, id, tweets FROM temp) sub WHERE sub.rn_pct <= %s) AS d SET `usage`=2 WHERE d.id = t.id', (x))
cursor.execute(
    'INSERT INTO processing_training(tweets) SELECT tweets FROM temp WHERE `usage`=2')
db.commit()
cursor.close()
