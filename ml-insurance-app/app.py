from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__, template_folder='template')

# Load trained model
model = joblib.load("model/multilinear.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form inputs
    age = float(request.form['age'])
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    sex = int(request.form['sex'])       # 1 = Male, 0 = Female
    smoker = int(request.form['smoker']) # 1 = Yes, 0 = No

    # Region one-hot encoding
    region = request.form['region']
    region_northwest = 0
    region_southeast = 0
    region_southwest = 0

    if region == 'northwest':
        region_northwest = 1
    elif region == 'southeast':
        region_southeast = 1
    elif region == 'southwest':
        region_southwest = 1
    # northeast is baseline (all zeros)

    # Prepare input for prediction
    features = np.array([[age, bmi, children, sex, smoker,
                          region_northwest, region_southeast, region_southwest]])

    prediction = model.predict(features)[0]

    return render_template("index.html", prediction_text=f"Predicted Insurance Charges: ₹{prediction:.2f}")

if __name__ == "__main__":
    app.run(debug=True)

