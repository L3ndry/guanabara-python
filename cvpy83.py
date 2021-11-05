lista = list()
expressao = input("Digite uma expressão: ").strip()
for simbolo in expressao:
    if simbolo == "(":
        lista.append("(")
    elif simbolo == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")

if len(lista) == 0:
    print("Expressão válida!")
else:
    print("Expressão inválida!")
