import sqlite3
db = sqlite3.connect('users.db')
db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL,password TEXT NOT NULL,name TEXT NOT NULL,email TEXT NOT NULL)");
db.commit()
