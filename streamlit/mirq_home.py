import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

st.write("Hello world")

st.header('Data')
st.header('A header with _italics_ :blue[colors] and **bold** text and emoji! :sunglasses:')

st.markdown('Streamlit can use **_use_ markdowns**')
st.markdown('This text is :red[colored red], and this is **:blue[colored blue]** and bold')

st.markdown(':green[$\sqrt{x^2+y^2}=1$] is Pythagoras theorem. :smile:')

st.write('Adding widget is same as declaring variable, no need for backends, routes, request etc.')


file = st.file_uploader('Upload file in CSV or Excel format', type=['csv', 'xlsx'])

if file is not None:
    # try:
    #     df = pd.read_csv(file)
    #     st.header(file.name)
    #     st.dataframe(df)
    # except:
    #     df = pd.read_excel(file)
    #     st.header(file.name)
    #     st.dataframe(df)

    # try:
    #     df2 = pd.DataFrame(df.groupby('STATION').mean())    
    #     st.map(df2)
    # except:
    #     pass


    try:
        df = pd.read_csv(file, parse_dates=['Time'])

        start_date, end_date = st.select_slider(
        'Select a time range',
        options=list(df['Time']),
        value=(df['Time'].min(), df['Time'].max()))

        mask = (df['Time'] > start_date) & (df['Time'] <= end_date)

        st.line_chart(df.loc[mask], x="Time", y="Price")
    except Exception as e:
        st.write(e)
