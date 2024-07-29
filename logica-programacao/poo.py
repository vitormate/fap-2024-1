class Organization:
    
    def __init__(self, name):
        self.name = name
        self.comunity = []
    
    def create(self, comunity):
        self.comunity.append(comunity)
        
    def read(self):
        print(f"{self.name}: {self.comunity}")
        
    def update(self):
        self.read()
        change = -1
        while change < 0 or change > len(self.comunity):
            change = int(input("Informe o número do item que você deseja TROCAR: "))
        new_comunity = input("Informe uma nova comunidade: ")
        self.comunity[change-1] = new_comunity
        
    def delete(self):
        self.read()
        change = -1
        while change < 0 or change > len(self.comunity):
            change = int(input("Informe o número do item que você deseja EXCLUIR: "))
        self.comunity.pop(change-1)
        self.read()
    
class Comunity:
    
    def __init__(self, name):
        self.name = name

menu = """
1 - CREATE
2 - READ
3 - UPDATE
4 - DELETE
"""       
        
comunidade1 = Comunity("Santa Cruz")
comunidade2 = Comunity("Náutico")
comunidade3 = Comunity("Sport")
comunidade4 = Comunity("Santos")
comunidade5 = Comunity("Palmeiras")
comunidade6 = Comunity("São Paulo")

organizacao1 = Organization("Pernambuco")

organizacao2 = Organization("São Paulo")

organizacao1.create(comunidade1.name)
organizacao1.create(comunidade2.name)
organizacao1.create(comunidade3.name)

organizacao2.create(comunidade4.name)
organizacao2.create(comunidade5.name)
organizacao2.create(comunidade6.name)

organizacao1.read()
organizacao2.read()