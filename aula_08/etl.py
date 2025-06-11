# Uma função de extract que lê e consolida os json
import pandas as pd
import os
import glob


def extrair_dados(pasta:str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# Uma função que transforma
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

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
    
def pipeline_calcular_kpi_de_vendas_consolidada(pasta: str, formato_saida: list):
    data_frame = extrair_dados(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_saida)
