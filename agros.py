####Librerías
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
from PIL import Image

####Carga BD
#@st.cache(allow_output_mutation=True)
def load_data(): 
	data = pd.read_csv('base.csv', encoding = 'latin1')
	return data
df = load_data() 

####Sesión a resaltar
def header(url):
     st.markdown(f'<p style="background-color:#86e000;color:#fafcf5;font-size:42px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('                      W1 Bootcamp DS')
# st.title('W1 Bootcamp DS')

####Sección 1
def header(url):
     st.markdown(f'<p style="color:#86e000;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('Taller AGROS')
# st.header('Taller AGROS')

####Métricas
num_ins= len(df)
num_asi= len(df[df.ASISTENCIA=='SI'])
num_apl= len(df[df.PERFIL.notnull()]) 
num_sel= len(df[df.PERFIL=='Seleccionado']) 

# st.metric(label="Número de inscritos y variación vs evento anterior", value=int(df['ID'].count()), delta="10%")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Número de inscritos", value=num_ins, delta="10%")
col2.metric("Número de asistentes", value=num_asi, delta="3%")
col3.metric("Número de aplicantes", value=num_apl, delta="2%")
col4.metric("Número de seleccionados", value=num_sel, delta="5%")

####Imagen
image = Image.open('eventoagros.JPG')
st.image(image)

####Sección 2
def header(url):
     st.markdown(f'<p style="color:#86e000;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('Funnel de conversión')

y = ["Registrados", "Asistentes", "Aplicantes", "Seleccionados"]
x = [int(num_ins),int(num_asi),int(num_apl),int(num_sel)]

fig = px.funnel(df, x=x, y=y)
fig.show()
st.plotly_chart(fig)

####Sección 3
def header(url):
     st.markdown(f'<p style="color:#86e000;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('Participación en el evento')

df1= df[['ID','ASISTENCIA']].groupby(['ASISTENCIA'], as_index=False).aggregate({'ID':'count'})
asistencia = df1["ASISTENCIA"]
ctd = df1["ID"]
# plot the value
fig = px.pie(df1, values=ctd, names=asistencia, title='Porcentaje de asistencia (%)', hole=.3)    
st.plotly_chart(fig)

####Sección 4
st.header('¿Llegamos al público que quisiéramos?')

def header(url):
     st.markdown(f'<p style="color:#86e000;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('Organización a la que pertenecen los inscritos en el evento')

df3= df[['ID','ETIQUETA_ORGANIZACION']].groupby(['ETIQUETA_ORGANIZACION'], as_index=False).aggregate({'ID':'count'})
fig1 = px.bar(df3, x='ID', y='ETIQUETA_ORGANIZACION', orientation='h', labels={'ETIQUETA_ORGANIZACION':'Organización','ID':'Número de personas'})
fig1.update_layout(title_text='Número de personas inscritas de acuerdo a su organización')
st.plotly_chart(fig1)

def header(url):
     st.markdown(f'<p style="color:#86e000;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('Cargo que ocupan los inscritos en el evento')

df3= df[['ID','ETIQUETA_CARGO']].groupby(['ETIQUETA_CARGO'], as_index=False).aggregate({'ID':'count'})
fig1 = px.bar(df3, x='ID', y='ETIQUETA_CARGO', orientation='h', labels={'ETIQUETA_CARGO':'Cargo','ID':'Número de personas'})
fig1.update_layout(title_text='Número de personas inscritas de acuerdo a su cargo')
st.plotly_chart(fig1)

####Sección 5

def header(url):
     st.markdown(f'<p style="color:#86e000;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('Motivación de los inscritos en el evento')

cond_asistencia= st.multiselect('Seleccione de acuerdo a asistencia', df1["ASISTENCIA"])
df3 = df[(df['ASISTENCIA'].isin(cond_asistencia))]
df3= df3[['ID','ETIQUETA_MOTIVACION']].groupby(['ETIQUETA_MOTIVACION'], as_index=False).aggregate({'ID':'count'})
fig1 = px.bar(df3, x='ETIQUETA_MOTIVACION', y='ID',labels={'ETIQUETA_MOTIVACION':'Motivación','ID':'Número de personas'})
fig1.update_layout(title_text='Número de personas por motivación de inscripción')
st.plotly_chart(fig1)

####Sección 6

def header(url):
     st.markdown(f'<p style="color:#86e000;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('Canal de inscripción al evento')

st.header('¿Deberíamos impulsar un canal en particular?')

df4= df[['ID','ETIQUETA_CANAL','ASISTENCIA']].groupby(['ETIQUETA_CANAL','ASISTENCIA'], as_index=False).aggregate({'ID':'count'})
fig2 = px.bar(df4, x="ETIQUETA_CANAL", y="ID",
             color='ASISTENCIA', barmode='group', labels={'ETIQUETA_CANAL':'Canal','ID':'Número de personas'},
             height=400)
st.plotly_chart(fig2)

####Última sección

def header(url):
     st.markdown(f'<p style="color:#86e000;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
header('Alcance por zona geográfica de acuerdo a perfil')

df5 = df[df.DEPARTAMENTO.notnull()]
df6= df5[['ID','PERFIL']].groupby(['PERFIL'], as_index=False).aggregate({'ID':'count'})

cond_perfil= st.multiselect('Seleccione el perfil', df6["PERFIL"])

df7 = df5[(df['PERFIL'].isin(cond_perfil))]
df7 = df7[['ID','DEPARTAMENTO']].groupby(['DEPARTAMENTO'], as_index=False).aggregate({'ID':'count'})
fig1 = px.bar(df7, x='DEPARTAMENTO', y='ID',labels={'DEPARTAMENTO':'Departamento','ID':'Número de Aplicantes'})
fig1.update_layout(title_text='Número de aplicantes por zona geográfica')
st.plotly_chart(fig1)

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
   

