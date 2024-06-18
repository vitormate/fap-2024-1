peso = float(input("Informe o peso total dos peixes: "))
excesso = 0
multa = 0

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4

print(f"""
Peso: {peso} kg
Peso a mais: {excesso} kg
Multa: R$ {multa:.2f}
""")