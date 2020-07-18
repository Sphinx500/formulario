
import mysql.connector


class Personas():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root',
                password='sphinx',
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
            query = ("SELECT * FROM personass;")
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

objeto = Personas()
objeto.connect() 

for row in objeto.select():
    print(row)