import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_karts = pd.read_csv('streamlit_template/data/kart_stats.csv')

df_karts = df_karts[['Body', 'Weight', 'Acceleration', 'On-Road traction', 'Mini-Turbo', 'Ground Speed']]

st.dataframe(df_karts.style
             .highlight_max(color='lightgreen',axis=0,subset=['Weight','Acceleration', 'On-Road traction', 'Mini-Turbo', 'Ground Speed'])
             .highlight_min(color='red',axis=0,subset=['Weight','Acceleration', 'On-Road traction', 'Mini-Turbo', 'Ground Speed'])
             )

st.line_chart(df_karts, x='Ground Speed', y=['Acceleration'])

df_first_5_karts = df_karts.iloc[0:5]

st.bar_chart(df_first_5_karts, x='Body', y=['Ground Speed','Acceleration','Weight','On-Road traction', 'Mini-Turbo'])

chosen_kart=st.selectbox('Pick a Kart',df_karts['Body'])

df_single_kart = df_karts.loc[df_karts['Body']==chosen_kart]

df_single_kart=df_single_kart.drop(columns=['Body'])

df_unp_karts = df_single_kart.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)

st.bar_chart(df_unp_karts, x='category', y='strength')