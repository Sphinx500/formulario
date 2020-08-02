
import mysql.connector
class Personas():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root',
                password='1234',
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
                    'id':row[1],
                    'nombre':row[2],
                    'pri_ap':row[3],
                    'seg_ap':row[4],
                    'age':row[5],
                    'date':row[6],
                    'gender':row[7],
                    'state':row[8]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result

    def view(self,id):
        try:
            self.connect()
            query = ("SELECT * FROM students where id = %s;")
            values = (id,)
            self.cursor.execute(query,values)
            result = []
            for row in self.cursor:
                r = {
                    'id':row[1],
                    'nombre':row[2],
                    'pri_ap':row[3],
                    'seg_ap':row[4],
                    'age':row[5],
                    'date':row[6],
                    'gender':row[7],
                    'state':row[8]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)

    def insert(self, nombre, email):
        try:
            self.connect()
            query = ("INSERT INTO students (nombre, pri_ap, seg_ap, age, date, gender, state) values(%s,%s,%s,%s,%s,%s,%s);")
            values = (nombre, pri_ap, seg_ap, age, date, gender, state)
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

for row in objeto.select():
    print(row)