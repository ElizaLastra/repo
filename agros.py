import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

st.title('W1 Bootcamp DS')
st.header('Inscripción en el evento de AGROS')

# @st.cache
# def get_data():
#     return pd.read_csv('https://github.com/ElizaLastra/repo/blob/master/base.csv', encoding = 'latin1', error_bad_lines=False)

# df = get_data()  


# cond_asistencia = st.selectbox('Asistencia', asistencia)
# df[df['ASISTENCIA'] == cond_asistencia]

#df.groupby(['ASISTENCIA']).value_counts().plot(kind='pie', y='ID')
#df= pd.read_csv('https://github.com/ElizaLastra/repo/blob/master/base.csv', encoding = 'utf8')
#df.groupby(['ASISTENCIA']).count().plot(kind='pie', y='ID')

# @st.cache(allow_output_mutation=True)
@st.cache(allow_output_mutation=True)
def load_data():
	data = pd.read_csv('base.csv', encoding = 'latin1')
# 	label = LabelEncoder()
# 	for col in data.columns:
# 		data[col] = label.fit_transform(data[col])
	return data

df = load_data() 
df['Participante'] = 1

# df.groupby(['ASISTENCIA']).sum().plot(kind='pie', y='Participante')

# asistencia = df['ASISTENCIA']
# participantes = df['Participante']
# plt.pie(participantes, labels=asistencia)
# plt.title("Gold medal achievements of five most successful\n"+"countries in 2016 Summer Olympics")
# plt.show()

st.write("""### 1. Data overview""",df.head())
st.write("""### 2. Aplicación de filtros""")

asistencia = df['ASISTENCIA'].unique()
cond_asistencia = st.selectbox('Asistencia', asistencia)
df[df['ASISTENCIA'] == cond_asistencia]
   
