import streamlit as st

name = st.text_input("Enter Your Name : ")
fname = st.text_input("Enter Your Father Name : ")
adr = st.text_area("Enter Your Text : ")
classdate = st.selectbox("Enter Your Class :", (1,2,3,4,6))

button = st.button("Done")
if button :
    st.markdown(f"Name : {name} \n  Father Name : {fname}  \n Address : {adr}  \n Class : {classdate}")