time = list()
jogador = dict()
partidas = list()

while True:
    jogador['Nome'] = str(input("Nome do jogador: ")).strip().title()

    quantidade_partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    for partida in range(quantidade_partidas):
        quantidade_gols = int(input(f"Quantos gols na partida {partida + 1}? "))
        partidas.append(quantidade_gols)

    gols_total = sum(partidas)
    jogador['Gols'] = partidas[:]
    jogador['Total'] = gols_total
    time.append(jogador.copy())
    jogador.clear()
    partidas.clear()

    while True:
        resposta = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if resposta in "SN":
            break
        print("Oops! Valor inválido! Digite somente 'S' ou 'N'.")
    if resposta == "N":
        break

print("-=" * 30)
print("Cod  Nome         Gols              Total")
print("- " * 30)
for contador, valor in enumerate(time):
    print(f"  {contador}  {valor['Nome']}       {valor['Gols']}          {valor['Total']}")
print("- " * 30)

dados = 0
while dados != 999:
    dados = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if dados <= len(time) - 1:
        print(f" -- Levantamento do jogador {time[dados]['Nome']}")
        for contador, gol in enumerate(time[dados]['Gols']):
            print(f"    No jogo {contador + 1} fez {gol} gol(s).")
    else:
        print(f"ERRO! Não existe jogador com código {dados}!")

print("    -- VOLTE SEMPRE --")
