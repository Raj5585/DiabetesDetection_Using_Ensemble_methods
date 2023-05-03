from flask import Flask, request, render_template
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
LogisticModel = pickle.load(open("LogisticModel.pkl", "rb"))
RandomForestModel = pickle.load(open("RandomForestModel.pkl", "rb"))
SvmModel = pickle.load(open("SvmModel.pkl", "rb"))
mean_std = pickle.load(open("Mean_std.pkl", "rb"))


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form
    input_data = request.form.to_dict()
    for key in input_data:

        if input_data[key] == '':
            input_data[key] = 0
        else:
            input_data[key] = float(input_data[key])

    features = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Pregnancies']

    values = np.array([input_data.get(i) for i in features])
    values_normalized = (values - mean_std["mean"])/mean_std["sd"]

    randomForestoutput = RandomForestModel.predict([values_normalized])
    logisticoutput = LogisticModel.predict([values_normalized])
    svmoutput = SvmModel.predict([values_normalized])

    # perform majority voting
    if (randomForestoutput + logisticoutput + svmoutput) >= 2:
        # yes diabetes
        return "Sad"
    else:
         # no diabetes
        return "Happy"

if __name__ == '__main__':
    app.run(debug=True)
