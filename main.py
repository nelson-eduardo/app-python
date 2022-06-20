# Importacao das princnipais bibliotecas

from email import header
from turtle import color
from click import style
import streamlit as st
import pandas as pd
# criacao de container
    # para os quatros campos que teremos 
header = st.container()
dataset = st.container()
feature = st.container()
model_training = st.container()

st.markdown(
""""
<style>
    .main{
       
    }
</style>

""",
unsafe_allow_html = True

)



with header:
    st.title("APlicacao sobre os dados de eleicao geral em Angola 2022")
    st.text("Neste projecto,desenvolvo um projecto de python com a platoforma Streamlit...")

with dataset:
    st.header("Os recurrso de dados para esta analise foram tiradas")
    st.text("Uma base de dados bem estruturado, tirado da plataforma nelson domingos Eduardo")
    df = pd.read_csv('data/2015_Street_Tree_Census_Data.csv')
    st.write(df.head(5))
    st.subheader('Legenda para onosso grafico...!')

    sel_col, disp_col = st.columns(2)
    max1 = sel_col.slider("Qual seria o valor para a profundidade", min_value= 0, max_value= 100, step=1, value=0)
    teste = pd.DataFrame(df['block_id'].value_counts()).head(max1)
    st.bar_chart(teste)

with feature:
    st.header("APlicacao sobre os dados de eleicao geral em Angola 2022")
    st.text("Neste projecto,desenvolvo um projecto de python com a platoforma Streamlit...")

with model_training:
    st.header("APlicacao sobre os dados de eleicao geral em Angola 2022")
    # st.button("botao para download")
    # st.camera_input("Sorrir! Estas a ser filmado!")
    st.text("Neste projecto,desenvolvo um projecto de python com a platoforma Streamlit...")


# Novos testes
sel_col1, disp_col = st.columns(2)
# max_diph = sel_col.slider("Qual seria o valor para a profundidade", min_value= 10, max_value= 100, step=1, value=0)

bloco_selecao = sel_col.selectbox("Seleciona uma das opcoes",["Homem", "Mulher", "Nenhum"])
entrada = st.text_input("Digita qualquer coisa", 'categorias')

# st.write(max_diph)
st.write(bloco_selecao)