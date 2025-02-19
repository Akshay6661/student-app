# Student Performance Prediction App
This is a Student Performance Prediction app that uses machine learning (linear regression) to predict a student's performance based on various factors like study hours, previous scores, and other habits. The app is built with Streamlit for easy deployment and user interaction, and it stores the prediction results in a NoSQL database for future analysis.

## Dataset Overview
The dataset contains the following columns:

**Hours Studied**: The number of hours the student spent studying.  

**Previous Scores**: The student's scores from previous tests.  

**Extracurricular Activities**: A categorical variable indicating whether the student participates in extracurricular activities (e.g., 1 for Yes, 0 for No).  

**Sleep Hours**: The number of hours the student sleeps.  

**Sample Question Papers Practiced**: The number of practice papers the student has gone through.  

**Performance Index**: The predicted or actual performance score based on the above factors.  

## Key Features
**Performance Prediction**: Uses a linear regression model to predict the Performance Index based on inputs like hours studied, previous scores, sleep hours, etc.  

**NoSQL Database Integration**: Stores the prediction results in a NoSQL database (e.g., MongoDB, Firebase) for easy tracking and retrieval of past predictions.  

**Streamlit Deployment**: The app is deployed using Streamlit, providing an interactive interface to input data and receive predictions instantly.  

## Technologies Used
**Python**: Core programming language used for data analysis and model building.  

**Pandas**: Data manipulation and analysis.  

**Scikit-learn**: For building and applying the linear regression model.  

**Streamlit**: A framework for deploying the app and providing a user-friendly web interface.  

**NoSQL Database**: Used for storing and retrieving prediction data (e.g., MongoDB).  


# Installation
## 1. Clone the repository
bash  

Copy

git clone https://github.com/Akshay6661/student-app.git
cd student-app  

## 2. Install dependencies
Ensure you have Python installed, then install the necessary libraries.

bash  

Copy

**pip install -r requirements.txt**

If you don't have a requirements.txt file, you can install libraries individually with:

bash

Copy

**pip install pandas scikit-learn streamlit pymongo**

Note: If you're using a different NoSQL database (e.g., Firebase), replace pymongo with the appropriate library.

## 3. Set up the database (if needed)
If you're using MongoDB:  


Ensure you have MongoDB installed and running locally or use a cloud-based MongoDB service like MongoDB Atlas. 

Replace the database credentials in your code with your own.

## How to Run the App

Launch the app: Once everything is set up, you can start the Streamlit app by running the following command:

bash

Copy

streamlit run app.py

**Input Data**: Enter values for "Hours Studied," "Previous Scores," "Extracurricular Activities," "Sleep Hours," and "Sample Question Papers Practiced" through the app interface.


**Prediction**: After entering the data, click Predict to get the predicted Performance Index.

**View Results**: The prediction is displayed on the screen, and the result is also saved to the NoSQL database.

## Contributing

Feel free to fork the repository, make changes, and create pull requests. If you'd like to contribute, follow these steps:

Fork this repository.

Clone your fork.

Create a new branch: git checkout -b feature-branch

Make your changes and commit: git commit -am 'Add new feature'

Push to your fork: git push origin feature-branch

Create a pull request!
