import streamlit as st
import plotly.figure_factory as ff
from pandas.api.types import is_numeric_dtype
import pandas as pd

#Title
st.title("Data Analysis App")
st.write("This app is for data analysis")
st.balloons()

st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


    st.checkbox
    agree = st.checkbox('I agree')

    if agree:
     st.write('Great!')

     #google markdown specs
     st.markdown("steamlit can use **_use_markdowns**")
     st.markdown("This text is :red[colored red], and this is**:blue[colored blue]**  and bold")
     st.markdown(":green[$\sqrt{x^2+y^2}=1$] is pythagoras theorem. :smile:")

     st.write("Adding widget is same as declaring variable, no need for backend, just routes, request etc.")

     file = st.file_uploader("Upload file in CSV or excel format", type=["csv", "xlsx"])

     if file is not None:
        try:
            df = pd.read_csv(file.read, engine="openpyxl")
            st.header(file.name)
            st.dataframe(df)
            
        except:
            df=pd.read_excel(file.read, engine="openpyxl")
            st.header(file.name)
            st.dataframe(df)

            
        try:
             st.map(df)
        except:
            pass




