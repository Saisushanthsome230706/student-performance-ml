
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("student_performance_linear_regression.pkl")

# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# Title
st.title("🎓 Student Performance Prediction")

st.write(
    "Enter the student's information to predict the final grade."
)

st.divider()

# Student Information
st.header("👤 Student Information")

col1, col2, col3 = st.columns(3)

with col1:
    school = st.selectbox("School", ["GP", "MS"])
    sex = st.selectbox("Gender", ["M", "F"])
    age = st.number_input("Age", 15, 22, 17)
    address = st.selectbox("Address", ["U", "R"])

with col2:
    famsize = st.selectbox("Family Size", ["GT3", "LE3"])
    Pstatus = st.selectbox("Parent Status", ["T", "A"])
    Medu = st.slider("Mother Education", 0, 4, 2)
    Fedu = st.slider("Father Education", 0, 4, 2)

with col3:
    guardian = st.selectbox(
        "Guardian",
        ["mother", "father", "other"]
    )

    reason = st.selectbox(
        "Reason for Choosing School",
        ["course", "home", "reputation", "other"]
    )

    traveltime = st.slider("Travel Time", 1, 4, 1)
    studytime = st.slider("Study Time", 1, 4, 2)


# Family Information
st.header("👨‍👩‍👧 Family Information")

col1, col2 = st.columns(2)

with col1:
    Mjob = st.selectbox(
        "Mother's Job",
        ["teacher", "health", "services", "at_home", "other"]
    )

with col2:
    Fjob = st.selectbox(
        "Father's Job",
        ["teacher", "health", "services", "at_home", "other"]
    )


# Academic Information
st.header("📚 Academic Information")

col1, col2, col3 = st.columns(3)

with col1:
    failures = st.slider(
        "Previous Failures",
        0,
        3,
        0
    )

    absences = st.number_input(
        "Number of Absences",
        min_value=0,
        max_value=100,
        value=4
    )

with col2:
    G1 = st.slider(
        "First Period Grade (G1)",
        0,
        20,
        12
    )

    G2 = st.slider(
        "Second Period Grade (G2)",
        0,
        20,
        13
    )

with col3:
    higher = st.selectbox(
        "Wants Higher Education?",
        ["yes", "no"]
    )

    internet = st.selectbox(
        "Internet Access?",
        ["yes", "no"]
    )


# Support and Activities
st.header("🏫 Support & Activities")

col1, col2, col3 = st.columns(3)

with col1:
    schoolsup = st.selectbox(
        "School Support",
        ["yes", "no"]
    )

    famsup = st.selectbox(
        "Family Support",
        ["yes", "no"]
    )

with col2:
    paid = st.selectbox(
        "Paid Extra Classes",
        ["yes", "no"]
    )

    activities = st.selectbox(
        "Extra Activities",
        ["yes", "no"]
    )

with col3:
    nursery = st.selectbox(
        "Attended Nursery",
        ["yes", "no"]
    )

    romantic = st.selectbox(
        "Romantic Relationship",
        ["yes", "no"]
    )


# Social and Health
st.header("❤️ Social & Health")

col1, col2, col3 = st.columns(3)

with col1:
    famrel = st.slider(
        "Family Relationship",
        1,
        5,
        4
    )

    freetime = st.slider(
        "Free Time",
        1,
        5,
        3
    )

with col2:
    goout = st.slider(
        "Going Out",
        1,
        5,
        3
    )

    Dalc = st.slider(
        "Workday Alcohol Consumption",
        1,
        5,
        1
    )

with col3:
    Walc = st.slider(
        "Weekend Alcohol Consumption",
        1,
        5,
        1
    )

    health = st.slider(
        "Health",
        1,
        5,
        4
    )


# Create input DataFrame
input_data = pd.DataFrame({
    "school": [school],
    "sex": [sex],
    "age": [age],
    "address": [address],
    "famsize": [famsize],
    "Pstatus": [Pstatus],
    "Medu": [Medu],
    "Fedu": [Fedu],
    "Mjob": [Mjob],
    "Fjob": [Fjob],
    "reason": [reason],
    "guardian": [guardian],
    "traveltime": [traveltime],
    "studytime": [studytime],
    "failures": [failures],
    "schoolsup": [schoolsup],
    "famsup": [famsup],
    "paid": [paid],
    "activities": [activities],
    "nursery": [nursery],
    "higher": [higher],
    "internet": [internet],
    "romantic": [romantic],
    "famrel": [famrel],
    "freetime": [freetime],
    "goout": [goout],
    "Dalc": [Dalc],
    "Walc": [Walc],
    "health": [health],
    "absences": [absences],
    "G1": [G1],
    "G2": [G2]
})


# Prediction
st.divider()

if st.button(
    "🎯 Predict Final Grade",
    type="primary",
    use_container_width=True
):

    prediction = model.predict(input_data)

    predicted_grade = float(prediction[0])

    # Keep grade between 0 and 20
    predicted_grade = max(
        0,
        min(20, predicted_grade)
    )

    # Performance category
    if predicted_grade < 10:
        category = "Needs Improvement"
    elif predicted_grade < 14:
        category = "Average"
    elif predicted_grade < 17:
        category = "Good"
    else:
        category = "Excellent"

    # Display result
    st.subheader("🎯 Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Predicted Final Grade",
            f"{predicted_grade:.2f} / 20"
        )

    with col2:
        st.metric(
            "Performance",
            category
        )

    if predicted_grade < 10:
        st.warning(
            "The student may require additional academic support."
        )

    elif predicted_grade < 14:
        st.info(
            "The student is predicted to have average performance."
        )

    elif predicted_grade < 17:
        st.success(
            "The student is predicted to have good performance."
        )

    else:
        st.success(
            "The student is predicted to have excellent performance."
        )


# About
st.divider()

st.subheader("📊 About This Project")

st.write(
    """
    This application uses Machine Learning to predict the
    final academic grade of a student.

    Dataset: Student Performance (Portuguese course)

    Target variable: G3

    Machine Learning Algorithm: Linear Regression

    Evaluation Metrics: MAE, RMSE and R² Score
    """
)
