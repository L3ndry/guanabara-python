def ficha(nome_jogador, quantidade_gols):
    return f"O jogador {nome_jogador} fez {quantidade_gols} gol(s) no campeonato."


nome = str(input("Nome do jogador: ")).strip().title()
if nome.strip() == "":
    nome = "<desconhecido>"
gols = str(input("Número de Gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

mensagem = ficha(nome, gols)
print(mensagem)
