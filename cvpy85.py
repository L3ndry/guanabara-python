lista = [[], []]
for contador in range(7):
    valor = int(input(f"Digite o {contador + 1}o valor: "))

    if valor % 2 == 0: # Se o valor for ímpar.
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print(f"Os valores pares digitados foram: {sorted(lista[0])}")
print(f"Os valores ímpares digitados foram: {sorted(lista[1])}")
