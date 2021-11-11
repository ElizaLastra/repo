import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

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

st.title('W1 Bootcamp DS')
st.header('Inscripción en el evento de AGROS')
st.metric(label="Número de inscritos y variación vs evento anterior", value=int(df['ID'].count()), delta="10%")

def pieChart():
    df1= df.groupby(['ASISTENCIA'])['ID'].count()
    asistencia = df1['ASISTENCIA']
    ctd = df1['ID']
    fig = plt.figure()
    plt.pie(ctd, labels = asistencia)
    st.balloons()	
    st.pyplot(fig)

# @st.cache
# def get_data():
#     return pd.read_csv('https://github.com/ElizaLastra/repo/blob/master/base.csv', encoding = 'latin1', error_bad_lines=False)

# df = get_data()  


# cond_asistencia = st.selectbox('Asistencia', asistencia)
# df[df['ASISTENCIA'] == cond_asistencia]

#df.groupby(['ASISTENCIA']).value_counts().plot(kind='pie', y='ID')
#df= pd.read_csv('https://github.com/ElizaLastra/repo/blob/master/base.csv', encoding = 'utf8')
#df.groupby(['ASISTENCIA']).count().plot(kind='pie', y='ID')

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
   
# df1= df.groupby(['ASISTENCIA'])['ID'].count()
# asistencia = df1['ASISTENCIA']
# ctd = df1['ID']
# fig = plt.figure()
# plt.pie(ctd, labels= asistencia, autopct='%1.1f%%')
# plt.title("Porcentaje de participación en el evento")
# # plt.show()
# st.plotly_chart(fig)


