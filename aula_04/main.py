idade = 30

altura = 1.75
nome = "Alice"
is_estudante = True

#Tipagem - type hint - boa prática 
idade: int = 30
altura: float = 1.75
nome: str = "Alice"
is_estudante: bool = True

produto_01: dict = {
    "nome": "Sapato",
    "quantidade": 10,
    "preço": 9.98,
    "disponibilidade": True
}

produto_02: dict = {
    "nome": "Camiseta",
    "quantidade": 2,
    "preço": 39.98,
    "disponibilidade": False
}

carrinho: list = []
carrinho.append(produto_01)
carrinho.append(produto_02)
print(carrinho)

import json
carrinho_json = json.dumps(carrinho)
print(carrinho_json)