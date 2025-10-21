# %%
import pandas as pd

df = pd.read_csv("perguntas/data/Ano-2024.csv", sep=';')

# pd.Series(df['vlrGlosa'].unique()).sort_values()
df.columns