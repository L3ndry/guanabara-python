numero = int(input("\033[35mMe diga um número qualquer:\033[m "))
par = numero % 2 == 0
if par:
    print("\033[36mEsse número é PAR!\033[m")
else:
    print("\033[36mEsse número é ÍMPAR!\033[m")
