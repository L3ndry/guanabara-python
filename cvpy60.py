from math import factorial

valor = int(input("Digite um número para\ncalcular o seu fatoria: "))
contador = valor
fatorial = factorial(valor)

print(f"Calculando {valor}! = ", end="")
while contador > 0:
    if contador == 1:
        print(f"{contador} = {fatorial}", end="")
    else:
        print(f"{contador} x", end=" ")

    contador -= 1
