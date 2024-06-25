salario_atual = float(input("Salário atual do colaborador: "))

if salario_atual <= 280:
    percentual =  0.2
elif salario_atual < 700:
    percentual = 0.15
elif salario_atual < 1500:
    percentual = 0.1
else:
    percentual = 0.05

novo_salario = salario_atual + salario_atual * percentual

print(f"""Salário antigo: R$ {salario_atual:.2f}
Porcentagem de aumento: {percentual * 100}%
Aumento salarial: R$ {salario_atual * percentual:.2f}
Novo salário: R$ {novo_salario:.2f}""")