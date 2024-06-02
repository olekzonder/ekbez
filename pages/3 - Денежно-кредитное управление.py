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

Денежная масса — наличные деньги и безналичные денежные средства резидентов Российской Федерации.

Наличные деньги в обращении (агрегат М0) - все банкноты и монеты в обращении

Переводные депозиты в рублях (агрегат М1 = М0 + переводные депозиты в рублях) - средства на расчетных, текущих и иных счетах до востребования (в том числе счетах для расчетов с использованием пластиковых карт) резидентов Российской Федерации (организаций и домашних хозяйств), открытых в банковской системе в валюте Российской Федерации

Денежная масса в национальном определении (М2 = М1 + другие депозиты в рублях) -   средства на счетах срочных депозитов и иные привлеченные на срок средства в валюте Российской Федерации, счетах в драгоценных металлах, а также все начисленные проценты по депозитным операциям резидентов Российской Федерации (организаций и домашних хозяйств) в банковской системе

"""        
outro = """

"""
def open_df(name,arg):
    df = pd.read_excel(name,index_col=0)
    fig = px.line(df, x=df.index, y=df.columns, title=arg)
    st.plotly_chart(fig,use_container_width=True)
def main():
    st.markdown(intro)
    st.image('База данных/Масса.png')
    col1,col2 = st.columns(2)
    with col1:
        open_df('База данных/Историческая динамика ДКУ.xlsx','Динамика показателей ДКУ')
    with col2:
        open_df('База данных/Удобство кредитования.xlsx','Кредитование')

main()