nomes = list()
medias = list()
notas = list()
temporario = list()

while True:
    nome = str(input("Nome: ")).strip().title()
    nomes.append(nome)
    nota1 = int(input("Nota 1: "))
    temporario.append(nota1)
    nota2 = int(input("Nota 2: "))
    temporario.append(nota2)
    media = (nota1 + nota2) / 2
    medias.append(media)
    notas.append(temporario[:])
    temporario.clear()

    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()
    if resposta == "N":
        break
    elif resposta == "S":
        print("Continuando...")
    else:
        exit()

print("", "- " * 20, "\n  No.   NOME      MÉDIA\n", "- " * 20)

for contador in range(len(nomes)):
    print(f"  {contador}     {nomes[contador]}       {medias[contador]}")
print("", "- " * 20)

while True:
    resposta = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if resposta <= len(nomes) - 1:
        print(f"Notas de {nomes[resposta]} são {notas[resposta]}")
    elif resposta == 999:
        print("Finalizando...\nVOLTE SEMPRE!")
        break
    else:
        continue
