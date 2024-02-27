import streamlit as st

st.markdown("# Welcome to my Website!")
st.sidebar.markdown("# Main Page")

st.write("Click on a page to see racer or kart stats")

link = '[To my Github Pages Site](https://github.com/honedog/Github_assignment1_take2.git)'
st.markdown(link, unsafe_all_html=True)