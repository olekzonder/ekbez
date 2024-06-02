import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
                [data-testid="stSidebar"]{
                min-width: 200px;
                max-width: 400px;
            }
            </style>
            """
st.set_page_config(page_title="Процентный коридор", layout="wide")
st.markdown(hide_st_style, unsafe_allow_html=True)

intro = """
## Определения

*RUONIA (Ruble Overnight Index Average)* -  взвешенная процентная ставка однодневных межбанковских кредитов (депозитов) в рублях, отражающая оценку стоимости необеспеченного заимствования на условиях овернайт (ставка на 1 рабочий день)

*MIACR (Moscow InterBank Actual Credit Rate)* - это средневзвешенная фактическая ставка по кредитам, которые предоставляются московскими банками.

"""        
def open_df(name,arg):
    df = pd.read_excel(name,index_col=0)
    fig = px.line(df, x=df.index, y=df.columns, title=arg)
    st.plotly_chart(fig,use_container_width=True)
def main():
    st.markdown(intro)
    open_df('База данных/Процентный коридор.xlsx','Процентный коридор')
main()