import streamlit as st
import pandas as pd
import numpy as np

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)


intro = """
### Часть 2 статьи 75 Конституции Российской Федерации

Защита и обеспечение устойчивости рубля –
основная функция Центрального банка Российской
Федерации, которую он осуществляет независимо
от других органов государственной власти.

### Статья 34.1 Федерального закона от 10.07.2002 № 86-ФЗ «О Центральном банке Российской Федерации (Банке России)»

Основной целью денежно-кредитной политики Банка
России является защита и обеспечение устойчивости
рубля посредством поддержания ценовой
стабильности, в том числе для формирования
условий сбалансированного и устойчивого
экономического роста.

### Цели и принципы денежно-кредитной политики

Основная цель денежно-кредитной политики (ДКП) ЦБ РФ - ценовая стабильность, достижение отметки годовой инфляции вблизи 4% г/г (инфляционное таргетирование).

Принципы денежно-кредитной политики Банка России:

- Установление постоянно действующей публичной количественной цели по инфляции

- Денежно-кредитная политика реализуется в условиях плавающего валютного курса - курс иностранной валюты к рублю определяется балансом спроса и предложения иностранной валюты на валютном рынке

- Основной инструмент денежно-кредитной политики - ключевая ставка

- Банк России принимает решения по денежно-кредитной политике на основе макроэкономического прогноза

- Открытость информации

### Почему цель по инфляции - 4% г/г?

Цель по инфляции "около 4%" годовых несколько выше, чем в странах с развитыми рыночными механизмами. В таких странах
цель по инфляции обычно устанавливается на уровне 1-3% г/г.

Банк России оценивал, что поддержание инфляции в РФ вблизи этих значений мерами ДКП затрудено из-за недостаточной
развитости рыночных механизмов и низкой диверсификации экономики. Кроме того, необходимо минимизировать риск возникновения
дефляции, что может повлечь за собой торможение экономики из-за раскручивания дефляционной спирали.
"""        
def main():
    st.markdown(intro)
    
main()