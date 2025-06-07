import csv

# É mais leve que importar o pandas, é uma api nativa do python

# Caminho para o arquivo CSV
caminho_arquivo: str = "exemplo.csv"

# Inicializa uma lista vazia para armazenar os dados
arquivo_csv: list = []

# Usa o gerenciador de contexto `with` para abrir o arquivo
with open(file=caminho_arquivo, mode = "r", encoding = "utf-8") as arquivo:
    # Cria um objeto leitor de CSV
    leitor_csv = csv.DictReader(arquivo)

    # Cria um objeto leitor de CSV
    for linha in leitor_csv:
        # Adiciona cada linha (um dicionário) à lista de dados
        arquivo_csv.append(linha)

# Exibe os dados lidos do arquivo CSV
print(arquivo_csv)
