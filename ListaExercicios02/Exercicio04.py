def calcular_e_imprimir_energias(particulas):
    for p in particulas:
        ec = 0.5 * p["massa"] * (p["velocidade"] ** 2)
        print(f"Partícula: {p['nome']} | Energia Cinética: {ec:.2f} J")

conjunto_1 = [
    {"nome": "Partícula Alfa", "massa": 2.0, "velocidade": 3.0},
    {"nome": "Partícula Beta", "massa": 1.5, "velocidade": 5.0},
    {"nome": "Partícula Gama", "massa": 4.0, "velocidade": 2.0},
]

print("Resultados do Conjunto 1")
calcular_e_imprimir_energias(conjunto_1)

conjunto_2 = [
    {"nome": "Esfera A", "massa": 0.5, "velocidade": 10.0},
    {"nome": "Esfera B", "massa": 3.0, "velocidade": 1.0},
    {"nome": "Esfera C", "massa": 2.5, "velocidade": 4.0},
]

print("\nResultados do Conjunto 2")
calcular_e_imprimir_energias(conjunto_2)