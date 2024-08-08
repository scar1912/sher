import streamlit as st
import numpy as np
import plotly.express as pe
st.markdown(
    """
    <style>
    .main{
    background-color: #FFD700;
    color: black;
    }
    </style>
    """,
    unsafe_allow_html=True)
st.title("Login")
a=st.text_input("Enter user name")
b=st.text_input("Enter password")
if st.button("Sign in"):
    if a=="Rohit456" and b=="Rising@456":
        st.write("Login successful")
    else:
        st.write("Login Failed")

st.title("Tax calculator")
name=st.text_input("Enter your name")
val=st.number_input("Enter your annual salary")
tax=0
if st.button("Calculator"):
    if val<500000:
        tax=0
    elif val<750000:
        tax=val*5/100
    else:
        tax=val*10/100
    st.subheader(f"Tax to be paid Rs. {tax}")

st.title("EMI calculator")
loan=st.number_input("Enter loan amount")
time=st.slider("Enter duration in years",0,10,2)
interest=8.75
emi=(loan*interest*time/100)+loan
emi=emi/(time*12)
st.subheader(f"emi to be paid Rs. {int(emi)}")
