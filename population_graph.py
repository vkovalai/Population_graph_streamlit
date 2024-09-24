import pandas as pd

df = pd.read_csv("population.csv")
df = df.drop(columns = ["Unnamed: 0"])
df.head()
#Lets define the list of column headers (country names) (excepr the first column which is the year)

unique_names = df["country"].unique().tolist()

#Lets define the years (the first column)

years = df["year"].unique()

#Then create the first column of dataframe
df_visu = pd.DataFrame(years,columns=["year"])
#display(df_visu.head())

#What should we have in other colums? Population by country
#For example Sweden
#df[df["country"]== "Sweden"]["pop"].values

#For all the countries
for country_name in unique_names:
    df_visu[country_name]=df[df["country"]== country_name]["pop"].values

#Make graphics

import streamlit as st
#Define the figure title

st.title("Population plot")
#Define a selector (colums to draw)
columns = st.multiselect("Countries: ",unique_names)
#Plot the line chart

st.line_chart(df_visu,x = "year", y = columns, y_label = "Population", x_label = "Year")

#streamlit run .\population_graph.py