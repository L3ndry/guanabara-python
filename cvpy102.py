def fatorial(numero, mostrar=False):
    """
    Teste
    Feito por -Lndr-
    """
    from math import factorial
    if mostrar:
        contador = numero
        while contador > 0:
            print(contador, end=" ")
            if contador != 1:
                print("x", end=" ")
            contador -= 1
        print("=", end=" ")
    return factorial(numero)


retorno = fatorial(5)
print(f"{retorno}")
help(fatorial)
