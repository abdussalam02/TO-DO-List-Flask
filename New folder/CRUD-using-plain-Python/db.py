import mysql.connector as my

con = my.connect(host="localhost",  user="root", password="admin")
cur = con.cursor()
cur.execute("DROP DATABASE pythondb")
cur.execute("CREATE DATABASE pythondb")
cur.execute("CREATE TABLE pythondb.Students(roll INT NOT NULL AUTO_INCREMENT, name VARCHAR(50) NOT NULL, age INT NOT NULL, PRIMARY KEY (roll))")

con.close()