import streamlit as st 
import pickle
import pandas as pd 
from PIL import Image

st.title("Welcome to Streamlit")

model=pickle.load(open('model.sav','rb'))
st.header("Telecom Data Analyis")
st.text("user_id, engagement_score, experience_score and satisfaction_score Analysis")

st.write(model.head(10))
customer_age = st.slider('Customer Age', 18, 100, 30)
plan_type = st.selectbox('Plan Type', ['Basic', 'Premium'])
call_duration = st.slider('Call Duration (minutes)', 0, 2000, 500)
data_usage = st.slider('Data Usage (MB)', 0, 10000, 2000)

st.markdown('### Bar chart')
st.bar_chart(model['user_id'][0:10])
st.bar_chart(model['engagement_score'][0:10])
st.bar_chart(model['experience_score'][0:10])
st.bar_chart(model['satisfaction_score'][0:10])

st.header("Recommendation:")
st.text  ("Based on the positive growth potential and the company's strong foundation, I recommend \nthat the employer seriously consider purchasing this company.\nThe data analysis highlights a healthy customer base, positive engagement, and high \nsatisfaction levels. With the right strategic investments and improvements in customer\nexperience, the company can further solidify its position in the market and drive \nfuture growth.")
st.image(Image.open('Streamlit_image.png'))


