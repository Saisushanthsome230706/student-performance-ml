
# Student Performance Prediction Using Machine Learning

## Project Overview

This project predicts the final academic grade of a student using Machine Learning.

The application is built using Streamlit and can be deployed through GitHub and Streamlit Community Cloud.

## Dataset

Student Performance Dataset - Portuguese course.

- Number of students: 649
- Number of columns: 33
- Target variable: G3
- G3 represents the final student grade.

## Machine Learning Models

The following models were evaluated:

1. Linear Regression
2. Random Forest Regression

## Model Results

| Model | MAE | RMSE | R2 Score |
|---|---:|---:|---:|
| Linear Regression | 0.7651 | 1.2149 | 0.8487 |
| Random Forest | 0.7514 | 1.2456 | 0.8409 |

Linear Regression was selected as the final model based on the overall evaluation results.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## Machine Learning Workflow

Data Collection
→ Data Cleaning
→ Exploratory Data Analysis
→ Data Preprocessing
→ Feature Encoding
→ Train/Test Split
→ Model Training
→ Model Evaluation
→ Model Selection
→ Model Saving
→ Streamlit Deployment

## Streamlit Application

The application allows users to enter student information and predicts:

- Final Grade
- Performance Category

## Performance Categories

- Below 10: Needs Improvement
- 10-13.99: Average
- 14-16.99: Good
- 17-20: Excellent
