from random import randint

computador = randint(0, 5)
print("Sou seu computador. . .\nAcabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
palpite = ""
tentativas = 0

while palpite != computador:
    palpite = int(input("Qual é o seu palpite? "))
    tentativas += 1
    if palpite > 10 or palpite < 0:
        print("Oops! Digite um valor entre 0 e 10.")
        if tentativas > 0:
            tentativas -= 1
    elif palpite != computador:
        print("Mais. . . Tente mais uma vez.")

print(f"Conseguiu acertar após {tentativas} tentativa(s).")
