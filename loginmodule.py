import sqlite3

conetions_db = sqlite3.connect('users.db')


cursor = conetions_db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+
"Titulo VARCHAR(255), "+
"descripcion TEXT"+
")")
conetions_db.commit

cursor.execute("INSERT INTO usuarios VALUES(null, 'Admin', 'Administrator')")
conetions_db.commit()

cursor.execute("SELECT * FROM usuarios;")
conetions_db = cursor.fetchall()

for i in conetions_db:
    print("Titulo: ", conetions_db[1])
    print("\n",i)