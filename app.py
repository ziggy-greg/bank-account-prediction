import streamlit as st
import pandas as pd
import pickle

# Load model and encoders
with open('finances_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('label_encoder.pkl', 'rb') as le_file:
    encoders = pickle.load(le_file)

# --- UI Layout ---
st.markdown("<h1 style='color:#FFA500; text-align: center;'>Financial Inclusion Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict if an individual is likely to have access to a bank account based on demographic features.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- User Inputs ---
location = st.selectbox("Location Type", ['Urban', 'Rural'])
cellphone = st.selectbox("Cellphone Access", ['Yes', 'No'])
household_size = st.number_input("Household Size", min_value=1, max_value=30)
age = st.number_input("Age of Respondent", min_value=10, max_value=100)
gender = st.selectbox("Gender", ['male', 'female'])
relationship = st.selectbox("Relationship With Head", ['Head of Household', 'Spouse', 'Child', 'Parent', 'Other Relative', 'Other non-relatives'])
marital = st.selectbox("Marital Status", ['married', 'single', 'widowed', 'divorced', 'separated', 'dont know'])
education = st.selectbox("Education Level", ['No formal education', 'Primary education', 'Secondary education', 'Tertiary education', 'Vocational/Specialised training', 'Other/Dont know/RTA'])
job = st.selectbox("Job Type", ['Self employed', 'Government Dependent', 'Formally employed Private', 'Formally employed Government', 'Informally employed', 'Farming and Fishing', 'Remittance Dependent', 'Other Income', 'No Income'])

# --- Predict Button ---
if st.button("Predict Bank Account", use_container_width=True):
    # Create DataFrame
    input_df = pd.DataFrame({
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

    # Apply Label Encoders
    for col in encoders:
        input_df[col] = encoders[col].transform(input_df[col])

    # Predict
    prediction = model.predict(input_df)[0]

    # Result Display
    if prediction == 1:
        st.success("✅ This individual is likely to have **a bank account**.")
    else:
        st.error("❌ This individual is **not likely** to have a bank account.")

# --- Footer ---
st.markdown("<hr style='margin-top: 40px;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Built by Ziggy Greg | <a href='https://github.com/ziggy-greg/bank-account-prediction' target='_blank'>View on GitHub</a></p>", unsafe_allow_html=True)
