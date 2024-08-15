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
        print("=" * 35)

        choice = int(input("\nEscolha uma opção: "))


        if choice == 1:
            self.registerCliente()
        else:
            self.endSystem
    
    def registerCliente(self):
        name = input("Nome: ")
        email = input("Email: ")

        self.cliente.createCliente(name, email)
        self.banco.insertCliente(self.cliente)

    def endSystem(self):
        return False

            