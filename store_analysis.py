import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# File handling
try:
    df = pd.read_csv('storeperformance.csv')
except FileNotFoundError:
    st.error('File not found. Please ensure the "storeperformance.csv" file is in the correct directory.')
    st.stop()
except pd.errors.EmptyDataError:
    st.error('File is empty. Please provide a valid "storeperformance.csv" file.')
    st.stop()
except pd.errors.ParserError:
    st.error("Error parsing the file.")
    st.stop()
except Exception as e:
    st.error(f'An unexpected error occurred: {e}')
    st.stop()

#data visualization of original dataset

df = pd.read_csv('storeperformance.csv')
st.title('Welcome To The Site')

st.title('EDA of Store Analysis')

st.subheader('Original dataset')
st.write(df)
st.write(df.shape)


    # Cleaning the dataset
try:
    st.write('Dataset:')
    dataset = pd.read_csv('storeperformance.csv')
    st.markdown(f'Total records before cleaning: {len(dataset)}')
    st.write(dataset.head())
    st.write(dataset.tail())

    # Dropping duplicates
    dataset = dataset.drop_duplicates()
    st.subheader(f'Total records after removing duplicates: {len(dataset)}')

    # Displaying dataset info and description
    st.write(dataset.info())
    st.write(dataset.describe())
except Exception as e:
    st.error(f'An error occurred while cleaning the dataset: {e}')
    st.stop()

    
# filling null values 
st.subheader("After Handling Missing Values")
df['Age'].fillna('M',inplace = True)
df['Qty'].fillna(np.min(df['Gender']),inplace=False)
st.write(df)
st.write(df.shape)

#data visualization

st.subheader('Bar Chart Example')
x_column = st.selectbox('Select X-axis column', df.columns,index=17)

if x_column == 0:
    st.error('Please select different columns for X and Y axis.')
else:
    st.subheader('Bar Chart')
    st.bar_chart(df[x_column].head(10),color='#669999')

    st.subheader('Line Chart')
    st.line_chart(df[x_column].head(60))

    st.subheader('Scatter Plot')
    st.scatter_chart(df[x_column].head(60))

    st.subheader('Area Chart')
    st.area_chart(df[x_column].head(60))

    # pie chart using matplotlib
    st.subheader("Pie Chart Using Matplotlib")
    plt.figure(figsize=[6,6])
    plt.pie(df['Age Group'].value_counts().values,autopct='%1.1f%%',labels=df['Age Group'].value_counts().index, colors=['#669999','#FF6633','#666666'])
    st.pyplot(plt)

# barh
    st.subheader("Barh Chart")
    plt.figure(figsize=[10,10])
    plt.barh(df['Size'].value_counts().index,df['Size'].value_counts().values,color=('#669999','#FF9933'))
    plt.title('THIS IS A BAR GRAPH')
    plt.xlabel('Count Of Clothes ')
    plt.ylabel('Size Of Clothes')
    plt.grid()
    plt.show()
    st.pyplot(plt)