from time import sleep
from random import randint


def sorteia(valores):
    print(f"Sorteando 5 valores na lista:", end=" ")

    soma = 0
    for contador in range(5):
        numeros.append(randint(0, 10))
        sleep(0.7)
        print(numeros[contador], end=" ")
        if numeros[contador] % 2 == 0:
            soma += numeros[contador]

    sleep(0.7)
    print("PRONTO!")
    print(f"Somando os valores pares de {valores}, temos {soma}")


numeros = list()
sorteia(numeros)
