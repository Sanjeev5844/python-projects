import streamlit as st
import pandas as pd
import numpy as np
st.title("Virat Kohli")
with st.echo():
    x=18    

with st.echo():
    y=17

with st.echo():
    z=x+y
    st.write(z)

st.write("Here is a dataframe")
st.write(pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
}))
df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})
df

chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['1','2','3']
)
st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000,2)/[50,50]+[37.76,-122.4],
    columns=['lat','lon'])
st.map(map_data)