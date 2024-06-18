valor_hora = float(input("Digite quanto você ganha por hora: R$ "))
horas_trabalhadas = int(input("Digite quantas horas você trabalhou no mês: "))

salario_total = valor_hora * horas_trabalhadas

print(f"Salário: R$ {salario_total:.2f}")