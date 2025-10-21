#Quais foram as categorias de despesa mais frequentes?
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("perguntas/data/Ano-2024.csv", sep=';')

df_categorias = df["txtDescricao"].value_counts()

plt.figure(figsize=(10,6))
df_categorias.head(9).plot(kind='bar', color='cornflowerblue', edgecolor='black')
plt.title("Categorias de despesa mais frequentes")
plt.xlabel("Categoria")
plt.ylabel("Frequência")
plt.xticks(rotation=30, ha='right', fontsize=5,fontweight='bold')
plt.tight_layout()
plt.show()