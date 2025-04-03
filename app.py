import streamlit as st
import pandas as pd
import pickle

# Load model and encoders
with open('finances_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('label_encoder.pkl', 'rb') as le_file:
    encoders = pickle.load(le_file)

# Streamlit app title
st.title("Financial Inclusion Predictor")

# Input fields
location = st.selectbox("Location Type", ['Urban', 'Rural'])
cellphone = st.selectbox("Cellphone Access", ['Yes', 'No'])
household_size = st.number_input("Household Size", min_value=1, max_value=30)
age = st.number_input("Age of Respondent", min_value=10, max_value=100)
gender = st.selectbox("Gender", ['Male', 'Female'])
relationship = st.selectbox("Relationship With Head", [
    'Head of Household', 'Spouse', 'Child', 'Parent',
    'Other Relative', 'Other non-relatives'
])
marital = st.selectbox("Marital Status", [
    'Married/Living together', 'Single', 'Widowed', 'Divorced', 'Separated', 'Dont know'
])
education = st.selectbox("Education Level", [
    'No formal education', 'Primary education', 'Secondary education',
    'Tertiary education', 'Vocational/Specialised training', 'Other/Dont know/RTA'
])
job = st.selectbox("Job Type", [
    'Self employed', 'Government Dependent', 'Formally employed Private',
    'Formally employed Government', 'Informally employed', 'Farming and Fishing',
    'Remittance Dependent', 'Other Income', 'No Income'
])

# Predict button
if st.button("Predict Bank Account"):
    # Create DataFrame with all required columns
    input_df = pd.DataFrame({
        'country': ['Kenya'],            # Placeholder
        'year': [2018],                  # Placeholder
        'uniqueid': ['uniqueid_1'],    # Placeholder
        'location_type': [location],
        'cellphone_access': [cellphone],
        'household_size': [household_size],
        'age_of_respondent': [age],
        'gender_of_respondent': [gender],
        'relationship_with_head': [relationship],
        'marital_status': [marital],
        'education_level': [education],
        'job_type': [job]
    })

    # Apply label encoders safely
    for col in encoders:
        if col in input_df.columns:
            input_df[col] = encoders[col].transform(input_df[col])

    # Predict
    prediction = model.predict(input_df)[0]

    # Display result
    if prediction == 1:
        st.success("Prediction: Has a bank account")
    else:
        st.error("Prediction: Does NOT have a bank account")
