#%%
import pandas as pd

df = pd.read_csv('perguntas/data/Ano-2024.csv', sep=';', encoding='utf-8')
# %%
#3. Quais os 10 fornecedores que receberam os maiores valores totais?
df_porFornecedor = df.groupby('txtFornecedor')['vlrLiquido'].sum().reset_index()
df_porFornecedor['txtDescricao'] = df.groupby('txtFornecedor')['txtDescricao'].first().values
df_porFornecedor = df_porFornecedor.sort_values('vlrLiquido',ascending=False)
print(df_porFornecedor.head(10))

# %%
