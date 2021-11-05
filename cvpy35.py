print("ANALISADOR DE TRIÂNGULOS . . .\n")

segmento1 = float(input("Primeiro segmento: "))
segmento2 = float(input("Segundo segmento0: "))
segmento3 = float(input("Terceiro segmento0: "))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    triangulo = True

else:
    triangulo = False

if triangulo:
    print("Os segmentos acima PODEM formar um triângulo!")

else:
    print("Os segmentos acima NÃO PODEM formar um triângulo.")
