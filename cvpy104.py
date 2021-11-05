def leia_inteiro(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor.isnumeric():
            return valor
        else:
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")


numero = leia_inteiro("Digite um número: ")
print(f"Você acabou de digitar o número {numero}")
