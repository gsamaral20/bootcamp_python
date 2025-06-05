#Exercícios de Listas e Dicionários
# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
lista_numeros: list = []

for i in range(1,11):
    lista_numeros.append(i)

for numero in lista_numeros:
    quadrado: int = numero**2
    print(quadrado)


# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista: list = ["Python", "Java", "C++", "JavaScript"]
lista.remove("C++")
lista.append("Ruby")
print(lista)


# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
from typing import Dict, Any
livros: Dict[str, Any] = {
    "Título": "1984",
    "Autor": "George Orwell",
    "Ano": 1949
}

lista_elementos: list = livros.items()

for elementos in lista_elementos:
    print(elementos)

# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
dict_palavras: dict = {}
string = "Atirei o pau no gato, mas o gato não morreu"
#lista_string = string.split()

for palavra in string: #lista_string:
    if palavra.lower() in dict_palavras:
        dict_palavras[palavra.lower()] += 1
    else:
        dict_palavras[palavra.lower()] = 1
print(dict_palavras)

#Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
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