def calcular_energia_cinetica(massa, velocidade):
    """
    EXPLICAÇÃO DA UNIDADE (SI):
    - Massa (m): medida em quilogramas (kg)
    - Velocidade (v): medida em metros por segundo (m/s), logo v^2 fica em m^2/s^2
    - Unidade resultante: kg * (m^2/s^2) = (kg * m/s^2) * m = Newton * metro (N * m) = Joule (J)
    Portanto, a unidade da energia cinética no Sistema Internacional é o Joule (J).
    """
    return 0.5 * massa * (velocidade**2)


m1, v1 = 2, 3
ec1 = calcular_energia_cinetica(m1, v1)
print(f"Teste 1: m = {m1} kg, v = {v1} m/s -> E_c = {ec1} J")

m2, v2 = 1.5, 4.0
ec2 = calcular_energia_cinetica(m2, v2)
print(f"Teste 2: m = {m2} kg, v = {v2} m/s -> E_c = {ec2} J")