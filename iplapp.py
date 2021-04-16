
import math
import numpy as np
import pickle
import streamlit as st
filename='first.pkl'
regressor = pickle.load(open(filename,'rb'))
st.markdown("<h1 style='text-align: center; color: red;'>IPL Score Predictor (First Innings)</h1>", unsafe_allow_html=True)
 
st.markdown('''
<style>
body {
background-image: url("https://cdn.insidesport.co/wp-content/uploads/2021/02/04184843/1-1-9.jpg");
background-size: cover;
}
</style>
''',unsafe_allow_html=True)
if st.button('description'):
    st.write('This is the app you can use to predict the ipl score made by a certain team To make sure the model has good accuracy and some reliability the minium no of overs considered is more than 5 overs')

temp_array = list()
batting_team= st.selectbox('Select the batting team ',('Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab','Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals','Royal Challengers Bangalore','Sunrisers Hyderabad'))

if batting_team == 'Chennai Super Kings':
    temp_array = temp_array + [1,0,0,0,0,0,0,0]
elif batting_team == 'Delhi Daredevils':
    temp_array = temp_array + [0,1,0,0,0,0,0,0]
elif batting_team == 'Kings XI Punjab':
    temp_array = temp_array + [0,0,1,0,0,0,0,0]
elif batting_team == 'Kolkata Knight Riders':
    temp_array = temp_array + [0,0,0,1,0,0,0,0]
elif batting_team == 'Mumbai Indians':
    temp_array = temp_array + [0,0,0,0,1,0,0,0]
elif batting_team == 'Rajasthan Royals':
    temp_array = temp_array + [0,0,0,0,0,1,0,0]
elif batting_team == 'Royal Challengers Bangalore':
    temp_array = temp_array + [0,0,0,0,0,0,1,0]
elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]

bowling_team = st.selectbox('Select the bowling team ',('Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab','Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals','Royal Challengers Bangalore','Sunrisers Hyderabad'))
if bowling_team==batting_team:
    st.error('Bowling and Batting teams should be different')
if bowling_team == 'Chennai Super Kings':
    temp_array = temp_array + [1,0,0,0,0,0,0,0]
elif bowling_team == 'Delhi Daredevils':
    temp_array = temp_array + [0,1,0,0,0,0,0,0]
elif bowling_team == 'Kings XI Punjab':
    temp_array = temp_array + [0,0,1,0,0,0,0,0]
elif bowling_team == 'Kolkata Knight Riders':
    temp_array = temp_array + [0,0,0,1,0,0,0,0]
elif bowling_team == 'Mumbai Indians':
    temp_array = temp_array + [0,0,0,0,1,0,0,0]
elif bowling_team == 'Rajasthan Royals':
    temp_array = temp_array + [0,0,0,0,0,1,0,0]
elif bowling_team == 'Royal Challengers Bangalore':
    temp_array = temp_array + [0,0,0,0,0,0,1,0]
elif bowling_team == 'Sunrisers Hyderabad':
    temp_array = temp_array + [0,0,0,0,0,0,0,1]
    
overs = st.number_input('enter the overs',min_value=5.1,max_value=19.5,value=5.1,step=0.1)
if overs-math.floor(overs)>0.5:
    st.error('Please enter valid over input as one over only contains 6 balls')

runs = st.number_input('enter the total runs',min_value=0,max_value=354,step=1,format='%i')
wickets =st.slider('enter the wickets fallen till now',0,9)
wickets=int(wickets)
runs_in_prev_5 = st.number_input('runs scored in the last 5 overs',min_value=0,max_value=runs,step=1,format='%i')
wickets_in_prev_5 = st.number_input('wickets taken in the last 5 overs',min_value=0,max_value=wickets,step=1,format='%d')

temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
data = np.array([temp_array])

if st.sidebar.button('About Project'):
    st.sidebar.write('The project is built on the IPL dataset from kaggle and uses linear regression to predcit the runs scored in first innings of any match')
    st.sidebar.write('Dataset Link - https://www.kaggle.com/manasgarg/ipl')
if st.sidebar.button('About Developer'):
    st.sidebar.write('Hi my name is Rahul Rustagi and I am a university of Michigan certified data science professional . Most of my projects and training have been centered around the concept of automation and improved system usability. Not only do I have experience in building and optimization of machine learning and deep learning models ,I also have experience in their front end development and cloud deployment on services like Azure ,GCP and AWS.  ')
    st.sidebar.write('Linkedin profile - https://www.linkedin.com/in/rahul-rustagi-4a1836133/ ')
    st.sidebar.write('Github profile - https://github.com/rrustagi9 ')
if st.sidebar.button('About IPL'):
    st.sidebar.write('The Indian Premier League (IPL) is a professional Twenty20 cricket league, contested by eight teams based out of eight different Indian cities.[3] The league was founded by the Board of Control for Cricket in India (BCCI) in 2007. It is usually held between March and May of every year and has an exclusive window in the ICC Future Tours Programme.')
if st.button('predict score'):
    my_prediction = int(regressor.predict(data)[0])
    while((my_prediction-5)<runs):
        my_prediction=my_prediction+11
    st.write('The score of this inning would most probably be in the range of',my_prediction-5,'to',my_prediction+5 )
            
