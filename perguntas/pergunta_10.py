#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

df = pd.read_csv('perguntas/data/Ano-2024.csv', sep=';')

#%%
#10. É possível prever o gasto mensal da câmara com base nos meses anteriores?
df_10 = df.copy()
df_10['datEmissao'] = pd.to_datetime(df_10['datEmissao'])
df_10['mesEmissao'] = df_10['datEmissao'].dt.month
df_mesParlamentar = df_10.groupby('mesEmissao')['vlrLiquido'].sum().reset_index()
#%%
x = df_mesParlamentar['mesEmissao'].values
y = df_mesParlamentar['vlrLiquido'].values
#%%
dados = pd.DataFrame({
    'Mes': x,
    'Valor': y
})

plt.figure(figsize=(10, 6))
sns.scatterplot(data=dados, x='Mes', y='Valor', s=100)
plt.title(f'Valores por Mês - Deputados')
plt.xlabel('Mês')
plt.ylabel('Valor')
plt.xticks(range(1, 13), ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
                          'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.grid(True, alpha=0.3)
plt.show()

def ajuste_polinomial(x, y, grau):
    coef = np.polyfit(x, y, grau)
    p = np.poly1d(coef)
    return p

# Função para plotar o ajuste
def plot_ajuste(x, y, p, titulo="Ajuste Polinomial"):
    xp = np.linspace(min(x), max(x), 100)
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="red", label="Dados experimentais")
    plt.plot(xp, p(xp), color="blue", label=f"Ajuste (grau {p.order})")
    plt.title(titulo)
    plt.xlabel("Mês")
    plt.ylabel("Gasto (R$)")
    plt.xticks(range(1, 13), ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
                               'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

ajuste = ajuste_polinomial(x, y, 2)

plot_ajuste(x, y, ajuste, "Ajuste 2° grau")

x_previsao = 13
y_previsao = ajuste(13)
fig = go.Figure()

xp = np.linspace(1, 12, 100)
yp = ajuste(xp)

# Adicionando pontos dos dados reais
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='markers',
    name='Gastos Reais',
    marker=dict(size=12, color='red', symbol='circle'),
    hovertemplate='<b>Mês:</b> %{text}<br><b>Gasto:</b> R$ %{y:,.2f}<extra></extra>',
    text=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
          'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
))

# Adicionando o ajuste
fig.add_trace(go.Scatter(
    x=xp,
    y=yp,
    mode='lines',
    name='Ajuste Polinomial (grau 2)',
    line=dict(color='blue', width=2),
    hovertemplate='<b>Ajuste:</b> R$ %{y:,.2f}<extra></extra>'
))

# Adicionar ponto de previsão
fig.add_trace(go.Scatter(
    x=[x_previsao],
    y=[y_previsao],
    mode='markers',
    name='Previsão (próximo mês)',
    marker=dict(size=15, color='gold', symbol='star'),
    hovertemplate='<b>Previsão para Jan/2025:</b><br>R$ %{y:,.2f}<extra></extra>'
))

# Configurar layout
fig.update_layout(
    title='Previsão de Gastos Mensais - Câmara dos Deputados',
    xaxis_title='Mês',
    yaxis_title='Gasto (R$)',
    hovermode='closest',
    showlegend=True,
    xaxis=dict(
        tickmode='array',
        tickvals=list(range(1, 14)),
        ticktext=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
                  'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Jan/25']
    ),
    template='plotly_white',
    width=1000,
    height=600
)

fig.show()

# Imprimir a previsão
print(f"Previsão para o próximo mês: R$ {y_previsao:,.2f}")
# %%
