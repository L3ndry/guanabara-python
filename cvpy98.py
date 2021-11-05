from time import sleep


def contador(inicio, fim, passo):
    print("- " * 30)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}.")
    sleep(2)
    if inicio < fim:
        for valor in range(inicio, fim + 1, passo):
            sleep(0.6)
            print(valor, end=" ")
    else:
        for valor in range(inicio, fim, passo):
            sleep(0.6)
            print(valor, end=" ")
    sleep(0.6)
    print("FIM!")


Inicio = int(input("Início: "))
Fim = int(input("Fim: "))
Passo = int(input("Passo: "))

contador(Inicio, Fim, Passo)
