import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_excel('contagem_atendimentos.xlsx')
st.write(data)

chart_data = pd.DataFrame(
    np.random.randn(20, 8),
    columns=['Adami', 'Suzano', 'Klabin', 'Irani', 'RFR Guarulhos', 'RFR Indaiatuba', 'GKN', 'Coopercarga']
)

st.bar_chart(chart_data)
st.line_chart(chart_data)
