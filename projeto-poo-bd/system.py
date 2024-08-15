from myDB import BancoDeDados
from Cliente import Cliente

class Sistema:
    
    def __init__(self) -> None:
        self.banco = BancoDeDados()
        self.cliente = Cliente()
        # pass

    def menu(self):
        print()
        print("*" * 10, "CRUD Cliente", "*" * 10)
        print("=" * 35)
        print("1 - Registrar Cliente")
        print("2 - Listar cliestes")
        print("=" * 35)

        choice = int(input("\nEscolha uma opção: "))


        if choice == 1:
            self.registerCliente()
        elif choice == 2:
            self.listCliente()
        else:
            self.endSystem
    
    def registerCliente(self):
        name = input("Nome: ")
        email = input("Email: ")

        self.cliente.createCliente(name, email)
        self.banco.insertCliente(self.cliente)
    
    def listCliente(self):
        records = self.banco.getAllCliente()

        print(f"\n{"Id Cliente":^40} | {"Nome":^40} | {"Email":^40}")
        for record in records:
            print("=" * 125)
            print(f"{record[0]:<40} | {record[1]:<40} | {record[2]:<40}")

    def endSystem(self):
        return False

            