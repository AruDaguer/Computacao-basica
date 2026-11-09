temperaturas = [290, 295, 301, 298, 305]

contador = 0

for T in temperaturas:
    if T > 300:
        contador += 1

print(f"Quantidade de temperaturas acima de 300 K: {contador}")