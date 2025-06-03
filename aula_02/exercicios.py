# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
soma = n1 + n2
print(f"A soma dos dois números é: {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero = float(input("Digite um número: "))
constante = int(5)
div = numero % constante
print(f"O resto da divisão do número por {constante} é: {div}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
multiplicacao = n1 * n2
print(f"A multiplicação de {n1} * {n2} é: {multiplicacao}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
div = n1 / n2
print(f"A divisão de {n1}/{n2} é: {div}")
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
n1 = float(input("Digite um número: "))
resultado = n1 ** 2
print(f"O quadrado do número é: {resultado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
soma = n1 + n2
print(f"A soma de {n1} + {n2} é: {soma}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
media = (n1 + n2)/2
print(f"A média é: {media}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite um número: "))
expoente = float(input("Digite um número: "))
potencia = base ** expoente
print(f"A potência de {base} por {expoente} é: {potencia}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite uma temperatura em Celsius: "))
fahrenheit = (celsius * (9/5)) + 32
print(f"A conversão de {celsius}º para Fahrenheit é: {fahrenheit}")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
raio = float(input("Insira um raio: "))
area_circulo = math.pi * (raio**2)
print(f"A área do círculo é: {area_circulo}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
string = input("Insira uma string: ")
maiuscula = string.upper()
print(maiuscula)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
string = input("Insira uma string: ")
minuscula = string.lower()
print(minuscula)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Insira uma frase: ")
resultado = frase.strip()
print(resultado)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Insira uma data no formato dd/mm/aaaa: ")
lista_data = data.split("/")
print(f"O dia é {lista_data[0]}, o mês é: {lista_data[1]} e o ano é: {lista_data[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
str1 = input("Insira uma string: ")
str2 = input("Insira uma string: ")
concat = str1 + " " + str2
print(concat)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
bool1 = True
bool2 = False
resultado = bool1 and bool2
print(resultado)


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
bool1 = True
bool2 = False
resultado = bool1 or bool2
print(resultado)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor1 = True
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
resultado = n1 == n2
print(resultado)


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
resultado = n1 != n2
print(resultado)


# #### try-except e if

# 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
try:
    celsius = float(input("Digite uma temperatura em Celsius: "))
    fahrenheit = (celsius * (9/5)) + 32
    print(f"A conversão de {celsius}º para Fahrenheit é: {fahrenheit}")
except ValueError as v:
    print(v)

# 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.
entrada = input("Insira uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")


# 23: Calculadora Simples
#Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

try: 
    n1 = float(input("Insira um número: "))
    n2 = float(input("Insira um número: "))
    operador = input("Digite um operador (+, -, *, /): ")
    if operador == "+":
        soma = n1 + n2
        print(f"A soma de {n1} + {n2} é: {soma}")
    elif operador == "-":
        subtracao = n1 - n2
        print(f"A subtração de {n1} - {n2} é: {subtracao}")
    elif operador == "*":
        multiplicacao = n1 * n2
        print(f"A multiplicacao de {n1} * {n2} é: {multiplicacao}")
    elif operador == "/":
        divisao = n1 / n2
        print(f"A divisão de {n1} / {n2} é: {divisao}")
    else:
        print("Operador inválido. Use um dos seguintes: +, -, *, /.")
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)

# 24: Classificador de Números
#Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".
try:
    numero = float(input("Insira um número: "))
    modulo = numero % 2

    #Classificador
    if numero == 0:
        print("O valor inserido é zero")
    elif numero > 0 and modulo == 0:
        print("O valor inserido é positivo e par.")
    elif numero > 0 and modulo != 0:
        print("O valor inserido é positivo e ímpar.")
    elif numero < 0 and modulo == 0:
        print("O valor inserido é negativo e par.")
    elif numero < 0 and modulo != 0:
        print("O valor inserido é negativo e ímpar.")
except ValueError as v:
    print(v)

# 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

try:
    lista = input("Insira uma lista de números separados por vírgula: ")
    lista_tratada = lista.split(",")
    lista_int = []

    for num in lista_tratada:
        lista_int.append(int(num.strip()))
        print("Lista de números: ", lista_int)
except ValueError as v:
    print(v)

