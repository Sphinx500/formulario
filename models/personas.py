
import mysql.connector


class Personas():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root',
                password='Sphonx',
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
                    'id':row[0],
                    'nombre':row[1],
                    'pri_ap':row[2],
                    'seg_ap':row[3],
                    'age':row[4],
                    'date':row[5],
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

objeto = Personas()
objeto.connect() 

for row in objeto.select():
    print(row)