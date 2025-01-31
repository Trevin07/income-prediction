from flask import Flask, request, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

dataset = pd.read_csv('data.csv')
dataset.dropna(inplace=True)

label_encoder_workclass = LabelEncoder()
label_encoder_education = LabelEncoder()
label_encoder_country = LabelEncoder()

dataset['workclass'] = label_encoder_workclass.fit_transform(dataset['workclass'])
dataset['education'] = label_encoder_education.fit_transform(dataset['education'])
dataset['country'] = label_encoder_country.fit_transform(dataset['country'])

X = dataset[['age', 'education', 'workclass', 'country']]
y = dataset['salary']

model = LinearRegression()
model.fit(X, y)

sector_salary_multipliers = {
    'IT': 1.2,
    'Finance': 1.15,
    'Healthcare': 1.1,
    'Education': 0.9,
    'Manufacturing': 1.0,
    'Other': 1.0
}

sector_list = ['IT', 'Finance', 'Healthcare', 'Education', 'Manufacturing', 'Other']

education_list = label_encoder_education.classes_
workclass_list = label_encoder_workclass.classes_
country_list = label_encoder_country.classes_

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        age = float(request.form['age'])
        education = int(request.form['education'])
        workclass = int(request.form['workclass'])
        country_name = request.form['country']
        sector_name = request.form.get('sector', 'Other')

        country = label_encoder_country.transform([country_name])[0]
        sector_multiplier = sector_salary_multipliers.get(sector_name, 1.0)

        base_prediction = model.predict([[age, education, workclass, country]])[0]
        final_prediction = base_prediction * sector_multiplier * 10000

        prediction = round(final_prediction, 2)

    return render_template('index.html', prediction=prediction,
                           education_list=education_list, workclass_list=workclass_list,
                           country_list=country_list, sector_list=sector_list)

if __name__ == '__main__':
    app.run(debug=True)
