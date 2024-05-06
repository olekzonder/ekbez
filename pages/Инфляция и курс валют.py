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
st.set_page_config(page_title="ДКУ", layout="wide")
st.markdown(hide_st_style, unsafe_allow_html=True)

intro = """
## Определения
*Инфляция* - устойчивое повышение общего уровня цен на товары и услуги
"""        
outro = """
## Выводы
В период с 2017 по 2020 инфляция держалась на уровне около 4% г/г. В июле 2020 года Банком России было принято решение
по установлению минимального уровня ключевой ставки (4,25% г/г), и такой уровень сохранялся до 19 марта 2021 г. 
Под влиянием пандемии COVID-19 темпы инфляции начали возрастать, и Банком России было начато ужесточение денежно-кредитной политики.

На фоне беспрецедентных торговых ограничений 28 февраля 2022 г. Банком России было решено поднять ключевую ставку до 20% г/г. После некоторого послабления в 2023 году на 2024 год был взят курс на дальнейшее повышение ключевой ставки до 16% г/г.
"""
def open_df(name,arg):
    df = pd.read_excel(name,index_col=0)
    fig = px.line(df, x=df.index, y=df.columns, title=arg)
    st.plotly_chart(fig,use_container_width=True)
def main():
    st.markdown(intro)
    open_df('База данных/Инфляция.xlsx','Инфляция')
    open_df('База данных/Курс валют.xlsx','Курс валют')
    st.markdown(outro)
main()