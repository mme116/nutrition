import streamlit as st #web app
import pandas as pd #data manipulation
import numpy as np
import plotly.express as px #visualizations
import plotly.graph_objects as go #visualizations


st.set_page_config(
     page_title="nutrition_app.py",
     layout="wide",
     initial_sidebar_state="expanded",
     )

BMI=pd.read_csv("BMI.csv")
BMI=BMI.drop(BMI.columns[[0]], axis=1)
#st.write(BMI)

Obesity=pd.read_csv("Obesity.csv")
Obesity=Obesity.drop(Obesity.columns[[0]], axis=1)
#st.write(Obesity)

Underweight=pd.read_csv("final_underweight.csv")
Underweight=Underweight.drop(Underweight.columns[[0]], axis=1)
#st.write(Underweight)



st.title("Worldwide Nutrition Dashboard")
from PIL import Image
image = Image.open('bmi6.jpg')
st.image(image)



st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Charts accordingly:")
st.subheader("The dashboard will visualize the world's nutrition status in terms of Body Mass Index, Obesity, and Underweight in different regions.")


st.markdown("## Key Facts and Figures for the Year 2016")

metric1, metric2, metric3=st.columns(3)
metric1.metric(label="Overweight among adults", value="1.9B")
metric2.metric(label="Obesity among adults", value="650M")
metric3.metric(label="Underweight among adults", value="462M")

dataset_name=st.selectbox("Select Dataset", ("BMI", "Obesity", "Underweight"))
if not st.checkbox("Hide", True, key='3'):
	if dataset_name=="BMI":
		st.subheader("Average BMI (kg/m²) per Region over the Years")
		st.write("This dataset, collected from WHO website, shows the average BMI among adults per region from the year 1975 till the year 2016." )
		st.write(BMI)


	if dataset_name=="Obesity":
		st.subheader("Prevalence of Obesity (%) per Region in 2016")
		st.write("This dataset, collected from WHO website, shows the prevalence of obesity among adults per region in 2016.")
		st.write(Obesity)

	if dataset_name=="Underweight":
		st.subheader("Prevalence of Underweight (%) per Region in 2016")
		st.write("This dataset, collected from WHO website, shows the prevalence of underweight among adults per region in 2016.")
		st.write(Underweight)


select=st.sidebar.selectbox('Visualization type',['Line Chart-BMI', 'Bar Chart-Obesity', 'Pie Chart-Underweight'], key= "1")
if not st.sidebar.checkbox("Hide", True, key='2'):
	if select=="Bar Chart-Obesity":
		st.subheader("Percentage of Obesity (%) among Adults per Region for the Year 2016")
		fig= px.bar(Obesity, x=Obesity["Region"], y=Obesity["Percentage of Obesity (%)"], color=Obesity["Region"], range_y=[0,35], text="Percentage of Obesity (%)")
		st.plotly_chart(fig)
	
	if select == 'Line Chart-BMI':
		st.subheader("Pattern of Average BMI (kg/m²) across Different Regions over Time")
		fig=px.line(BMI, x=BMI["Year"], y=BMI["Average BMI (kg/m²)"], color=BMI["Region"])
		fig.update_layout(xaxis_title="Years", yaxis_title="Average BMI (kg/m²)")
		fig.update_xaxes(range=[1975, 2016])
		st.plotly_chart(fig)

	if select== "Pie Chart-Underweight":
		st.subheader("Prevalence of Underweight (%) per Region in 2016")
		fig= px.pie(Underweight, values='Percentage of Underweight (%)', names='Region',
             hover_data=['Percentage of Underweight (%)'], labels={'Percentage of Underweight (%)':'% of Underweight'})
		st.plotly_chart(fig)



