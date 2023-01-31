import mysql.connector


class Countries:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="", database="bdejemploPy")

    def __str__(self):
        datos=self.consulta_paises()
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
    
    def consulta_paises(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM countries")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_pais(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM countries WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_pais(self,SIGLA, Nombre_de_País, Capital, Moneda):
        cur = self.cnn.cursor()
        sql='''INSERT INTO countries (SIGLA, Nombre_de_País, Capital, Moneda) 
        VALUES('{}', '{}', '{}', '{}')'''.format(SIGLA, Nombre_de_País, Capital, Moneda)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_pais(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM countries WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_pais(self,Id, SIGLA, Nombre_de_País, Capital, Moneda):
        cur = self.cnn.cursor()
        sql='''UPDATE countries SET SIGLA='{}', Nombre_de_País='{}', Capital='{}',
        Moneda='{}' WHERE Id={}'''.format(SIGLA, Nombre_de_País, Capital, Moneda,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
