valor_hora = float(input("Informe o valor hora: "))
horas_trabalhadas = int(input("Informe as horas trabalhadas: "))

salario_bruto = valor_hora * horas_trabalhadas

imposto = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - imposto - inss - sindicato

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"INSS: R$ {inss:.2f}")
print(f"Sindicato: R$ {sindicato:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")