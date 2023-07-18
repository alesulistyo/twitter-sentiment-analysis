import pymysql

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()
cursor.execute("SELECT * FROM (SELECT 'tweets','manual' UNION ALL(SELECT tweets,manual FROM tocsv)) resulting_set INTO OUTFILE 'C:/xampp/temp.csv' FIELDS ENCLOSED BY '' TERMINATED BY ','  ESCAPED BY '' LINES TERMINATED BY '\r\n'")
db.commit()
cursor.close()
