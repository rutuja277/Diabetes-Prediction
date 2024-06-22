# Diabetes Prediction Flask App

This is a Flask web application that predicts whether a person has diabetes or not based on various health metrics. The prediction is made using a Random Forest model.

## Features

- User-friendly interface
- Accepts multiple health parameters as input
- Predicts diabetes status (diabetic or non-diabetic)

## Demo
![Demo Screenshot](Images/Capture.JPG)

## The Dataset

The Pima Indians Diabetes Dataset is a publicly available test dataset widely used for diabetes research and predictive modeling. It contains 768 observations of females of Pima Indian heritage aged 21 years or older. The dataset includes eight medical predictor variables and one target variable.

### Predictor Variables

- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration over 2 hours in an oral glucose tolerance test
- **Blood Pressure**: Diastolic blood pressure (mm Hg)
- **Skin Thickness**: Triceps skinfold thickness (mm)
- **Insulin**: 2-hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)^2)
- **Diabetes Pedigree Function**: A function that scores the likelihood of diabetes based on family history
- **Age**: Age in years

### Target Variable

- **Outcome**: Indicates whether the patient had diabetes (1) or not (0)

This training dataset is particularly useful for testing machine learning algorithms for binary classification tasks.


## Prerequisites

- Python 3.x
- Flask
- Scikit-learn
- Pickle

## Running the App

1. Start the Flask app:
    ```bash
    python app.py
    ```
2. Open your web browser and go to:
    ```
    http://127.0.0.1:5000/
    ```

## Usage

1. Enter the required health metrics into the form:
    - Number of Pregnancies
    - Glucose
    - BloodPressure
    - Skin Thickness
    - Insulin
    - BMI
    - Diabetes Pedigree Function
    - Age
2. Click the "Predict" button.
3. The app will display whether the input indicates a diabetic or non-diabetic status.
