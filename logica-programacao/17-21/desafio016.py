from collections import defaultdict

controle = defaultdict(list)

print("Cadastre os membros ou 0 para sair")
membros = []
sair = 1
while sair != 0:
    membro = input("Membro: ")
    if membro == "0":
        sair = 0
    else:
        membros.append(membro)

print("Cadastre as tarefas ou 0 para sair")
tarefas = []
sair = 1
while sair != 0:
    tarefa = input("Tarefa: ")
    if tarefa == "0":
        sair = 0
    else:
        tarefas.append(tarefa)

for membro in membros:
    while True:
        print(f"Atribua tarefas a {membro}: ")
        print(tarefas)
        atribui = input("Tarefa: ")
        if atribui == "0":
            break
        else:
            controle[membro].append(atribui)
            tarefas.remove(atribui)
        
print(dict(controle))
