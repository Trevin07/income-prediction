# Income Prediction Project

This project predicts the monthly salary of individuals based on various attributes such as age, education level, work class, country, and sector. The model outputs a predicted salary value based on these features by a model which was trained by using over 26,000 thousand records/samples.

---
Screenshot of the Web Application

![Screenshot](./screensot.jpg)

---

## Project Overview

The goal of this project is to predict the monthly salary of an individual using machine learning models. The following features are considered:

- **Age**: The age of the individual.
- **Education**: The highest level of education attained (e.g., Bachelor’s, High School).
- **Workclass**: The type of employment (e.g., Private, Government).
- **Country**: The country of residence of the individual.
- **Sector**: The industry or sector in which the individual is employed.

The model provides a predicted monthly salary based on these inputs.

---

## Models Used

The following machine learning models were used in this project:

- **Logistic Regression**: A statistical model for regression tasks.
- **Support Vector Machine (SVM)**: A model that uses hyperplanes to classify and predict values.
- **Neural Networks**: A deep learning model designed to capture complex relationships in data.

---

## Data

The **Adult Census dataset** is used, which contains demographic information and income data. The key features in the dataset include age, education, occupation, and income.

---

## Technologies Used

- **Python**: The primary language used for training the models and data processing.
- **Scikit-learn**: A library used to implement the machine learning models.
- **TensorFlow/Keras**: Frameworks used for building and training neural networks.
- **Pandas**: A library used for data manipulation and analysis.
- **NumPy**: A library used for numerical computations.
- **Flask**: A web framework used to deploy the trained models.
- **HTML/CSS**: For building the web interface to interact with the model.

---

## How to Run

 1. Clone the repository:

git clone https://github.com/Trevin07/income-prediction.git

2. Install dependencies:

pip install -r requirements.txt

3. Train the model:
Run the script to train the machine learning models:

python income.ipynb

4. Start the web application:
Run the Flask web application:
python app.py

5. Access the web app:
Navigate to http://127.0.0.1:5000 in your browser to use the model.

Features
Salary Prediction: Predict the monthly salary based on inputs like age, education, workclass, country, and sector.
Web Interface: A simple and intuitive interface that allows users to input their data and get salary predictions.

License
This project is licensed under the MIT License - see the LICENSE file for details.





