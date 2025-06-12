# Uma função de extract que lê e consolida os json
import pandas as pd
import os
import glob
from utils_log import log_decorator

# Este script segue a estrutura ETL (Extract, Transform, Load) com funções separadas para cada etapa.
# Todas as funções estão decoradas com o @log_decorator, que serve para registrar automaticamente
# informações úteis de execução (como início, fim, duração ou erros) sem precisar repetir código de logging em cada função.
# Isso facilita o rastreio da execução e a depuração, especialmente em pipelines de dados.


@log_decorator
def extrair_dados(pasta:str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

@log_decorator
# Uma função que transforma
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

@log_decorator
# Uma função que da load em csv ou parquet
def carregar_dados(df: pd.DataFrame, formato_saida: list):
    """
    parametro que vai ser csv ou parquet ou os dois
    """
    for formato in formato_saida:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet", index=False)

@log_decorator
def pipeline_calcular_kpi_de_vendas_consolidada(pasta: str, formato_saida: list):
    data_frame = extrair_dados(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_saida)