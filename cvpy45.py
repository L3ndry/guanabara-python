from random import randint
from time import sleep

itens = "Pedra", "Papel", "Tesoura"
computador = randint(0, 2)

jogador = int(input("""Suas opçôes: 
1 - PEDRA
2 - PAPEL
3 - TESOURA
Qual é a sua jogada? Digite o número correspondente.
>>> """))
jogador -= 1

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")
sleep(0.5)
print("-" * 20)

if jogador < 0 or jogador > 2:
    print("Oops! Algo errado!")
    exit()

print(f"Jogador jogou {itens[jogador]}")
print(f"O computador jogou {itens[computador]}")

venceu = "O JOGADOR VENCEU!"
if jogador == 0 and computador == 2:
    print(venceu)
elif jogador == 1 and computador == 0:
    print(venceu)
elif jogador == 2 and computador == 1:
    print(venceu)
elif jogador == computador:
    print("EMPATE!")
else:
    print("COMPUTADOR VENCEU!")
