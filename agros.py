import streamlit as st
import pandas as pd

st.title('W1 Bootcamp DS')
st.header('Inscripción en el evento de AGROS')

df= pd.read_csv('base.csv', encoding = 'utf8')
#df.groupby(['ASISTENCIA']).count().plot(kind='pie', y='ID')
