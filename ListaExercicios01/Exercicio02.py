tempos = [0, 2, 4, 6, 8]
posicoes = [0, 3, 8, 15, 24]

for i in range(len(tempos) - 1):
    delta_s = posicoes[i + 1] - posicoes[i]
    delta_t = tempos[i + 1] - tempos[i]
    v_media = delta_s / delta_t

    print(f"Intervalo {i + 1} (t = {tempos[i]}s a {tempos[i + 1]}s): Velocidade média = {v_media:.2f} m/s")