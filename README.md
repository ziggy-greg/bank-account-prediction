

# Financial Inclusion Predictor

This Streamlit web app predicts whether an individual is likely to have access to a bank account based on demographic features.

![App Screenshot](https://user-images.githubusercontent.com/your-screenshot-placeholder.png)

## Demo
Try it live: [Streamlit App](https://your-deployment-url.streamlit.app)

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Acknowledgements](#acknowledgements)

---

## About the Project

Many individuals in developing regions still lack access to financial services. This app uses a machine learning model trained on demographic data to predict if a person is likely to own a bank account.

It is built with:
- **Scikit-learn** for machine learning
- **Streamlit** for a sleek UI
- **Pandas** for data handling

## Features

- User-friendly dropdowns to input personal data
- Real-time prediction with visual feedback
- Powered by a Random Forest Classifier
- Clean and responsive design
- Deployable via [Streamlit Cloud](https://streamlit.io/cloud)

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/ziggy-greg/bank-account-prediction.git
cd bank-account-prediction

	2.	Install dependencies

pip install -r requirements.txt

	3.	Run the app

streamlit run app.py

How to Use
	1.	Fill in the demographic details using the dropdowns.
	2.	Click Predict Bank Account.
	3.	The app will display whether the person is likely to own a bank account.

Technologies Used
	•	Python
	•	Scikit-learn
	•	Pandas
	•	Streamlit
	•	Git & GitHub

Project Structure

├── app.py                   # Streamlit web app
├── finances_model.pkl       # Trained ML model
├── label_encoder.pkl        # Encoded labels for categorical features
├── Financial_Inclusion_dataset.csv
├── requirements.txt
└── .gitignore

Acknowledgements
	•	Dataset sourced from Financial Inclusion in Africa Dataset
	•	App built and maintained by Ziggy Greg

Built with love by Ziggy Greg

