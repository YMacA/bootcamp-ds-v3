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

code = '''
df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)

df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)

'''
st.code(code, language='python')

code = '''
df_expected.sample(2).T
'''
st.code(code, language='python')

st.dataframe(df_expected.sample(2).T)
#df_counted.shape()
#df_counted['RFID'].nunique()
code = '''

df_counted = df_counted.drop_duplicates("RFID")

df_B = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})

'''
st.code(code, language='python')

df_counted = df_counted.drop_duplicates("RFID")

df_B = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})

code = '''
df_B.sample(10)
'''
st.code(code, language='python')

st.dataframe(df_B.sample(10))

my_cols_selected = ["Retail_Product_Color",
"Retail_Product_Level1",
"Retail_Product_Level1Name",
"Retail_Product_Level2Name",
"Retail_Product_Level3Name",
"Retail_Product_Level4Name",
"Retail_Product_Name",
"Retail_Product_SKU",
"Retail_Product_Size",
"Retail_Product_Style",
"Retail_SOHQTY"]

code = '''
my_cols_selected = ["Retail_Product_Color",
"Retail_Product_Level1",
"Retail_Product_Level1Name",
"Retail_Product_Level2Name",
"Retail_Product_Level3Name",
"Retail_Product_Level4Name",
"Retail_Product_Name",
"Retail_Product_SKU",
"Retail_Product_Size",
"Retail_Product_Style",
"Retail_SOHQTY"]

'''
st.code(code, language='python')

code = '''
df_A = df_expected[my_cols_selected]
'''
st.code(code, language='python')

df_A = df_expected[my_cols_selected]

code = '''
df_A.head().T
'''
st.code(code, language='python')

st.dataframe(df_A.head().T)



df_discrepancy = pd.merge(df_A, df_B, how="outer", left_on="Retail_Product_SKU", right_on="Retail_Product_SKU", indicator=True)

code = '''
df_discrepancy = pd.merge(df_A, df_B, how="outer", left_on="Retail_Product_SKU", right_on="Retail_Product_SKU", indicator=True)
'''
st.code(code, language='python')

code = '''
df_discrepancy.head()
'''
st.code(code, language='python')

st.dataframe(df_discrepancy.head())

df_discrepancy['Retail_CCQTY'] = df_discrepancy['Retail_CCQTY'].fillna(0)

df_discrepancy["Retail_CCQTY"] = df_discrepancy["Retail_CCQTY"].astype(int)

code = '''
df_discrepancy['Retail_CCQTY'] = df_discrepancy['Retail_CCQTY'].fillna(0)

df_discrepancy["Retail_CCQTY"] = df_discrepancy["Retail_CCQTY"].astype(int)

'''
st.code(code, language='python')

code = '''
df_discrepancy.head()
'''
st.code(code, language='python')

st.dataframe(df_discrepancy.head())

#st.write(df_discrepancy.dtypes())

df_discrepancy["Retail_SOHQTY"] = df_discrepancy["Retail_SOHQTY"].fillna(0).astype(int)

df_discrepancy["Diff"] = df_discrepancy["Retail_CCQTY"] - df_discrepancy["Retail_SOHQTY"]

code = '''
df_discrepancy["Retail_SOHQTY"] = df_discrepancy["Retail_SOHQTY"].fillna(0).astype(int)

df_discrepancy["Diff"] = df_discrepancy["Retail_CCQTY"] - df_discrepancy["Retail_SOHQTY"]

'''
st.code(code, language='python')

code = '''
df_discrepancy.head()
'''
st.code(code, language='python')

st.dataframe(df_discrepancy.head())

code = '''
df_discrepancy.loc[df_discrepancy["Diff"]<0, "Unders"] = df_discrepancy["Diff"] * (-1)
df_discrepancy["Unders"] = df_discrepancy["Unders"].fillna(0).astype(int)
'''
st.code(code, language='python')

df_discrepancy.loc[df_discrepancy["Diff"]<0, "Unders"] = df_discrepancy["Diff"] * (-1)

df_discrepancy["Unders"] = df_discrepancy["Unders"].fillna(0).astype(int)

code = '''
df_discrepancy.sample(10)
'''
st.code(code, language='python')

st.dataframe(df_discrepancy.sample(10))

code = '''
df_discrepancy.groupby("Retail_Product_Level1Name").sum()
'''
st.code(code, language='python')

st.dataframe(df_discrepancy.groupby("Retail_Product_Level1Name").sum())

code = '''
df_discrepancy.describe()
'''
st.code(code, language='python')
st.dataframe(df_discrepancy.describe())

#st.write(df_discrepancy.shape())


df_discrepancy[df_discrepancy["Diff"].isnull()]
code = '''
df_discrepancy[df_discrepancy["Diff"].isnull()]
'''
st.code(code, language='python')



