from time import sleep
from random import randint


def maior_numero(* valores):
    """
    Teste
    """
    maior = 0
    print("Analisando os valores passados...")
    for valor in valores:
        print(valor, end=" ")
        sleep(0.6)
        if valor > maior:
            maior = valor
    print(f"Foram informados {len(valores)} valores ao todo.")
    print(f"O maior valor informado foi {maior}.")


maior_numero(randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
help(maior_numero)
