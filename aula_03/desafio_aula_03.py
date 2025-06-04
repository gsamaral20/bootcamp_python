#Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.
# Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas para um número de ponto flutuante e prevenção de valores negativos para salário e bônus, você pode modificar o código diretamente. Isso envolve adicionar verificações adicionais após a tentativa de conversão para garantir que os valores sejam positivos.

nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido == False:
    try:
        # 1) Solicita ao usuário que digite seu nome
        nome = input("Digite seu nome: ").strip()

        # Verificar se o nome insirado é um dígito
        if nome.isdigit():
            print("Você digitou um nome inválido.")
        # Verificar se digitou nada
        elif len(nome) == 0:
            print("Você não digitou nada.")
        # Verificar se digitou só espaço
        elif nome.isspace():
            print("Você digitou só espaço")
        else:
            nome_valido = True
            print("Nome válido.", nome)
    except ValueError as v:
        print(v)

while salario_valido == False:
    try:
        # 2) Solicita ao usuário que digite o valor do seu salário    
        salario = float(input("Digite seu salário: "))
        if salario < 0:
            print("Valor inválido!")
        else:
            salario_valido = True
    except ValueError as v:
        print(v)

while bonus_valido == False:
    try:
        # 3) Solicita ao usuário que digite o valor do bônus recebido
        bonus = float(input("Digite seu bônus: "))
        if bonus < 0:
            print("Valor inválido!")
        else:
            bonus_valido = True
    except ValueError as v:
        print(v)

# 4) Calcule o valor do bônus final
constante_bonus = 1000
kpi_bonus = constante_bonus + (salario * bonus)

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${kpi_bonus:.2f}.")