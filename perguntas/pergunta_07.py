# Qual é o gasto médio por parlamentar em cada partido?
# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/Ano-2024.csv", sep=';')

partidos = df[df['sgPartido'].notnull()].groupby('sgPartido')

df_partidos = pd.DataFrame()
df_partidos['vlrLiquido'] = partidos['vlrLiquido'].sum()
df_partidos['qtdParlamentar'] = partidos['txNomeParlamentar'].unique()
df_partidos['qtdParlamentar'] = df_partidos['qtdParlamentar'].apply(len)
df_partidos['vlrPorParlamentar'] = (df_partidos['vlrLiquido']/df_partidos['qtdParlamentar'])/1000
df_partidos['vlrPorParlamentar'] = round(df_partidos['vlrPorParlamentar'], 2)
df_partidos = df_partidos.sort_values('vlrPorParlamentar')
df_partidos['txQtdParlamentar'] = df_partidos.index.astype(str) + ' ' + df_partidos['qtdParlamentar'].astype(str).str.zfill(3)

plt.figure(dpi=400)
plt.title("Gasto médio por parlamentar em cada partido")
plt.barh(df_partidos['txQtdParlamentar'], 
         df_partidos['vlrPorParlamentar'], 
         label='Gastos em Milhares')
plt.grid(True, axis='x', linestyle='--')
plt.legend()
plt.show()