from nbformat import write
import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('My First App')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.read_csv('train.csv')
df

"""
# Chart
"""
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

'''# Map'''
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

'''# Checkbox'''
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

shart_data = df['Age']
st.line_chart(chart_data)

'''# Selectbox'''
option = st.selectbox(
    'Pilih kolom Age',
    df['Age']
)

'Your selected option is ', option

option_2 = st.sidebar.selectbox(
    'Pilih kolom Pclass',
     df['Pclass'])

'You selected:', option_2

left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")


'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'


kolom = st.radio(
    'pilih kolom?'
    ('Age', 'Survived', 'Pclass')
if kolom == 'Age':
    st.write(df.Age)
elif kolom == 'Survived':
    st.write(df.Survived)
else:
    st.write(df.Pclass)
)