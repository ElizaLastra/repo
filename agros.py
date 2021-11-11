import streamlit as st
import pandas as pd

st.title('W1 Bootcamp DS')
st.header('Inscripción en el evento de AGROS')

@st.cache
def get_data():
    return pd.read_csv('https://github.com/ElizaLastra/repo/blob/master/base.csv')
  
#df= pd.read_csv('https://github.com/ElizaLastra/repo/blob/master/base.csv', encoding = 'utf8')
#df.groupby(['ASISTENCIA']).count().plot(kind='pie', y='ID')
