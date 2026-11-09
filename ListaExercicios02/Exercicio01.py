def contar_temperaturas_altas(temperaturas):
    contador = 0
    for t in temperaturas:
        if t > 300:
            contador += 1
    return contador


conjunto_1 = [290, 295, 301, 298, 305]
resultado_1 = contar_temperaturas_altas(conjunto_1)
print(f"Conjunto 1: {conjunto_1}")
print(f"Quantidade de temperaturas acima de 300 K: {resultado_1}\n")

conjunto_2 = [300.0, 300.5, 285.2, 312.0, 299.9, 305.4]
resultado_2 = contar_temperaturas_altas(conjunto_2)
print(f"Conjunto 2: {conjunto_2}")
print(f"Quantidade de temperaturas acima de 300 K: {resultado_2}")