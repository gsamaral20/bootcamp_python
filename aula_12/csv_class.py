import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filtrar_por(self, coluna, atributo):
        return self.df[self.df[coluna]==atributo]
    
caminho_csv = './exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_csv = CsvProcessor(caminho_csv)
arquivo_csv.carregar_csv()
print(arquivo_csv.filtrar_por(filtro, limite))

