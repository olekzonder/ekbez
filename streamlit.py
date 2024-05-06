import streamlit as st
from st_pages import Page, show_pages, add_page_title
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)

intro = """
Студент 4 курса направления 10.05.04 "Информационно-аналитические системы безопасности"

Смирнов Александр Игоревич
"""

st.header("Экономика Российской Федерации: Денежно-кредитная политика Центрального Банка РФ")
st.markdown(intro)
show_pages([
Page("pages/Введение.py", "Введение"),
Page("pages/Инфляция и курс валют.py", "Инфляция и курс валют"),
Page("pages/Денежно-кредитное управление.py", "Денежно-кредитное управление"),
Page("pages/Процентный коридор.py", "Процентный коридор"),
Page("pages/Прогнозы.py", "Прогноз"),
Page("pages/Баланс Банка России.py", "Баланс Банка России"),
])

