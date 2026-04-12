import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title="Startup Analysis")

df = pd.read_csv('startup_clean.csv')

def load_investor_details(investor):
    st.title(investor)
    # load the last recent 5 investments od the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','verical','city','round','amount']]
    st.subheader('Most recent investments')
    st.dataframe(last5_df)
    
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    with col1:
        # biggest investments
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending = False)
        st.subheader("Biggest Investments")
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        
        st.pyplot(fig)
        
    with col2:
        verical_series = df[df['investors'].str.contains(investor)].groupby('verical')['amount'].sum()
        st.subheader("Sectors Invested")
        fig1, ax1 = plt.subplots()
        ax1.pie(verical_series, labels=verical_series.index, autopct="%0.01f%%")
        
        st.pyplot(fig1)
        
    with col3:
        verical_series = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        st.subheader("Stage Invested")
        fig1, ax1 = plt.subplots()
        ax1.pie(verical_series, labels=verical_series.index, autopct="%0.01f%%")
        
        st.pyplot(fig1)

# vertical is named as verical
st.sidebar.title("Startup Funding Analysis")

option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    st.title("Overall Analysis")
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Analysis')
    st.title("Startup Analysis")
else:
    selected_investor = st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Analysis')
    st.title("Investor Analysis")
    
    if btn2:
        load_investor_details(selected_investor)