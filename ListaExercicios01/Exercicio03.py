corpo = {
    "massa": 2.5,  # massa em kg
    "posicao": 10.0,  # posição em metros
    "velocidade": 4.0,  # velocidade em m/s
}

energia_cinetica = 0.5 * corpo["massa"] * (corpo["velocidade"] ** 2)

# adicionando a energia cinética ao dicionário do corpo
corpo["energia_cinetica"] = energia_cinetica

print("Dicionário do corpo:")
for chave, valor in corpo.items(): # itera sobre cada par chave-valor no dicionário corpo
    print(f"  {chave}: {valor}")