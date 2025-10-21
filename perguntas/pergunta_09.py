#%%
import pandas as pd
df = pd.read_csv('perguntas/data/Ano-2024.csv', sep=';', encoding='utf-8')
#%%
#9. Quais deputados têm os gastos mais consistentes? (menor variacao)

df_9 = df.copy()
df_9['datEmissao'] = pd.to_datetime(df_9['datEmissao'])
df_9['mesEmissao'] = df_9['datEmissao'].dt.month
df_mesPorParlamentar = df_9.pivot_table(index='txNomeParlamentar', columns='mesEmissao', values='vlrLiquido', aggfunc='sum', fill_value=0).reset_index()
df_mesPorParlamentar.columns = ['txNomeParlamentar'] + [f'gastos{mes}' for mes in 
    ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 
     'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']]
colunas_meses = ['gastosJaneiro', 'gastosFevereiro', 'gastosMarco', 'gastosAbril', 'gastosMaio', 'gastosJunho', 'gastosJulho', 'gastosAgosto', 'gastosSetembro', 'gastosOutubro', 'gastosNovembro', 'gastosDezembro']
df_mesPorParlamentar['DesvPadrao'] = df_mesPorParlamentar[colunas_meses].std(axis=1)
df_mesPorParlamentar['GastoTotal'] = df_mesPorParlamentar[colunas_meses].sum(axis=1)
primeiro_quartil = df_mesPorParlamentar['GastoTotal'].quantile(0.25)
df_mesPorParlamentarFiltrado = df_mesPorParlamentar[df_mesPorParlamentar['GastoTotal']>primeiro_quartil]
df_mesPorParlamentarFiltrado = df_mesPorParlamentarFiltrado.sort_values('DesvPadrao', ascending=True)[:10]
df_mesPorParlamentarFiltrado.to_excel('perguntas/data/MesPorParlamentar.xlsx')
# %%
