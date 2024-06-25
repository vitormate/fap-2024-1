p1 = float(input("Informe o preço do 1 produto: "))
p2 = float(input("Informe o preço do 2 produto: "))
p3 = float(input("Informe o preço do 3 produto: "))

menor = p1

if p2 < menor:
    menor = p2

if p3 < menor:
    menor = p3

print(f"Comprar o produto que custa: R$ {menor:.2f}")