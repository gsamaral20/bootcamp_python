import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    """
    Função que lê um arquivo csv e retorna uma lista de dicionários
    """

    lista = []
    with open(nome_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    """
    Função que filtra produtos em que entrega = True
    """
    lista_produtos_filtrados: list = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_produtos_filtrados.append(produto)
    return lista_produtos_filtrados

def soma_valores_produtos(lista_produtos_filtrados: list[dict]) -> int:
    """
    Função que soma os valores dos produtos que estão na lista
    """
    valor_total: float = 0
    for produto in lista_produtos_filtrados:
        valor_total += float(produto.get("price"))
    return valor_total
