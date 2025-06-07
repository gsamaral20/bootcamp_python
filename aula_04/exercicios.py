#Exercícios de Listas e Dicionários
# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
lista_numeros: list = []

for i in range(1,11):
    lista_numeros.append(i)

for numero in lista_numeros:
    quadrado: int = numero**2
    print(quadrado)


# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista: list = ["Python", "Java", "C++", "JavaScript"]
lista.remove("C++")
lista.append("Ruby")
print(lista)


# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
from typing import Dict, Any
livros: Dict[str, Any] = {
    "Título": "1984",
    "Autor": "George Orwell",
    "Ano": 1949
}

lista_elementos: list = livros.items()

for elementos in lista_elementos:
    print(elementos)

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
dict_palavras: dict = {}
string = "Atirei o pau no gato, mas o gato não morreu"
#lista_string = string.split()

for palavra in string: #lista_string:
    if palavra.lower() in dict_palavras:
        dict_palavras[palavra.lower()] += 1
    else:
        dict_palavras[palavra.lower()] = 1
print(dict_palavras)

#5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
lista_frutas: list = ["maçã", "banana", "cereja"]
preco_frutas: dict = {
    "maçã": 0.45, 
    "banana": 0.30, 
    "cereja": 0.65
    }

total: float = 0
for fruta in lista_frutas:
    total += preco_frutas[fruta]
print(total)

# 6. Eliminação de Duplicatas
#Objetivo: Dada uma lista de emails, remover todos os duplicados.

emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]

#Usar set() em uma sequência elimina elementos duplicados (entrentanto retorna um dicionário).

def eliminar_duplicados(lista: list) -> list:
    lista_emails = list(set(lista))
    return lista_emails

lista_emails = eliminar_duplicados(emails)
print(lista_emails)



# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
def filtrar_maior_idade(lista: list) -> list:
    lista_filtrada: list = []
    for idade in lista:
        if idade >= 18:
            lista_filtrada.append(idade)
    return lista_filtrada

idade = [2,3,55,123,14,17,19,20,18]

print(filtrar_maior_idade(idade))

# 8.Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Carol", "idade": 25},
    {"nome": "Bob", "idade": 20}
]
# Ordene a lista 'pessoas' usando sorted(), com key = lambda que retorna o nome
lista_ordenada = sorted(pessoas, key=lambda pessoa: pessoa['nome'])
print(lista_ordenada)

# 9. Agregação de Dados
#Objetivo: Dado um conjunto de números, calcular a média.

def media(lista: list) -> float:
    soma: float = 0
    for numero in lista:
        soma += numero
    media = soma/len(lista)
    return media

numeros = [12,65,12,45,323,21]
print(media(numeros))

# A função sum(lista) soma automaticamente todos os elementos numéricos da lista,
# eliminando a necessidade de usar um loop manual para acumular a soma.

def media(lista: list) -> float:
    soma: float = sum(lista)
    media: float = soma/len(lista)
    return media

numeros = [12,65,12,45,323,21]
print(media(numeros))

# 10. Divisão de Dados em Grupos
#Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
def divisao_par_impar(lista: list) -> list:
    lista_par: list = []
    lista_impar: list = []
    for numero in lista:
        if numero % 2 == 0:
            lista_par.append(numero)
        else:
            lista_impar.append(numero)
    return lista_par, lista_impar

x = [2, 9, 4, 3, 982, 77]

print(divisao_par_impar(x))

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

def atualizar_preco(produtos: dict, id: int, preco: float) -> dict:
    dados: dict = produtos.copy()
    for produto in produtos:
        if produto["id"] == id:
            produto["preço"] = preco
    return produtos

print(atualizar_preco(produtos, 3, 250))


# 12. Fusão de Dicionários
#Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

# O operador | junta dois dicionarios
dicionario3 = dicionario1 | dicionario2
print(dicionario3)

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
estoque_positivo: dict = {}
for i in estoque:
        if estoque[i] > 0:
            estoque_positivo[i] = estoque[i]
print(estoque_positivo)

#for k, v in estoque.items():
    #print(f"k: {k}, v: {v}")

# Define uma função que recebe um dicionário como parâmetro e retorna outro dicionário
def filtrar_produtos(dicionario: dict) -> dict:
    # Cria um dicionário vazio para armazenar os produtos com quantidade maior que 0
    estoque_positivo: dict = {}
    # Percorre cada par chave-valor (produto e quantidade) no dicionário original
    for produto, quantidade in dicionario.items():
        # Verifica se a quantidade do produto é maior que 0
        if quantidade > 0:
            # Adiciona o produto ao dicionário filtrado
            estoque_positivo[produto] = quantidade
        # Retorna o dicionário apenas com os produtos que têm estoque
    return estoque_positivo

print(filtrar_produtos(estoque))

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
dicionario = {"a": 1, "b": 2, "c": 3}
lista1: list = []
lista2: list = []

for chave, valor in dicionario.items():
    lista1.append(chave)
    lista2.append(valor)

print(f"lista1: {lista1}")
print(f"lista2: {lista2}")


chaves = list(dicionario.keys())   # Converte as chaves do dicionário em uma lista
valores = list(dicionario.values())  # Converte os valores do dicionário em uma lista
print("Chaves:", chaves)
print("Valores:", valores)

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
texto: str = "engenharia de dados"
frequencia: dict = {}

for caracter in texto:
    if caracter in frequencia:
        frequencia[caracter] += 1
    else:
        frequencia[caracter] = 1
print(frequencia)

# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

# Função que recebe uma lista de números e retorna a soma de todos eles
def soma(lista_numeros: list) -> float:
    soma_numeros: float = sum(lista_numeros)
    return soma_numeros

lista_numeros: list = [64, 34, 25, 12, 22, 11, 90]
print(soma(lista_numeros))

# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

def verificar_numero_primo(numero: int):
    # Inicializa o resultado como False (não primo)
    resultado: bool = False
    # Verifica se o valor passado é um número inteiro
    if not isinstance(numero, int):
        print("Insira um número inteiro.")  # Mensagem de erro para valores não inteiros
        return None  # Encerra a função retornando None
    # Verifica se o número é par (e diferente de 2)
    elif numero % 2 == 0:
        return False  # Números pares (exceto 2) não são primos
    else:
        return True  # Assume que números ímpares são primos (simplificação)

print(verificar_numero_primo(9))  # Testa a função com o número 9

# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
texto: str = "Gabriel"

# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
texto: str = "Gabriel"

def reverter_string(texto: str) -> str:
    # Usamos slicing com passo -1 para inverter a string
    texto_revertido: str = texto[::-1]
    # Retornamos a string invertida
    return texto_revertido

print(reverter_string(texto))

# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
k = [1, 2, 3, 4, 5]

def combinar_pares(lista_numero: list, numero: int) -> list:
    lista_pares: list = []  # Inicializa a lista onde os pares válidos serão armazenados
    # Loop externo para percorrer cada elemento da lista (posição i)
    for i in range(len(lista_numero)):
        # Loop interno começa a partir da próxima posição (j > i), evitando pares repetidos/invertidos
        for j in range(i + 1, len(lista_numero)):
            # Verifica se a soma dos elementos nas posições i e j é igual ao número fornecido
            if lista_numero[i] + lista_numero[j] == numero:
                # Se for, adiciona a tupla (par de valores) à lista de pares
                lista_pares.append((lista_numero[i], lista_numero[j]))
    # Retorna a lista com todos os pares encontrados
    return lista_pares

lista_numeros: list = [64.5, 34, 25, 12, 22, 11, 90]
numero = 47

print(combinar_pares(lista_numeros, numero))

# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
dicionario = {"banana": 3, "abacate": 5, "laranja": 2}

def lista_chaves_ordenadas(dicionario: dict) -> list:
    lista_chaves: list = dicionario.keys()
    lista_chaves_ordenadas: list = sorted(lista_chaves)
    return lista_chaves_ordenadas

print(lista_chaves_ordenadas(dicionario))

# Define uma função que recebe um dicionário e retorna ele com as chaves em ordem alfabética
def ordenar_dicionario(dicionario: dict) -> dict:
    # Obtém todas as chaves do dicionário original
    lista_chaves: list = dicionario.keys()
    # Ordena as chaves em ordem alfabética (ou crescente se forem números)
    lista_chaves_ordenadas: list = sorted(lista_chaves)
    # Cria um novo dicionário vazio para armazenar os itens ordenados
    dicionario_ordenado: dict = {}
    # Percorre a lista de chaves ordenadas
    for chave in lista_chaves_ordenadas:
        # Adiciona ao novo dicionário a chave e seu respectivo valor original
        dicionario_ordenado[chave] = dicionario[chave]
    # Retorna o novo dicionário com as chaves em ordem
    return dicionario_ordenado

print(ordenar_dicionario(dicionario))