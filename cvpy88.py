from random import randint

jogos = list()
lista = list()
contador = 0

print("", "-" * 20, "\n ", "JOGO DA MEGA SENA\n", "-" * 20 )
quantidade_jogos = int(input("\nQuantos jogos você quer que eu sorteie? "))
total = quantidade_jogos
print(f"\n-- SORTEANDO {quantidade_jogos} JOGOS --\n")

while quantidade_jogos > 0:
    contador = 6
    while contador > 0:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador -= 1

    quantidade_jogos -= 1
    jogos.append(lista[:])
    lista.clear()

for posicao in range(total):
    print(f"Jogo {posicao + 1}: {jogos[posicao]}")

print("\n-- BOA SORTE! --")
