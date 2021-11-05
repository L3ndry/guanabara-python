soma = 0
cont = 0
for numero in range(1, 500, 2):
    multiplo_tres = numero % 3 == 0
    if multiplo_tres:
        soma += numero
        cont += 1

print(f"A soma de todos os {cont} valores somados é igual a {soma}.")
