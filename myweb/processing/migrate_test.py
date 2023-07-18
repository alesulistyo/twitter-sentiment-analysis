import pymysql

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()
cursor.execute(
    'UPDATE processing_testing INNER JOIN processing_testtemp ON processing_testing.id=processing_testtemp.id SET processing_testing.manual=processing_testtemp.dat WHERE processing_testing.id=processing_testtemp.id')
db.commit()
cursor.close()
