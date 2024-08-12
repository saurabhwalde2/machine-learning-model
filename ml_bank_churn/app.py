import streamlit as st
import pandas as pd
#import joblib

# Load the trained model
#model = joblib.load('bank_churn_model.pkl')

import pickle

# Load the model from a file
with open('bankchurn_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title("Bank Customer Churn Prediction")




# Create input fields for user to enter data
CreditScore = st.number_input("Credit Score", min_value=300, max_value=900, step=1)
Age = st.number_input("Age", min_value=18, max_value=100, step=1)
Tenure = st.number_input("Tenure", min_value=0, max_value=10, step=1)
Balance = st.number_input("Balance", min_value=0.0, format="%.2f")
NumOfProducts = st.number_input("Number of Products", min_value=1, max_value=4, step=1)
EstimatedSalary = st.number_input("Estimated Salary", min_value=0.0, format="%.2f")
Geography = st.selectbox("Geography", ("France", "Germany", "Spain"))
Gender = st.selectbox("Gender", ("Male", "Female"))

# Convert categorical features to numeric
Geography_Germany = 1 if Geography == "Germany" else 0
Geography_Spain = 1 if Geography == "Spain" else 0
Gender_Male = 1 if Gender == "Male" else 0

# Create a predict button
if st.button("Predict"):
    # Prepare the input data as a DataFrame
    input_data = pd.DataFrame({
        'CreditScore': [CreditScore],
        'Age': [Age],
        'Tenure': [Tenure],
        'Balance': [Balance],
        'NumOfProducts': [NumOfProducts],
        'EstimatedSalary': [EstimatedSalary],
        'Geography_Germany': [Geography_Germany],
        'Geography_Spain': [Geography_Spain],
        'Gender_Male': [Gender_Male]
    })

    # Make prediction
    prediction = model.predict(input_data)

    # Display the result
    st.write(f"Prediction: {'Exited' if prediction[0] == 1 else 'Not Exited'}")

