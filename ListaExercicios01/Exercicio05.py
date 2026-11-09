# lista de dicionários representando partículas
particulas = [
    {"nome": "Partícula 1", "massa": 2.0, "velocidade": 3.0},
    {"nome": "Partícula 2", "massa": 1.5, "velocidade": 5.0},
    {"nome": "Partícula 3", "massa": 4.0, "velocidade": 2.0},
]

for p in particulas:
    p["energia_cinetica"] = 0.5 * p["massa"] * (p["velocidade"] ** 2) # calcula a energia cinética e adiciona ao dicionário da partícula

maior_particula = max(particulas, key=lambda p: p["energia_cinetica"]) # encontra a partícula com a maior energia cinética usando a função max() e uma função lambda como chave de comparação

for p in particulas:
    print(
        f"{p['nome']}: m = {p['massa']} kg, v = {p['velocidade']} m/s -> Ec = {p['energia_cinetica']:.2f} J"
    )

print(f"\nA partícula com a maior energia cinética é a {maior_particula['nome']} ({maior_particula['energia_cinetica']:.2f} J).")