def calcular_velocidade_media(s_inicial, s_final, t_inicial, t_final):
    """
    TRATAMENTO DE INTERVALO NULO (Δt = 0):
    Se a variação de tempo (Δt = t_final - t_inicial) for zero, a divisão
    por zero geraria um erro (ZeroDivisionError). A função trata esse caso
    retornando None, indicando que a velocidade média é indefinida.
    """
    delta_t = t_final - t_inicial

    if delta_t == 0:
        return None

    delta_s = s_final - s_inicial
    return delta_s / delta_t

s0_1, sf_1 = 0, 20
t0_1, tf_1 = 0, 5
vm1 = calcular_velocidade_media(s0_1, sf_1, t0_1, tf_1)
print(f"Teste 1: s0 = {s0_1} m, sf = {sf_1} m, t0 = {t0_1} s, tf = {tf_1} s -> Velocidade média = {vm1:.2f} m/s")

s0_2, sf_2 = 10, 50
t0_2, tf_2 = 2, 10
vm2 = calcular_velocidade_media(s0_2, sf_2, t0_2, tf_2)
print(f"Teste 2: s0 = {s0_2} m, sf = {sf_2} m, t0 = {t0_2} s, tf = {tf_2} s -> Velocidade média = {vm2:.2f} m/s")

s0_3, sf_3 = 5, 15
t0_3, tf_3 = 4, 4 # caso de teste com Δt = 0
vm3 = calcular_velocidade_media(s0_3, sf_3, t0_3, tf_3)
print(f"Teste 3 (Δt = 0): s0 = {s0_3} m, sf = {sf_3} m, t0 = {t0_3} s, tf = {tf_3} s -> Velocidade média = {vm3}")