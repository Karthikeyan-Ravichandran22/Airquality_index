
import streamlit as st
import pickle
import time




dtree=pickle.load(open("dtree_regressor_pickle",'rb'))
linear_reg=pickle.load(open("linerRegression_pickle",'rb'))
Rfreg=pickle.load(open("RFregressor_pickle",'rb'))




    

                         
   
st.title("Air Quality Index Prediction ")
st.image("https://www.ankitparakh.com/wp-content/uploads/2021/11/Understanding-Air-Quality-Index-Web-scaled.jpg")
st.markdown("Here we are using temperature as the input to predict the day's revenue")

st.subheader("Enter the temperature")
T = st.number_input('', 7,100,key = "T")
st.write("Average Temperature (°C)")

TM = st.number_input('', 8,100,key = "TM")
st.write("Maximum temperature (°C)")

Tm = st.number_input('', 8,100,key = "Tm")
st.write("Minimum temperature (°C)")

SLP = st.number_input('', 8,100,key = "SLP")
st.write("Atmospheric pressure at sea level (hPa)")

H = st.number_input('', 8,100,key = "H")
st.write("Average relative humidity (%)")

VV = st.number_input('', 9,100,key = "VV")
st.write("Average visibility (Km)")


V = st.number_input('', 6,100,key = "V")
st.write("Average wind speed (Km/h)")

VM = st.number_input('', 5,100,key = "VM")
st.write("Maximum sustained wind speed (Km/h)")



algo = st.sidebar.selectbox("Select the algorithm you want to use for prediction?", ("Decision tree", "Linear regression", "Random forest"))
if algo=="Linear regression":
    if st.button("Predict"): 
        Rsult=linear_reg.predict([[T,TM,Tm,SLP,H,V,VV,VM]])
        st.success(' AIR QUALITY INDEX  {}'.format(Rsult))
        
if algo=="Decision tree":
    if st.button("Predict"): 
        Rsult=dtree.predict([[T,TM,Tm,SLP,H,V,VV,VM]])
        
        st.success(' AIR QUALITY INDEX  {}'.format(Rsult))
        
if algo=="Random forest":
    if st.button("Predict"): 
        Rsult=Rfreg.predict([[T,TM,Tm,SLP,H,V,VV,VM]])
        with st.balloons():
            time.sleep(1)
        st.success(' PREDICTED AIR QUALITY INDEX  {}'.format(Rsult))
        


