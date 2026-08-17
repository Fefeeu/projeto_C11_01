# Projeto C11

Projeto da disciplina de Ciência de Dados (C11) do Inatel, que responde **10 perguntas** sobre um conjunto de dados público escolhido pelo grupo.

### Grupo

| Nome | Matrícula |
|---|---|
| Felipe Ferreira | 380 GES |
| Felipe Loschi | 601 GES |
| Maria Rita | 2019 GEC |

## 📊 Dados

O projeto utiliza dados abertos da Câmara dos Deputados, disponíveis em [dadosabertos.camara.leg.br](https://dadosabertos.camara.leg.br): especificamente as **Despesas pela Cota para Exercício da Atividade Parlamentar (CEAP)**, referentes ao ano de 2024 (`perguntas/data/Ano-2024.csv`).

## 🛠️ Tecnologias utilizadas

- **Python 3**
- [Pandas](https://pandas.pydata.org/) — leitura, limpeza e agregação dos dados
- [NumPy](https://numpy.org/) — cálculos numéricos e ajuste polinomial
- [Matplotlib](https://matplotlib.org/) e [Seaborn](https://seaborn.pydata.org/) — visualizações estáticas (boxplots, dispersão)
- [Plotly](https://plotly.com/python/) — visualização interativa (previsão de gastos)

## 📁 Estrutura do repositório

```
projeto_C11_01/
├── perguntas/
│   ├── data/
│   │   └── Ano-2024.csv          # base de despesas parlamentares (CEAP 2024)
│   ├── pergunta_01.py            # comparação de gastos médios entre deputados
│   ├── pergunta_02.py            # categorias de despesa mais frequentes
│   ├── pergunta_03.py            # 10 fornecedores com maiores valores totais
│   ├── pergunta_04.py            # média e desvio padrão por categoria
│   ├── pergunta_05.py            # deputados com glosas significativas
│   ├── pergunta_06.py            # deputados que mais gastaram por tipo de despesa
│   ├── pergunta_07.py            # gasto médio por parlamentar em cada partido
│   ├── pergunta_08.py            # variação de gastos ao longo dos meses por partido
│   ├── pergunta_09.py            # 10 deputados com gastos mais consistentes
│   └── pergunta_10.py            # previsão do gasto mensal da câmara
├── a.py                          # script auxiliar de exploração inicial dos dados
├── .gitignore
└── README.md
```

## ❓ Perguntas respondidas

1. Qual a comparação de gastos médios entre deputados?
2. Quais foram as categorias de despesa mais frequentes?
3. Quais os 10 fornecedores que receberam os maiores valores totais?
4. Qual o valor médio e o desvio padrão das despesas por categoria?
5. Há deputados com glosas (valores recusados) significativamente altas?
6. Quais deputados mais gastaram em cada tipo de despesa?
7. Qual é o gasto médio por parlamentar em cada partido?
8. Qual a variação de gastos ao longo dos meses para cada partido?
9. Quais são os 10 deputados que têm os gastos mais consistentes (menor variação)?
10. É possível prever o gasto mensal da câmara com base nos meses anteriores?

A última pergunta é respondida com um **ajuste polinomial de 2º grau** sobre o total de gastos mensais, usado para projetar o gasto do mês seguinte.

## ⚙️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Fefeeu/projeto_C11_01.git
   cd projeto_C11_01
   ```

2. Instale as dependências:
   ```bash
   pip install pandas numpy matplotlib seaborn plotly
   ```

3. Rode a pergunta desejada a partir da raiz do repositório (os scripts leem o CSV com caminho relativo a partir daqui):
   ```bash
   python perguntas/pergunta_01.py
   ```
