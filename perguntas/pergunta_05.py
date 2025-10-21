# Há deputados com glosas (valores recusados) significativamente altas (vlrGlosa)?
# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("perguntas/data/Ano-2024.csv", sep=';')

deputados = df[df['cpf'].notnull()]

glosas_deputados = deputados.groupby('txNomeParlamentar')['vlrGlosa'].sum()
glosas_deputados = glosas_deputados.sort_values(ascending=False)

maiores_glosas = glosas_deputados[glosas_deputados > glosas_deputados.quantile(0.95)]

plt.figure(dpi=600, figsize=(10, 10))
plt.title('5% dos Deputados com maiores glosas')
plt.barh(maiores_glosas.index, maiores_glosas.values)
plt.grid(True, axis='x', linestyle='--')
plt.show()