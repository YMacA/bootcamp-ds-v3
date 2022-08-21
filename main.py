import pandas as pd

import streamlit as st
#from pandasql import sqldf
st.title('Exercise 3 (Inventory Discrepancy)')
st.text('''
1. Remove dups
2. Aggregate
3. Merge 2 datasets
 ''')

df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)

df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)


st.dataframe(df_expected.sample(2).T)
