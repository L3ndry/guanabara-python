matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = maior = soma_coluna = 0

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        matriz[linha][coluna] = valor
        if valor % 2 == 0:
            soma_pares += valor
        if coluna == 2:
            soma_coluna += valor
        if linha == 1:
            if coluna == 0:
                maior = valor
            else:
                if valor > maior:
                    maior = valor

for linha in range(3):
    for coluna in range(3):
        print(f"[ {matriz[linha][coluna]} ]", end=" ")
    print()

print("-" * 25, f"\nA soma dos valores pares é {soma_pares}.")
print(f"A soma dos valores da terceira coluna é {soma_coluna}.")
print(f"O maior valor da segunda linha é {maior}")