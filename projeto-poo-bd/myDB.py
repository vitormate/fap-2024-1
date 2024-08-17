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
        self.cursor = self.conn.cursor()


    def connectToDatabase(self):
        try:
            connection = mysql.connector.connect(**self.config)
            # if connection.is_connected():
                # print("Conexão estabelecida com sucesso.")
            return connection
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            return None

    def insertCliente(self, cliente: Cliente):
        try:
            sql = "INSERT INTO cliente (nome, email) VALUES (%s, %s)"
            self.cursor.execute(sql, (cliente.name, cliente.email))
            self.conn.commit()
            print("Cliente criado com sucesso")
        except mysql.connector.Error as err:
            print(f"Erro ao criar Cliente: {err}")

    def getAllCliente(self):
        try:
            sql = "SELECT * FROM cliente"
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except mysql.connector.Error as err:
            print(f"Erro ao ler a tabela Cliente: {err}")

    def updateCliente(self, id, name, email):
        try:
            updates = []
            values = []

            if name:
                updates.append("nome = %s")
                values.append(name)

            if email:
                updates.append("email = %s")
                values.append(email)

            sql = f"UPDATE cliente SET {', '.join(updates)} WHERE idCliente = %s"
            values.append(id) 
            self.cursor.execute(sql, values)
            self.conn.commit()
            
            print("Cliente alterado com sucesso")
        except mysql.connector.Error as err:
            print(f"Erro ao alterar o Cliente: {err}")

    def deleteCliente(self, id):
        try:
            sql = "DELETE FROM cliente WHERE idCliente = %s"
            self.cursor.execute(sql, (id,))
            self.conn.commit()

            print("Cliente deletado com sucesso")
        except mysql.connector.Error as err:
            print(f"Erro ao deletar o Cliente: {err}")