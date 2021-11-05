contador = soma = condicao = 0

while condicao != 999:
    numero = int(input("Digite um número [999 para parar]: "))
    condicao = numero
    if condicao != 999:
        contador += 1
        soma += numero

print(f"VocÊ digitou {contador} números e a soma entre eles foi {soma}")
