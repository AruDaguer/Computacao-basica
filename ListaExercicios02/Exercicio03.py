def calcular_media(valores):
    """
    TRATAMENTO DE LISTA VAZIA:
    Se a lista enviada estiver vazia (not valores), a função retorna None.
    Isso evita o erro de divisão por zero (ZeroDivisionError) e indica
    que a média é indefinida quando não há dados.
    """
    if not valores: # verifica se a lista está vazia
        return None

    return sum(valores) / len(valores)

dados_1 = [10.5, 12.0, 9.8, 11.2, 10.0]
media_1 = calcular_media(dados_1)
print(f"Conjunto 1: {dados_1}")
print(f"Média: {media_1:.2f}\n")

dados_2 = [25.4, 26.1, 24.8]
media_2 = calcular_media(dados_2)
print(f"Conjunto 2: {dados_2}")
print(f"Média: {media_2:.2f}\n")

dados_vazio = []
media_vazia = calcular_media(dados_vazio)
print(f"Conjunto Vazio: {dados_vazio}")
print(f"Resultado para lista vazia: {media_vazia}")