import streamlit as st 
import pandas as pd
import numpy as np
import io
import requests
import warnings 
warnings.filterwarnings('ignore')

# compactor = pd.read_csv('compactor.csv')


def shed_func(df): 
    # shed = pd.read_csv('shed.csv')
    shed = df
    selection = st.sidebar.radio('Search by : ', ['Part Number', 'Mat Code', 'Description'], index=0)
    result = shed
    if selection == 'Part Number' : 
        
        partno = st.selectbox('Pick a Part No', shed['partnumber'].dropna())
        result = shed[shed['partnumber'] == partno]
    
    if selection == 'Mat Code' : 
        shed['matcode'].replace({'nan' : np.nan}, inplace=True)
        matcode = st.selectbox('Pick a Mat code', shed['matcode'].dropna().to_list())
        result = shed[shed['matcode'] == matcode]

   
    if selection == 'Description' : 
        description = st.selectbox('Pick a Name', shed['description'].dropna())
        result = shed[shed['description'] == description]

    result.replace({'nan' : np.nan}, inplace=True)

    st.markdown(f"# {result['description'].values[0]}")
    if not result['sparePic'].isnull().any()  : 
        st.image(result['sparePic'].values[0])
    
    st.markdown(f"Location : {result['location'].values[0]}")
    st.markdown(f"Material Code : {result['matcode'].values[0]}")
    st.markdown(f"Part Number : {result['partnumber'].values[0]}")
    st.markdown(f"Qty : {result['quantity'].values[0]}   |  UoM : {result['UOM'].values[0]}")
    st.markdown(f"PO No: {result['po'].values[0]}")
    st.markdown(f"Tags: {result['tags'].values[0]}")

def compactor(df) : 
    #compactor = pd.read_csv('compactor.csv')
    
    compactor = df
    selection = st.sidebar.radio('Search by : ', ['Part Number', 'Mat Code', 'Description'], index=0)
    result = compactor
    if selection == 'Part Number' : 
        partno = st.selectbox('Pick a Part No', compactor['partnumber'].dropna())
        result = compactor[compactor['partnumber'] == partno]
    
    if selection == 'Mat Code' : 
        matcode = st.selectbox('Pick a Mat code', compactor['matcode'].dropna())
        result = compactor[compactor['matcode'] == matcode]

    if selection == 'Description' : 
        description = st.selectbox('Pick a Name', compactor['description'].dropna())
        result = compactor[compactor['description'] == description]

   
    result.replace({'nan' : np.nan}, inplace=True)

    st.markdown(f"# {result['description'].values[0]}")
    if not result['sparePic'].isnull().any() : 
        st.image(result['sparePic'].values[0])
    

    st.markdown(f"Location : {result['location'].values[0]}")
    st.markdown(f"Material Code : {result['matcode'].values[0]}")
    st.markdown(f"Part Number : {result['partnumber'].values[0]}")
    st.markdown(f"Qty : {result['quantity'].values[0]}   |  UoM : {result['UOM'].values[0]}")
    st.markdown(f"PO No: {result['po'].values[0]}")
    st.markdown(f"Tags: {result['tags'].values[0]}")

@st.cache()
def create_compactor_df() : 
    url = 'https://drive.google.com/file/d/1A7b8QQyTzZsjuhJ9yOhcuJ_gXoQC3zy0/view?usp=sharing'
    file = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
    return pd.read_csv(file)

@st.cache()
def create_shed_df() : 
    url = 'https://drive.google.com/file/d/19AoOXN7_rjb4GNn8Nazzt6ywDw6PDAZF/view?usp=sharing'
    file = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
    return pd.read_csv(file)

    

# sidebar
st.sidebar.markdown('# Logging Store')
section = st.sidebar.radio('Select a Section :', ['Compactor', 'Shed'], index=0)

# sections
if section == 'Compactor' : 
    df = create_compactor_df()
    compactor(df)

if section == 'Shed' : 
    df = create_shed_df()
    shed_func(df)


