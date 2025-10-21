#Comparação de gastos médios entre deputados. (plotbox)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("perguntas/data/Ano-2024.csv", sep=';')

df_deputados_valores = df[['txNomeParlamentar','cpf','vlrLiquido']]

df_deputados_valores = df_deputados_valores[
    df_deputados_valores['cpf'].notna() & (df_deputados_valores['cpf'].astype(str).str.strip() != "")
]


#Retirando valores nulos
df_deputados_valores = df_deputados_valores[df_deputados_valores['vlrLiquido'] > 0]


#Agrupando por deputado e somando os valores
gastos_medios = df_deputados_valores.groupby('txNomeParlamentar')['vlrLiquido'].mean().reset_index()


#Plotando grafico de boxplot
plt.figure(figsize=(8, 8))  # aumenta a altura
plt.boxplot(
    gastos_medios['vlrLiquido'],
    vert=True,
    patch_artist=True,
    boxprops=dict(facecolor='skyblue', color='navy'),
    flierprops=dict(marker='o', markerfacecolor='red', markersize=6, alpha=0.4)
)
plt.ylabel('Gasto médio (R$)')
plt.title('Comparação de Gastos Médios entre Deputados (2024)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Definindo os limites e intervalos do eixo Y
y_min = 0
y_max = gastos_medios['vlrLiquido'].max() + 500  # só pra garantir espaço no topo
plt.yticks(np.arange(y_min, y_max, 500))  # vai de 1000 em 1000

plt.tight_layout()
plt.show()
