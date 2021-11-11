import streamlit as st
import pandas as pd

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

@st.cache(persist=True)
	def load_data():
		data = pd.read_csv('mushrooms.csv')
		label = LabelEncoder()
		for col in data.columns:
			data[col] = label.fit_transform(data[col])
	return data
   
asistencia = data['ASISTENCIA'].unique()
   
