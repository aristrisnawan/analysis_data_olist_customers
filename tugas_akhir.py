import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import gdown
sns.set_theme(style='dark')

file_id = '1pKIMOECTiNRg1EEgAZ3WFTjEBeQL6lHw'
url = f"https://drive.google.com/uc?id={file_id}"
output = 'olist_customers_dataset.csv'

gdown.download(url, output, quiet=False)

# Baca file CSV
data = pd.read_csv(output)
df = pd.DataFrame(data)
datas = data.head()
# st.dataframe(datas)
data['customer_state'].count()
state_column = data['customer_state'].value_counts().reset_index()
state_column.columns = ['customer_state','count']

def customer_site():
    data['customer_state'].count()
    state_column = data['customer_state'].value_counts().reset_index()
    state_column.columns = ['customer_state','count']

    def top_5_customer_state(df):
        top_5 = state_column.head()
        top_5

        fig, ax = plt.subplots(figsize=(8,5))
        sns.barplot(y=top_5['count'], x=top_5['customer_state'], ax=ax)
        ax.set_title('Data Top 5 customer berdasarkan state')
        ax.set_xlabel('State')
        ax.set_ylabel('Jumlah Customer')
        return fig

    def bottom_5_customer_state(df):
        bottom_5 = state_column.tail()
        bottom_5

        fig, ax = plt.subplots(figsize=(8,5))
        sns.barplot(y=bottom_5['count'], x=bottom_5['customer_state'], ax=ax)
        ax.set_title('Data Bottom 5 customer berdasarkan state')
        ax.set_xlabel('State')
        ax.set_ylabel('Jumlah Customer')
        return fig

    st.subheader('Data Customer State')
    col1, col2 = st.columns(2)

    with col1:
        st.metric('Data Terbesar :',value=state_column['count'].max())
    with col2:
        st.metric('Data Terkecil :',value=state_column['count'].min())

    
    data_select = st.selectbox(
        label='Pilih data yang kamu inginkan',
        options=('Top 5','Bottom 5')
    )
    st.subheader(f"{data_select} Customer State")
    if data_select == 'Top 5':
        fig = top_5_customer_state(any)
        st.pyplot(fig)
    else:
        fig = bottom_5_customer_state(any)
        st.pyplot(fig)

def customer_city():
    data['customer_state'].count()
    state_column = data['customer_state'].value_counts().reset_index()
    state_column.columns = ['customer_state','count']

    def top_5_customer_state(df):
        top_5 = state_column.head()
        top_5

        fig, ax = plt.subplots(figsize=(8,5))
        sns.barplot(y=top_5['count'], x=top_5['customer_state'], ax=ax)
        ax.set_title('Data Top 5 customer berdasarkan state')
        ax.set_xlabel('State')
        ax.set_ylabel('Jumlah Customer')
        return fig

    def bottom_5_customer_state(df):
        bottom_5 = state_column.tail()
        bottom_5

        fig, ax = plt.subplots(figsize=(8,5))
        sns.barplot(y=bottom_5['count'], x=bottom_5['customer_state'], ax=ax)
        ax.set_title('Data Bottom 5 customer berdasarkan state')
        ax.set_xlabel('State')
        ax.set_ylabel('Jumlah Customer')
        return fig

    st.subheader('Data Customer State')
    col1, col2 = st.columns(2)

    with col1:
        st.metric('Data Terbesar :',value=state_column['count'].max())
    with col2:
        st.metric('Data Terkecil :',value=state_column['count'].min())

    
    data_select = st.selectbox(
        label='Pilih data yang kamu inginkan',
        options=('Top 5','Bottom 5')
    )
    st.subheader(f"{data_select} Customer State")
    if data_select == 'Top 5':
        fig = top_5_customer_state(any)
        st.pyplot(fig)
    else:
        fig = bottom_5_customer_state(any)
        st.pyplot(fig)



def customer_city():
    data['customer_city'].count()
    city_column = data['customer_city'].value_counts().reset_index()
    city_column.columns = ['customer_city','count']

    def top_5_customer_city():
        top5 = city_column.head()
        top5

        fig, ax = plt.subplots(figsize=(8,5))
        sns.barplot(y=top5['count'], x=top5['customer_city'], ax=ax)
        ax.set_title('Data top 5 customer city')
        ax.set_xlabel('City')
        ax.set_ylabel('Jumlah Customer')
        return fig
    def bottom_5_customer_city():
        bottom5 = city_column.tail()
        bottom5
        fig, ax = plt.subplots(figsize=(8,5))
        sns.barplot(y=bottom5['count'], x=bottom5['customer_city'], ax=ax)
        ax.set_title('Bottom 5 customer city')
        ax.set_ylabel('City')
        ax.set_xlabel('Jumlah Customer')
        return fig
    
    st.subheader('Customer City')
    col1, col2 = st.columns(2)

    with col1:
        st.metric('Data Terbesar', value=city_column['count'].max())
    with col2:
        st.metric('Data Terkecil', value=city_column['count'].min())
    
    data_selected = st.selectbox(
        label='Pilih data yang kamu inginkan',
        options=('Top 5 Customer City','Bottom 5 Customer City')
    )
    
    st.subheader(f"{data_selected} Customer City")

    if data_selected == 'Top 5 Customer City':
        fig = top_5_customer_city()
        st.pyplot(fig)
    else:
        fig = bottom_5_customer_city()
        st.pyplot(fig)

    


with st.sidebar:
        st.title('Tugas Akhir')
        st.image('https://images.unsplash.com/photo-1556742212-5b321f3c261b?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')

st.header('Tugas Akhir Dicoding 😁')

tab1, tab2 = st.tabs(['Customer State','Customer City'])


with tab1:
    customer_site()
with tab2:
    customer_city()
