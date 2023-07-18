import pymysql

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()
cursor.execute(
    'UPDATE processing_training INNER JOIN processing_traintemp ON processing_training.id=processing_traintemp.id SET processing_training.manual=processing_traintemp.dat WHERE processing_training.id=processing_traintemp.id')
db.commit()
cursor.close()
