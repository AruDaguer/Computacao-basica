import math

def resolver_segundo_grau(a, b, c):
    """
    REPRESENTAÇÃO DA AUSÊNCIA DE RAÍZES REAIS:
    Quando Δ < 0, a equação não possui soluções no conjunto dos números reais.
    Essa ausência é representada retornando a tupla (None, None).
    """
    if a == 0:
        raise ValueError("O coeficiente 'a' não pode ser zero.") # raise ValueError é usado para indicar que a função não pode prosseguir com a execução devido a um valor inválido para 'a'.

    delta = b**2 - 4 * a * c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)
    elif delta == 0:
        x1 = -b / (2 * a)
        return (x1,)
    else:  # delta < 0
        return (None, None) # tupla (None, None) indica que não há raízes reais para a equação quadrática.

# testes

# caso Δ > 0 -> x² - 5x + 6 = 0
a1, b1, c1 = 1, -5, 6
raizes_1 = resolver_segundo_grau(a1, b1, c1)
print(
    f"Teste 1 (a={a1}, b={b1}, c={c1}): Δ > 0 -> Raízes reais: {raizes_1}"
)

# caso Δ = 0 -> x² - 4x + 4 = 0
a2, b2, c2 = 1, -4, 4
raizes_2 = resolver_segundo_grau(a2, b2, c2)
print(f"Teste 2 (a={a2}, b={b2}, c={c2}): Δ = 0 -> Raiz real: {raizes_2}")

# caso Δ < 0 -> x² + 2x + 5 = 0
a3, b3, c3 = 1, 2, 5
raizes_3 = resolver_segundo_grau(a3, b3, c3)
print(
    f"Teste 3 (a={a3}, b={b3}, c={c3}): Δ < 0 -> Raízes reais: {raizes_3}"
)