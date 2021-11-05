def area (largura, altura):
    Area = largura * altura
    print(f"A área de um terreno {largura}x{altura} é de {Area}m².")

print("-- Controle de Terrenos --\n", "- " * 20)
Largura = float(input("Largura (m): "))
Altura = float(input("Alutra (m): "))

area(Largura, Altura)
