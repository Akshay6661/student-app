#Student Performance Prediction App

This is a Student Performance Prediction app that uses machine learning (linear regression) to predict a student's performance based on various factors like study hours, previous scores, and other habits. The app is built with Streamlit for easy deployment and user interaction, and it stores the prediction results in a NoSQL database for future analysis.

Dataset Overview
The dataset contains the following columns:

Hours Studied: The number of hours the student spent studying.
Previous Scores: The student's scores from previous tests.
Extracurricular Activities: A categorical variable indicating whether the student participates in extracurricular activities (e.g., 1 for Yes, 0 for No).
Sleep Hours: The number of hours the student sleeps.
Sample Question Papers Practiced: The number of practice papers the student has gone through.
Performance Index: The predicted or actual performance score based on the above factors.
Key Features
Performance Prediction: Uses a linear regression model to predict the Performance Index based on inputs like hours studied, previous scores, sleep hours, etc.
NoSQL Database Integration: Stores the prediction results in a NoSQL database (e.g., MongoDB, Firebase) for easy tracking and retrieval of past predictions.
Streamlit Deployment: The app is deployed using Streamlit, providing an interactive interface to input data and receive predictions instantly.
Technologies Used
Python: Core programming language used for data analysis and model building.
Pandas: Data manipulation and analysis.
Scikit-learn: For building and applying the linear regression model.
Streamlit: A framework for deploying the app and providing a user-friendly web interface.
NoSQL Database: Used for storing and retrieving prediction data (e.g., MongoDB, Firebase).
