altura = float(input("Altura em metros: "))
peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7

print(f"O peso ideal para um homem de {altura}m é: {peso_ideal_homem:.1f}kg")
print(f"O peso ideal para uma mulher de {altura}m é: {peso_ideal_mulher:.1f}kg")