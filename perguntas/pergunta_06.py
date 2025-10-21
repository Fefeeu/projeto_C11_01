import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("perguntas/data/Ano-2024.csv", sep=';')

df_deputadosValidos = df[['txNomeParlamentar', 'cpf', 'vlrLiquido', 'txtDescricao']]
df_deputadosValidos = df_deputadosValidos[
    df_deputadosValidos['cpf'].notna() &
    (df_deputadosValidos['cpf'].astype(str).str.strip() != "") &
    (df_deputadosValidos['vlrLiquido'] > 0)
]

gastos = (
    df_deputadosValidos.groupby(['txtDescricao', 'txNomeParlamentar'])['vlrLiquido']
    .sum()
    .reset_index()
)

total_gastos_deputado = gastos.groupby('txNomeParlamentar')['vlrLiquido'].sum().sort_values(ascending=False)


top_200_deputados = total_gastos_deputado.head(200).index

gastos_filtrados = gastos[gastos['txNomeParlamentar'].isin(top_200_deputados)]

os.makedirs("graficos_pergunta_06", exist_ok=True)

for tipo in gastos_filtrados['txtDescricao'].unique():
    df_tipo = gastos_filtrados[gastos_filtrados['txtDescricao'] == tipo]

    df_tipo = df_tipo[df_tipo['vlrLiquido'] > 0]

    top = df_tipo.nlargest(20, 'vlrLiquido')
    outros = df_tipo['vlrLiquido'].sum() - top['vlrLiquido'].sum()

    labels = top['txNomeParlamentar'].tolist() + ['Outros']
    valores = top['vlrLiquido'].tolist() + [outros]

    fig, ax = plt.subplots(figsize=(15,12)) 

    wedges, texts, autotexts = ax.pie(
        valores,
        autopct='%1.1f%%',
        startangle=90,
        colors=plt.cm.tab20.colors,
        textprops={'fontsize': 10},
        pctdistance=0.7
    )

    for autotext in autotexts:
        autotext.set_fontsize(9)
        

    ax.set_title(f"Deputados que mais gastaram em: {tipo}", fontsize=14, weight='bold', pad=20)

    legenda_labels = [f"{i+1}. {dep} — R$ {val:,.2f}" for i, (dep, val) in enumerate(zip(top['txNomeParlamentar'], top['vlrLiquido']))]
    legenda_labels.append(f"Outros — R$ {outros:,.2f}")

    plt.legend(
        wedges,
        legenda_labels,
        title="Deputados",
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        fontsize=9
    )

    plt.tight_layout()
    nome_arquivo = tipo.replace('/', '_').replace(':', '_').replace(' ', '_')
    plt.savefig(f"graficos_pergunta_06/{nome_arquivo}.png", dpi=300, bbox_inches='tight')
    plt.close()
