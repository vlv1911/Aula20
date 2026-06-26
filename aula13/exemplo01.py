# pip install polars

import pandas as pd

# Polars é uma biblioteca que trabalha com multhread. Por isso, é recomendada para trabalhos em larga escala.
# A tendência é que seja bam mais rápida que o Pandas, pois o processamento de dados é feito em paralelo.
# http://polars.rs

import polars as pl

from datetime import datetime # biblioteca que trabalha com tempo

# https://portaldatransparencia.gov.br/download-de-dados/novo-bolsa-familia

# lendo Bolsa Familia

try:
    ENDERECO_DADOS = r'../dados/'

    hora_inicial = datetime.now()
    print('Carregando...')
    
    # Pandas = 0:00:19.309986
    # df_janeiro = pd.read_csv(ENDERECO_DADOS + '202601_NovoBolsaFamilia.csv', sep=';', encoding='iso-8859-1')

    # Polars = 0:00:05.971729
    df_janeiro = pl.read_csv(ENDERECO_DADOS + '202601_NovoBolsaFamilia.csv', separator=';', encoding='iso-8859-1')

    print(df_janeiro.head())
    print(df_janeiro.columns)
    print(df_janeiro.shape) # Quantidade de linhas e colunas

    hora_final = datetime.now()

    print(f'Tempo de execução: {hora_final - hora_inicial}')



except Exception as e:
    print(f'Erro ao processar as informações: {e}')