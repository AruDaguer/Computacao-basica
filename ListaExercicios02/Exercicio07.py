def calcular_energia_particula(particula):
    return 0.5 * particula["massa"] * (particula["velocidade"] ** 2)


def calcular_energia_total(particulas):
    energia_total = 0.0
    for p in particulas:
        energia_total += calcular_energia_particula(p)
    return energia_total

conjunto_particulas = [
    {"nome": "Partícula A", "massa": 2.0, "velocidade": 3.0},  # Ec = 0.5 * 2.0 * 3² = 9.0 J
    {"nome": "Partícula B", "massa": 1.0, "velocidade": 4.0},  # Ec = 0.5 * 1.0 * 4² = 8.0 J
    {"nome": "Partícula C", "massa": 3.0, "velocidade": 2.0},  # Ec = 0.5 * 3.0 * 2² = 6.0 J
]
e_total_funcao = calcular_energia_total(conjunto_particulas)

e1 = 0.5 * 2.0 * (3.0**2)  # 9.0 J
e2 = 0.5 * 1.0 * (4.0**2)  # 8.0 J
e3 = 0.5 * 3.0 * (2.0**2)  # 6.0 J
e_total_manual = e1 + e2 + e3  # 9.0 + 8.0 + 6.0 = 23.0 J

print("Energia Individual de cada Partícula")
for p in conjunto_particulas:
    e_p = calcular_energia_particula(p)
    print(f"{p['nome']}: {e_p:.2f} J")

print("\nComparação")
print(f"Energia total calculada pela função:  {e_total_funcao:.2f} J")
print(f"Energia total calculada manualmente: {e_total_manual:.2f} J")
print(f"Resultado idêntico: {e_total_funcao == e_total_manual}")