numeros = ("um", "dois", "três", "quatro", 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    numero = int(input("Digite um número entre 1 e 10: "))
    if numero <= 0 or numero > 10:
        print("Oops! Valor inválido!")
    else:
        print(f"Você digitou o número {numeros[numero - 1]}.")
        break
