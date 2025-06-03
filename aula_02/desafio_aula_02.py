# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.
# Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas para um número de ponto flutuante e prevenção de valores negativos para salário e bônus, você pode modificar o código diretamente. Isso envolve adicionar verificações adicionais após a tentativa de conversão para garantir que os valores sejam positivos.

try:
    # 1) Solicita ao usuário que digite seu nome
    nome = input("Digite seu nome: ").strip()

    # Verificar se o nome insirado é um dígito
    if nome.isdigit():
        print("Você digitou um nome inválido.")
        exit()
    # Verificar se digitou nada
    elif len(nome) == 0:
        print("Você não digitou nada.")
        exit()
    # Verificar se digitou só espaço
    elif nome.isspace():
        print("Você digitou só espaço")
        exit()
    else:
        print("Nome válido.", nome)

    # 2) Solicita ao usuário que digite o valor do seu salário    
    salario = float(input("Digite seu salário: "))
    if salario < 0:
        print("Valor inválido!")
        exit()

    # 3) Solicita ao usuário que digite o valor do bônus recebido
    bonus = float(input("Digite seu bônus: "))
    if bonus < 0:
        print("Valor inválido!")
        exit()

    # 4) Calcule o valor do bônus final
    constante_bonus = 1000
    kpi_bonus = constante_bonus + (salario * bonus)

    # 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
    print(f"Olá {nome}, o seu KPI é: {kpi_bonus:.2f}.")
    print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus:.2f}.")

except ValueError as v:
    print(v)