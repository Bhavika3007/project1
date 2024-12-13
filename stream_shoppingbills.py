import streamlit as st

st.title("Shopping Bill Tracker")

sal = st.number_input("Salary amount:")

fbill = st.number_input("First shopping bill:", min_value=1, step=1)
sbill = st.number_input("Second shopping bill:", min_value=1, step=1)
tbill = st.number_input("Third shopping bill:", min_value=1, step=1)

shoppingbill = fbill + sbill + tbill

if st.button('Total shopping bills'):
    st.write(f"Total shopping bill: {shoppingbill}")

if sal > 0:
    per = (shoppingbill / sal) * 100
    if st.button('Total amount spent'):
        st.write(f"Total amount spent: {per:.2f}%")
else:
    st.error("Please enter a valid salary amount.")
