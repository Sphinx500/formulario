
import mysql.connector


class Personas():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root',
                password='lup11t44',
                host='127.0.0.1',
                port=3306,
                database='alumnos'
            )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)
    def select(self):
        try:
            self.connect()
            query = ("SELECT * FROM students;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                r = {
                    'matricula':row[0],
                    'nombre':row[1],
                    'pri_ap':row[2],
                    'seg_ap':row[3],
                    'age':row[4],
                    'fdate':row[5],
                    'gender':row[6],
                    'state':row[7]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result
    def view(self,matricula):
        try:
            self.connect()
            query = ("SELECT * FROM students WHERE matricula = %s;")
            values = (matricula,)
            self.cursor.execute(query,values)
            result = []
            for row in self.cursor:
                diccionario = {
                    'matricula':row[0],
                    'nombre':row[1],
                    'pri_ap':row[2],
                    'seg_ap':row[3],
                    'age':row[4],
                    'fdate':row[5],
                    'gender':row[6],
                    'state':row[7]
                }
                result.append(diccionario)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
    def insert(self, matricula, nombre, pri_ap, seg_ap, age, fdate, gender, state):
        try:
            self.connect()
            query = ("INSERT INTO students(matricula,nombre,pri_ap,seg_ap,age,fdate,gender,state) values(%s,%s,%s,%s,%s,%s,%s,%s);")
            values = (matricula,nombre,pri_ap,seg_ap,age,fdate,gender,state)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

objeto = Personas()
objeto.connect() 
#objeto.insert("1718110388","lupita","espinoza","riveros","20","2000/04/05","Femenino","Hidalgo")
for row in objeto.select():
    print(row)