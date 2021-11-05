lista = [0, 0]
valores = list()

for contador in range(9):
    valor = int(input(f"Digite um valor para {lista}: "))
    valores.append(valor)
    lista[1] += 1
    if lista[1] == 3:
        lista[0] += 1
        lista[1] = 0

contador = 0
for item in valores:
    print(f"[{item}]", end=" ")
    contador += 1
    if contador == 3 or contador == 6:
        print()
