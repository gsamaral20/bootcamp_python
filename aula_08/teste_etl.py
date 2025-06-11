from etl import extrair_dados, calcular_kpi_de_total_de_vendas, carregar_dados

if __name__ == "__main__":
    pasta = 'data'
    df = extrair_dados(pasta)
    df_calculado = calcular_kpi_de_total_de_vendas(df)
    formato_saida = ["csv", "parquet"]
    carregar_dados(df_calculado, formato_saida)