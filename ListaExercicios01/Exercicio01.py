temperaturas = [295.0, 298.5, 301.2, 290.0, 305.4]

media = sum(temperaturas) / len(temperaturas)

maior_valor = max(temperaturas)

quantidade = len(temperaturas)

print(f"Média das temperaturas: {media:.2f}")
print(f"Maior temperatura registrada: {maior_valor}")
print(f"Quantidade de medidas realizadas: {quantidade}")