def soma(valor_1: float, valor_2: float = 10):
    """
    função que fixa o valor_2 caso não seja dado o input de nenhum número
    """
    soma: float = valor_1 + valor_2
    return soma


valor_3 = soma(10, 0)
print(valor_3)

valor_4 = soma(1, 2)
print(valor_4)
