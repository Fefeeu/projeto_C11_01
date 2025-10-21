# Variação de gastos ao longo dos meses para cada partido.
# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("perguntas/data/Ano-2024.csv", sep=';')

gasto_mes_partidos = df.groupby(['sgPartido', 'numMes'])['vlrLiquido'].sum()
gasto_mes_partidos = gasto_mes_partidos/1000000
gasto_mes_partidos = gasto_mes_partidos.unstack(level=0).fillna(0)

# Adicione o parâmetro colormap='nipy_spectral'
ax = gasto_mes_partidos.plot(kind='line', figsize=(12, 7), colormap='nipy_spectral')

# ----- O resto do seu código fica igual -----
plt.title("Gasto por Partido ao longo dos Meses em Milhões de R$", fontsize=16)
plt.xlabel("Mês")
plt.ylabel("Valor Líquido Gasto")
plt.legend(title='Partidos', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()
