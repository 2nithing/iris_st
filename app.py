import plotly.express as px
import pandas as pd
import streamlit as st
import numpy as np

st.header('Plotly')

df = pd.read_csv('mentornow/timesData.csv')

df['income'] = df['income'].replace('-', np.nan).astype(float)
with st.expander('see data'):
    st.write(df)
with st.sidebar:
    options = st.multiselect('Select columns to plot',['teaching', 'research', 'citations', 'income', 'student_staff_ratio',])
    xaxis = st.selectbox('select xaxis', ['world_rank','university_name','country'])
    year = st.select_slider('select year', options = np.arange(2011,2017))

fig = fig = px.line(df.iloc[:100],x=xaxis,y=options)
st.plotly_chart(fig)

top3 = df[df['year']==year].iloc[:3]
fig = px.bar(top3, x='university_name', y=['citations', 'teaching'], barmode='group')
st.plotly_chart(fig)