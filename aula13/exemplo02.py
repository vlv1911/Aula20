import pandas as pd
import polars as pl
from datetime import datetime #Biblioteca que trabalha com tempo


ENDERECO_DADOS = r'../dados/'

try:
    print('Obtendo dados....')

    inicio = datetime.now()

    lista_arquivo = ['202601_NovoBolsaFamilia.csv',
                     '202602_NovoBolsaFamilia.csv',
                     '202603_NovoBolsaFamilia.csv',
                     '202604_NovoBolsaFamilia.csv',
                     ]

    df_bolsa_familia = None

    for arquivo in lista_arquivo:
        print(f'\nProcessando o arquivo: {arquivo}')

        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')
        print(df.head())

        if df_bolsa_familia is None:
            df_bolsa_familia = df

        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])

        del df

    print(df_bolsa_familia.head())
    print(df_bolsa_familia.shape)

    final = datetime.now()

    print(f'Tempo de execução: {final - inicio}')


except Exception as e:
    print(f'Erro ao realizar a leitura dos meses: {e}')