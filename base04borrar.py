import mysql.connector
conexion1 = mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    database="db2")
cursor1 = conexion1.cursor()
sql = "DELETE FROM articulos WHERE descripcion = %s"
dato_a_borrar = ("Monitor",)

cursor1.execute(sql, dato_a_borrar)
conexion1.commit()
conexion1.close()
print("Se ha eliminado el artículo 'Monitor' de la tabla.")