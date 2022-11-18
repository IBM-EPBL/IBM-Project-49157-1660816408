import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="Goutham17",database="user",port="3306",auth_plugin='mysql_native_password')
print("connected")
cur=db.cursor()
cur.execute("CREATE TABLE reg (id INT AUTO_INCREMENT PRIMARY KEY,username TEXT NOT NULL,password TEXT NOT NULL,name TEXT NOT NULL,email TEXT NOT NULL)");
db.commit()