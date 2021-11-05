soma = 0
contagem = 0
for cada_numero in range(1, 7):
    numero = int(input(f"Digite o valor {cada_numero}: "))
    par = numero % 2 == 0
    if par:
        soma += numero
        contagem += 1

print(f"Você informou {contagem} números PARES e a soma entre todos eles é igual a {soma}.")
