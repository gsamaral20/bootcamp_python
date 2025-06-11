from etl import pipeline_calcular_kpi_de_vendas_consolidada

pasta: str = 'data'
formato: list = ['csv']

pipeline_calcular_kpi_de_vendas_consolidada(pasta, formato)