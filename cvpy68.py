from random import randint

quantidade_vitorias = 0
print("Vamos jogar par ou ímpar!\n")
while True:
    valor = int(input("Digite um valor: "))
    opcao = input("Par ou Ímpar? [P/I] ").upper().strip()
    computador = randint(1, 10)
    soma = valor + computador

    if soma % 2 == 0:
        par = True
    else:
        par = False

    print(f"\nVocê jogou {valor} e o computador {computador}. Total de {soma} ", end="")

    if par:
        print("DEU PAR")
    else:
        print("DEU ÍMPAR")

    if par and opcao == "P" or not par and opcao == "I":
        print("Você VENCEU!\nVamos jogar novamente. . .\n")
        quantidade_vitorias += 1
    else:
        print(f"Você PERDEU!\nGAME OVER! você venceu {quantidade_vitorias} vezes.")
        break
