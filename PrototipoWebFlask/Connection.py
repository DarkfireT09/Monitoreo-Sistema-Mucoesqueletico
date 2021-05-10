import psycopg2

#conexión con la base de datos: recordar cambiar puerto, contraseña, y base de datos según como la tengan definida
class Connection:
    
    def __init__(self):
        self.connection = None
    
    def openConnection(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="0000",
                                               database="Cornerstone",
                                               host="localhost", 
                                               port="5432")
        except Exception as e:
            print (e)

    def closeConnection(self):
        self.connection.close()