menu = """========== Menu ==========
1. Cadastrar uma tarefa
2. Alterar uma tarefa
3. Excluir uma tarefa
4. Listar tarefas
5. Sair do sistema

"""
tasks = {}

while True:
    print(menu)
    choice = int(input("Escolha uma opção: "))

    if choice == 1:
        print("***************** CADASTRANDO TAREFA *****************")
        name = input("Nomeie a tarefa: ").capitalize()
        description = input("Informe a descrição da tarefa: ")
        tasks[name] = description
    elif choice == 2:
        print("***************** ALTERANDO TAREFA *****************")
        for task in tasks.keys():
            print(task, end=" | ")
        name = input("\nInforme a tarefa a ser alterada: ").capitalize()
        description = input("Informe a nova descrição da tarefa: ")
        tasks[name] = description
    elif choice == 3:
        print("***************** EXCLUINDO TAREFA *****************")
        for task in tasks.keys():
            print(task, end=" | ")
        name = input("\nInforme a tarefa a ser excluída: ").capitalize()
        del tasks[name]
    elif choice == 4:
        for task in tasks.keys():
            print(f"""
                Tarefa: {task}
                Descrição: {tasks[task]}""")
    elif choice == 5:
        break
    else:
        print("Escolha uma opção válida!")
