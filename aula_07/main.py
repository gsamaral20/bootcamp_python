from etl import ler_csv, filtrar_produtos_nao_entregues, soma_valores_produtos

path_arquivo = "vendas.csv"

lista_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_produtos)
valor_produtos_entregues = soma_valores_produtos(produtos_entregues)
print(valor_produtos_entregues)