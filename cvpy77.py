vogais = ("A", "E", "I", "O", "U")
palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS", "ESTUDAR", "PRATICAR")

for palavra in palavras:
    print(f"\nNa palavra {palavra} temos:", end=" ")
    for letra in palavra:
        if letra in vogais:
            print(letra.lower(), end=" ")
