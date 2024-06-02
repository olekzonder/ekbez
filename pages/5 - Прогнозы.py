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
st.set_page_config(page_title="Прогнозы", layout="wide")
st.markdown(hide_st_style, unsafe_allow_html=True)

intro = """
### Основные направления государственной денежно-кредитной политики на 2023 и период 2024 и 2025 годов

При разработке денежно-кредитной политкии Банк России учитывает различные факторы, которые могут повлиять на её
реализацию и поэтому, как правило, формирует три сценария возможного развития действий:

- Базовый (сохраняются все мировые экономические тренды)

- Ускоренная адаптация (поставленные цели и стабилизация экономики будут достигнуты раньше примерно на год по сравнению с базовым сценарием)

- Глобальный кризис (усиление фрагментации в мировой экономике)
""" 

st.markdown(intro)
st.image('База данных/Прогноз.png')