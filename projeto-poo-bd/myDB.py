import mysql.connector
from Cliente import Cliente

class BancoDeDados:
    def __init__(self) -> None:
        self.config = {
            'user' : 'root',
            'host' : 'localhost',
            'password' : 'vitor133',
            'database' : 'vendas',
            'raise_on_warnings' : True
        }
        self.conn = self.connectToDatabase()

    def connectToDatabase(self):
        try:
            connection = mysql.connector.connect(**self.config)
            self.cursor = self.conn.cursor()
            if connection.is_connected():
                print("Conexão estabelecida com sucesso.")
            return connection
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            return None

    def closeConnection(self):
        self.cursor.close()

    def createCliente(self, cliente: Cliente):
        try:
            cursor = self.conn.cursor()
            sql = f"INSERT INTO cliente (nome, email) VALUES ({cliente.name}, {cliente.email})"
            cursor.execute(sql)
            self.conn.commit()
            print("Cliente criado com sucesso")
        except mysql.connector.Error as err:
            print(f"Erro ao criar Cliente: {err}")
        finally:
            cursor.close()
