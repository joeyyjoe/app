import streamlit as st
import pandas as pd

APP_TITLE = "Fraud and Identity Theft Report"
APP_SUB_TITLE = "Source: Federal Trade Commission"

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    #LOAD DATA
    df = pd.read_csv('data/AxS-Fraud Box_Full Data_data.csv')

    st.write(df.shape)
    st.write(df.head())
    st.write(df.columns)

    if __name__ == "__main__":
        main()