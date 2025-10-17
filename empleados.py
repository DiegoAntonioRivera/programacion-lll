import mysql.connector

class Empleados:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost",
                                              user="root",
                                              passwd="",
                                              database="db3")
        return conexion

    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into empleados(nombre, apellido_paterno, apellido_materno, email, fecha_contrato, notas) values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select nombre, apellido_paterno, apellido_materno, email, fecha_contrato, notas from empleados where id=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id, nombre, apellido_paterno, apellido_materno, email, fecha_contrato, notas from empleados"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def baja(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="delete from empleados where id=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount

    def modificacion(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update empleados set nombre=%s, apellido_paterno=%s, apellido_materno=%s, email=%s, fecha_contrato=%s, notas=%s where id=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount