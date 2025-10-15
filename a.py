# %%
import pandas as pd

df = pd.read_csv("data/Ano-2024.csv", sep=';')

# pd.Series(df['vlrGlosa'].unique()).sort_values()
df.groupby('txNomeParlamentar')['vlrGlosa'].sum().sort_values()