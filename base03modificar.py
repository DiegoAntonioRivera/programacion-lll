import mysql.connector
conexion1=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    database="db2")
cursor1 = conexion1.cursor()
sql = "UPDATE articulos SET precio = %s WHERE descripcion = %s"
nuevos_datos = (6, "Monitor")

cursor1.execute(sql, nuevos_datos)
conexion1.commit()
conexion1.close()
print("Se han modificado los datos del artículo 'Monitor'.")