from random import randint
from time import sleep
print("Vou pensar em um número entre 0 e 5. Tente adivinhar. . .")
numero_pensado = randint(0, 5)
numero_escolhido = int(input("Em que número eu pensei? \n>>> "))
print("\033[33mPROCESSANDO. . .\033[m")
sleep(3)
if numero_escolhido == numero_pensado :
    print("\033[34mPARABÉNS, você conseguiu me vencer.\033[m")
elif numero_escolhido > 5 or numero_escolhido < 0 :
    print("Oops! Valor inválido.")
else :
    print(f"GANHEI! Eu pensei no número {numero_pensado} e não no {numero_escolhido}.")
