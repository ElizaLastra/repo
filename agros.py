import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px

# @st.cache(allow_output_mutation=True)
@st.cache(allow_output_mutation=True)
def load_data():
	data = pd.read_csv('base.csv', encoding = 'latin1')
# 	label = LabelEncoder()
# 	for col in data.columns:
# 		data[col] = label.fit_transform(data[col])
	return data

df = load_data() 
# df['Participante'] = 1

st.title('W1 Bootcamp DS')
st.header('Inscripción en el evento de AGROS')
st.metric(label="Número de inscritos y variación vs evento anterior", value=int(df['ID'].count()), delta="10%")

st.header('Participación en el evento')

df1= df[['ID','ASISTENCIA']].groupby(['ASISTENCIA'], as_index=False).aggregate({'ID':'count'})
asistencia = df1["ASISTENCIA"]
ctd = df1["ID"]
# plot the value
fig = px.pie(df1, values=ctd, names=asistencia, title='Porcentaje de asistencia (%)', hole=.3)    
st.plotly_chart(fig)
# fig = px.pie(df, values='pop', names='country', title='Population of European continent')

st.header('Motivación de los inscritos en el evento')

cond_asistencia= st.multiselect('Seleccione de acuerdo a asistencia', df1["ASISTENCIA"])
# cond_asistencia = str(cond_asistencia)
# st.write(cond_asistencia)

df3 = df[(df['ASISTENCIA'].isin(cond_asistencia))]
df3= d3[['ID','ETIQUETA_MOTIVACION']].groupby(['ETIQUETA_MOTIVACION'], as_index=False).aggregate({'ID':'count'})
fig1 = px.bar(df3, x='ETIQUETA_MOTIVACION', y='ID',labels={'ETIQUETA_MOTIVACION':'Motivación','ID':'Número de personas'})
fig1.update_layout(title_text='Número de personas por motivación de inscripción')

st.plotly_chart(fig1)

st.write("""### 1. Data overview""",df.head())
st.write("""### 2. Aplicación de filtros""")

asistencia = df['ASISTENCIA'].unique()
cond_asistencia = st.selectbox('Asistencia', asistencia)
df[df['ASISTENCIA'] == cond_asistencia]

plt.rcParams.update(plt.rcParamsDefault)
plt.style.use('bmh')
fig3 = plt.figure(constrained_layout=True,figsize=(21,11))
gs = fig3.add_gridspec(40,40)

fig3.add_subplot(gs[0:19,0:20])
plt.hist(df['Participante'],range=(0,160),bins=16,alpha=0.8)
plt.ylabel('Frequency',fontsize=25)
plt.xlabel('Caps',fontsize=25)
plt.xticks(size=20)
plt.yticks(size=20)
st.pyplot(fig3)
   

