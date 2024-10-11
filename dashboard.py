import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide") #arrumando o layout para ocupar toda a página
st.title("Análise dos acidentes rodoviários no Maranhão de 2007-2020")

df = pd.read_csv("dados_ma.csv")
df = df.sort_values(by = ["ano", "municipio"], ascending = True)
ano = st.sidebar.selectbox("Ano", df["ano"].unique())
municipio = st.sidebar.selectbox("Município", df["municipio"].unique())

df_filtro_ano = df[df.ano == ano]
df_filtro_municipio = df[(df.municipio == municipio) & (df.ano == ano)]

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

col1.metric(label="Total de acidentes", value= df.shape[0])
col2.metric(label=f"Total de acidentes {ano}", value=df_filtro_ano.shape[0])

fig = px.bar(df, x= "ano", y= "mortos", title = "Mortos por ano no Estado")
st.plotly_chart(fig)

fig_ano = px.bar(df_filtro_ano, x = "mes", y = "mortos",
                title = f"Número de mortos por mês por acidente rodoviário no Maranhão em {ano}",
                color = "mortos",
                labels={'mes': 'meses', 'mortos': 'Nº de mortos'})
fig_ano.update_xaxes(tickvals=list(range(1, 13)),
                      ticktext=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"])
fig_ano.update_layout(xaxis=dict(tickangle=-30))
col1.plotly_chart(fig_ano)

fig_municipio = px.bar(df_filtro_municipio, x = "mes", y = "mortos",
                       title = f"Número de mortos por mês em {ano} no município de {municipio}",
                       labels={'mes': 'meses', 'mortos': 'Nº de mortos'})
fig_municipio.update_xaxes(tickvals=list(range(1, 13)),
                            ticktext=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"])
fig_municipio.update_layout(xaxis=dict(tickangle=-30))
col2.plotly_chart(fig_municipio)

fig_br = px.pie(df_filtro_ano, values= "mortos", names= "br", 
                title= f"Qual a BR com mais vítimas fatais no Estado em {ano}?")
fig_br.update_traces(textposition='inside', textinfo='percent+label')
col3.plotly_chart(fig_br)

fig_br_municipio = px.pie(df_filtro_municipio, values= "mortos", names= "br", 
                title= f"Qual a BR com mais vítimas fatais em {municipio} em {ano}?")
fig_br_municipio.update_traces(textposition='inside', textinfo='percent+label')
col4.plotly_chart(fig_br_municipio)
