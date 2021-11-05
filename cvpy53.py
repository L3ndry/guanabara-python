frase = input("Digite uma frase: ")
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for item in range(len(junto)- 1, -1, -1):
    inverso += junto[item]

print(f"O inverso de {junto} é {inverso}")
if junto == inverso:
    print("Temos um pelíndromo!")
else:
    print("Não é pelíndromo.")
