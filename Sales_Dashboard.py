# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px



#loading data
data=pd.read_csv("Superstore.csv",encoding="windows-1252")
data["Order Date"]=pd.to_datetime(data["Order Date"])
st.set_page_config(page_title="Sales Dashboard",page_icon=None,layout="wide")

# setting sidebar
st.sidebar.header("Sales Dashboard")
st.sidebar.image("Sales.jpg")
st.sidebar.write("This is Sales dashboard for suoerstore")
st.sidebar.write("")
st.sidebar.markdown("Made By :bar_chart:"+"[Amna](https://google.com)")
st.sidebar.write("")
st.sidebar.write("Filter Your data")
city=st.sidebar.selectbox("City:",data["City"].drop_duplicates().sort_values())
year=st.sidebar.selectbox("Year:",data["Order Date"].dt.year.drop_duplicates().sort_values())


fdata=data[(data["City"]==city)&(data["Order Date"].dt.year==year)]

# rows 1
c1,c2,c3,c4=st.columns(4)
c1.metric("Total Sales K",(fdata['Sales'].sum()/1000).round())
c2.metric("Total Profit K",(fdata['Profit'].sum()/1000).round())
c3.metric("Total Quantity ",(fdata['Quantity'].sum()).round())
c4.metric("Profit Margin % ",(fdata['Profit'].sum()/fdata['Sales'].sum()*100).round())

#row 2
c1,c2=st.columns(2)
fig=px.bar(data_frame=fdata,x='Segment',y="Sales")
c1.plotly_chart(fig,use_container_width=True)
fig=px.bar(data_frame=fdata,x='State',y="Sales")
c2.plotly_chart(fig,use_container_width=True)
#Row 3
fig=px.bar(data_frame=fdata,x='City',y="Sales")
st.plotly_chart(fig,use_container_width=True)

# Row 5
fig=px.scatter(data_frame=fdata,x='Sales',y='Profit', color='Segment',size='Quantity')
st.plotly_chart(fig,use_container_width=True)

#Row 6
st.text("Sales By Category")
fig=px.pie(data_frame=fdata,names='Category',values='Sales',hole=.4)
st.plotly_chart(fig,use_container_width=True)