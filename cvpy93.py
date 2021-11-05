jogador = dict()
partidas = list()

jogador['Nome'] = str(input("Nome do jogador: ")).strip().title()
quantidade_partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))

for partida in range(quantidade_partidas):
    quantidade_gols = int(input(f"Quantos gols na partida {partida + 1}? "))
    partidas.append(quantidade_gols)

gols_total = sum(partidas)
jogador['Gols'] = partidas[:]
jogador['Total'] = gols_total

print("- " * 15)
print(jogador)
print("- " * 15)
for chave, valor in jogador.items():
    print(f"O campo {chave} tem o valor {valor}")
print("- " * 15)
for contador, gols in enumerate(partidas):
    if contador == 0:
        print(f"O jogador {jogador['Nome']} jogou {quantidade_partidas} partidas.")
    print(f"Na partida {contador + 1}, fez {gols} gols.")

print(f"Foi um total de {gols_total} gols.")
