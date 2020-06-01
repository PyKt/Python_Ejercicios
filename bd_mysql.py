import mysql.connector

# Creamos coneccion de base de datos

database = mysql.connector.connect(
    host="localhost",
    user="alberto",
    password="fava",
    database="curso_python"

)

cursor = database.cursor(buffered=True)
cursor.execute("CREATE DATABASE IF NOT EXISTS curso_python")
cursor.execute("SHOW DATABASES")

for list_database in cursor:
    print("####Listando las bases de datos en el servidor ####\n")
    print(f"{list_database}\n")

# Creacion de tablas.
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculo(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")
# Visualicion de tabla
cursor.execute("SHOW TABLES")

for list_table in cursor:
    print("####Esta es una tabla dentro de una base de datos ####\n")
    print(f"{list_table}\n")

"""Insertar registro en la bases de datos"""

cursor.execute("INSERT INTO vehiculo VALUES(null, 'Honda', 'Fit', 520000)")
database.commit()

# Crear registro a una base de tados
coches = [
    ('Seat', 'Ibiza', 21000),
    ('Renault', 'Clio', 15000),
    ('Kia', 'Rio', 500000)
]

cursor.executemany("INSERT INTO vehiculo VALUES (null, %s,%s,%s)", coches)
database.commit()

# Parametros SELET

cursor.execute ("SELECT * FROM vehiculo")
result = cursor.fetchall()

for inventario in result:
    print(inventario[3])

cursor.execute("SELECT * FROM vehiculo")
result = cursor.fetchone()
print(result)

borrador = input("escriba la marca a borrar: \n")

#Registro borrados

cursor.execute(f"DELETE FROM vehiculo WHERE marca = '{borrador}'")
database.commit()

print(cursor.rowcount, "borrados")
