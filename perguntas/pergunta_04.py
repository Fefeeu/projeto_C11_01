#%%
import pandas as pd

df = pd.read_csv('perguntas/data/Ano-2024.csv', sep=';', encoding='utf-8')
#%%
#4. Qual o valor médio e o desvio padrão das despesas por categoria (txtDescricao)?
df_porCategoria = df.groupby('txtDescricao')['vlrLiquido'].sum().reset_index(name='Soma(R$)')
df_porCategoria['Média(R$)'] = df.groupby('txtDescricao')['vlrLiquido'].mean().values
df_porCategoria['Desvio Padrão(R$)'] = df.groupby('txtDescricao')['vlrLiquido'].std().values
df_porCategoria = df_porCategoria.sort_values('Soma(R$)', ascending=False)
df_porCategoria['Soma(R$)'] = df_porCategoria['Soma(R$)'].apply(lambda x: f"{x:,.2f}")
df_porCategoria['Média(R$)'] = df_porCategoria['Média(R$)'].apply(lambda x: f"{x:,.2f}")
df_porCategoria['Desvio Padrão(R$)'] = df_porCategoria['Desvio Padrão(R$)'].apply(lambda x: f"{x:,.2f}")
print(df_porCategoria)

# %%
