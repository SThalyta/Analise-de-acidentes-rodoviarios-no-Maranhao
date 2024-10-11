# Análise de Acidentes Rodoviários no Maranhão (2007-2020)

Este projeto realiza uma análise detalhada dos acidentes ocorridos nas rodovias federais do Maranhão entre os anos de 2007 e 2020. Utilizando Python, o projeto envolve tratamento, limpeza e visualização de dados, com o objetivo de gerar insights sobre as causas e o impacto dos acidentes no estado.

O **dashboard interativo** permite que os usuários filtrem os dados por ano e município, visualizando informações como o número de mortos, feridos e as rodovias com mais acidentes fatais.

## 🛠️ Tecnologias Utilizadas

- **Pandas**: Para manipulação e limpeza de dados.
- **Streamlit**: Para construção do dashboard interativo.
- **Plotly**: Para visualização dos dados em gráficos interativos.
- **Jupyter Notebook**: Utilizado no tratamento inicial e limpeza dos dados.

## 📋 Pré-requisitos

Você vai precisar ter o Python 3.12.1 instalado na sua máquina. Além disso, certifique-se de que possui as seguintes bibliotecas instaladas:

- Pandas
- Streamlit
- Plotly

Se não tiver, você pode instalá-las utilizando o comando abaixo:

```bash
pip install pandas streamlit plotly
```

## 🚀 Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/SThalyta/Analise-de-acidentes-rodoviarios-no-Maranhao.git
   cd Analise-de-acidentes-rodoviarios-no-Maranhao
   ```

2. **Instale as dependências**:

   Você pode instalar todas as bibliotecas necessárias de uma vez usando o comando:

   ```bash
   pip install -r requirements.txt
   ```

3. **Adicione o arquivo de dados**:

   Certifique-se de que o arquivo de dados `acidentes2007-2020.csv` está presente na pasta do projeto. Este arquivo contém os dados brutos que serão utilizados para análise e visualização. Caso você deseje modificar ou realizar sua própria análise, esse é o link para a base de dados: https://www.kaggle.com/datasets/marcosfnlr/acidentes-em-rodovias-federais-20072020.

## ▶️ Como executar

1. **Executar o dashboard**:

   O dashboard interativo é construído no arquivo `dashboard.py`. Para rodar a aplicação, use o seguinte comando no terminal:

   ```bash
   streamlit run dashboard.py
   ```

   O Streamlit abrirá uma aba no navegador, onde você poderá interagir com o dashboard.

## 📊 Descrição do Projeto

### Tratamento e Limpeza dos Dados

O tratamento e limpeza de dados foram realizados em um **Jupyter Notebook**, onde os dados brutos foram carregados, tratados e preparados para serem visualizados. A base de dados utilizada foi encontrada no Kaggle: https://www.kaggle.com/datasets/marcosfnlr/acidentes-em-rodovias-federais-20072020 . As principais etapas incluem:

- **Carregamento dos dados**: O arquivo CSV `acidentes2007-2020.csv` foi importado para o pandas.
- **Tratamento de valores ausentes**: Colunas com valores ausentes foram identificadas e tratadas, seja removendo dados irrelevantes ou substituindo valores nulos.
- **Conversão de tipos**: Algumas colunas continham tipos de dados mistos, e o código converteu esses dados para garantir uma análise precisa.
- **Filtragem de dados**: Os dados foram filtrados por ano e município para facilitar a análise visual no dashboard.

### Visualização Interativa

O arquivo `dashboard.py` foi criado para oferecer uma interface de visualização interativa para o usuário. Através do **Streamlit** e **Plotly**, os dados são exibidos em gráficos dinâmicos e interativos.

- **Métricas gerais**: Total de acidentes e vítimas por ano e município.
- **Gráficos de barras**: Número de mortos por mês em diferentes contextos (estado ou município).
- **Gráficos de pizza**: Rodovias federais (BRs) com mais vítimas fatais por ano.

### Principais Gráficos

- **Número de mortos por ano**: Um gráfico de barras que mostra como o número de mortes variou ao longo dos anos.
- **Distribuição mensal dos acidentes**: Um gráfico de barras que exibe o número de mortos por mês.
- **Análise por rodovia**: Um gráfico de pizza para visualizar quais rodovias (BRs) possuem mais acidentes fatais.
