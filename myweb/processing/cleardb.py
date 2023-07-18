import pymysql

db = pymysql.connect("localhost", "root", "", "mywebdb")
cursor = db.cursor()

cursor.execute('DELETE FROM processing_testing')
cursor.execute('ALTER TABLE processing_testing AUTO_INCREMENT=0')
cursor.execute('DELETE FROM processing_training')
cursor.execute('ALTER TABLE processing_training AUTO_INCREMENT=0')
cursor.execute('DELETE FROM processing_traintemp')
cursor.execute('ALTER TABLE processing_traintemp AUTO_INCREMENT=0')
cursor.execute('DELETE FROM processing_testtemp')
cursor.execute('ALTER TABLE processing_testtemp AUTO_INCREMENT=0')
cursor.execute('DELETE FROM predict_temp')
cursor.execute('ALTER TABLE predict_temp AUTO_INCREMENT=0')
cursor.execute('DELETE FROM tocsv')
cursor.execute('ALTER TABLE tocsv AUTO_INCREMENT=0')
cursor.execute('DELETE FROM temp')
cursor.execute('ALTER TABLE temp AUTO_INCREMENT=0')
cursor.execute(
    "UPDATE `mywebdb`.`processing_val_ovr` SET `accuracy`='0', `precision`='0', `recall`='0', `f1`='0' WHERE  `id`=1")

db.commit()
cursor.close()
