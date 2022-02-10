import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title('My first app')
# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))


"""
# Titanic:
"""

df = pd.read_csv('./dataset/train.csv')

df

'''
# checkbox 
'''
show_df= st.checkbox("Show dataframe")
st.write(show_df)

if show_df:
  st.write(df)

"""
# Line Chart
"""
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

chart_data = df['Age']
st.line_chart(chart_data)


"""
# Map
"""
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


'''
selectbox op1
'''
option= st.selectbox(
    'pilih kolom Age',
    df['Age'])

'You selected: ', option

'''Lay out your app
'''
option_1 = st.sidebar.selectbox(
    'pilih kolom Pclass',
     df['Pclass'])


left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.markdown('This is the right column')

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")


'''
Show progress
'''
import time

# 'Starting a long computation...'
# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(20):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# '...and now we\'re done!'


'''
radio button
'''
kolom = st.radio(
    "periksa kolom?",
    ('Age', 'Survived', 'Pclass'))
if kolom == 'Age':
    st.write(df.Age)
elif kolom == 'Survived':
    st.write(df.Survived)
else:
    st.write(df.Pclass)

'''
radio button
'''

kolom_survived = st.radio(
    "periksa kolom Survived",df.Survived.unique())
st.write(df[df.Survived== kolom_survived])

#bisa diubah ke sidebar
# kolom_survived = st.sidebar.radio(
#     "periksa kolom Survived",df.Survived.unique())
# st.write(df[df.Survived== kolom_survived])

'''
select box titanic
'''

survived_pclass= st.selectbox(
    'pilih Pclass', df.Pclass.unique())

st.write(df[
  (df.Pclass== survived_pclass) &
  (df.Survived== kolom_survived)
  ])  

'''
# multiselect
'''
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
# st.write('You selected:', options)

'''
# slider
'''
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)) # 25 untuk mulai awalnya dari 25 dan akhirnya 75
st.write('Values:', values)

values2 = st.slider(
    'Select a range of values',
    0.0, df.Age.max(), (10.0, 60.0)) # awal 10, akhir 60
st.write('Values:', values2)
st.write(df[(df.Age>= values2[0]) & (df.Age<= values2[1])])
st.write(df[(df.Age>= values2[0]) & (df.Age<= values2[1])].shape)
# visualizations column age
# st.bar_chart(df[(df.Age>= values2[0]) & (df.Age<= values2[1])].Age)

#histogram using plotly and setting the number of bins
import plotly.express as px
#setting bins
fig = px.histogram(df[(df.Age>= values2[0]) & (df.Age<= values2[1])].Age, x='Age', nbins=20)
st.plotly_chart(fig)

#histogram using matplotlib
import matplotlib.pyplot as plt
# plt.hist(df[(df.Age>= values2[0]) & (df.Age<= values2[1])].Age)
# st.pyplot() #ini akan ada warning karena update
st.set_option('deprecation.showPyplotGlobalUse', False) #untuk mematikan peringatan warning

data_age= df[(df.Age>= values2[0]) & (df.Age<= values2[1])].Age
fig,ax = plt.subplots()
ax.hist(data_age, bins=10)
st.pyplot()

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title) # default value Life of Brian
st.write('The current movie title is', 'sardi') # sardi

number = st.number_input('Insert a number')
st.write('The current number is ', number)

st.number_input('Insert a number', 0.0, 100.0, 90.0)

txt = st.text_area('Text to analyze', '''
    hallo jono
    ini text area
    ''')
st.write('Sentiment:', txt)

# st.date_input('Pick a date', datetime.datetime(2020, 6, 1))
st.date_input('enter a date')

st.file_uploader("Choose a file", type=["csv", "txt"])


add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


#contoh visualisasi dengan selectbox
df_titanic = pd.read_csv('./dataset/train.csv')
#selectbox 
list_columns = ['Age', 'Fare']
df_titanic_select = st.selectbox('select column', list_columns)

plt.hist(df_titanic[df_titanic_select])
st.pyplot()

