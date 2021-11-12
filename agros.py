import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
from PIL import Image

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

def header(url):
     st.markdown(f'<p style="background-color:#86e000;color:#fafcf5;font-size:42px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('                      W1 Bootcamp DS')

# st.title('W1 Bootcamp DS')

def header(url):
     st.markdown(f'<p style="color:#86e000;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('Taller AGROS')

# st.header('Taller AGROS')

st.metric(label="Número de inscritos y variación vs evento anterior", value=int(df['ID'].count()), delta="10%")

image = Image.open('eventoagros.JPG')
st.image(image)

def header(url):
     st.markdown(f'<p style="color:#86e000;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('Participación en el evento')

# st.header('Participación en el evento')

df1= df[['ID','ASISTENCIA']].groupby(['ASISTENCIA'], as_index=False).aggregate({'ID':'count'})
asistencia = df1["ASISTENCIA"]
ctd = df1["ID"]
# plot the value
fig = px.pie(df1, values=ctd, names=asistencia, title='Porcentaje de asistencia (%)', hole=.3)    
st.plotly_chart(fig)
# fig = px.pie(df, values='pop', names='country', title='Population of European continent')

st.header('¿Llegamos al público que quisiéramos?')

def header(url):
     st.markdown(f'<p style="color:#86e000;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('Organización a la que pertenecen los inscritos en el evento')

# st.header('Organización a la que pertenecen los inscritos en el evento')

df3= df[['ID','ETIQUETA_ORGANIZACION']].groupby(['ETIQUETA_ORGANIZACION'], as_index=False).aggregate({'ID':'count'})
fig1 = px.bar(df3, x='ID', y='ETIQUETA_ORGANIZACION', orientation='h', labels={'ETIQUETA_ORGANIZACION':'Organización','ID':'Número de personas'})
fig1.update_layout(title_text='Número de personas inscritas de acuerdo a su organización')
st.plotly_chart(fig1)

def header(url):
     st.markdown(f'<p style="color:#86e000;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('Cargo que ocupan los inscritos en el evento')

# st.header('Cargo que ocupan los inscritos en el evento')

df3= df[['ID','ETIQUETA_CARGO']].groupby(['ETIQUETA_CARGO'], as_index=False).aggregate({'ID':'count'})
fig1 = px.bar(df3, x='ID', y='ETIQUETA_CARGO', orientation='h', labels={'ETIQUETA_CARGO':'Cargo','ID':'Número de personas'})
fig1.update_layout(title_text='Número de personas inscritas de acuerdo a su cargo')
st.plotly_chart(fig1)

def header(url):
     st.markdown(f'<p style="color:#86e000;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('Motivación de los inscritos en el evento')

# st.header('Motivación de los inscritos en el evento')

cond_asistencia= st.multiselect('Seleccione de acuerdo a asistencia', df1["ASISTENCIA"])
df3 = df[(df['ASISTENCIA'].isin(cond_asistencia))]
df3= df3[['ID','ETIQUETA_MOTIVACION']].groupby(['ETIQUETA_MOTIVACION'], as_index=False).aggregate({'ID':'count'})
fig1 = px.bar(df3, x='ETIQUETA_MOTIVACION', y='ID',labels={'ETIQUETA_MOTIVACION':'Motivación','ID':'Número de personas'})
fig1.update_layout(title_text='Número de personas por motivación de inscripción')
st.plotly_chart(fig1)

def header(url):
     st.markdown(f'<p style="color:#86e000;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('Canal de inscripción al evento')

# st.header('Canal de inscripción al evento')

st.header('¿Deberíamos impulsar un canal en particular?')

df4= df[['ID','ETIQUETA_CANAL','ASISTENCIA']].groupby(['ETIQUETA_CANAL','ASISTENCIA'], as_index=False).aggregate({'ID':'count'})
fig2 = px.bar(df4, x="ETIQUETA_CANAL", y="ID",
             color='ASISTENCIA', barmode='group', labels={'ETIQUETA_CANAL':'Canal','ID':'Número de personas'},
             height=400)
st.plotly_chart(fig2)

# st.write("""### 1. Data overview""",df.head())
# st.write("""### 2. Aplicación de filtros""") ##

# asistencia = df['ASISTENCIA'].unique()
# cond_asistencia = st.selectbox('Asistencia', asistencia)
# df[df['ASISTENCIA'] == cond_asistencia]

# plt.rcParams.update(plt.rcParamsDefault)
# plt.style.use('bmh')
# fig3 = plt.figure(constrained_layout=True,figsize=(21,11))
# gs = fig3.add_gridspec(40,40)

# fig3.add_subplot(gs[0:19,0:20])
# plt.hist(df['Participante'],range=(0,160),bins=16,alpha=0.8)
# plt.ylabel('Frequency',fontsize=25)
# plt.xlabel('Caps',fontsize=25)
# plt.xticks(size=20)
# plt.yticks(size=20)
# st.pyplot(fig3)
   

