from flask import Flask, render_template, request
from joblib import load
import numpy as np
app = Flask(__name__)

@app.route("/")
def information():
    return render_template('index.html')

@app.route("/result",methods=["GET","POST"])
def result():
    if request.method == 'POST':
        keys = ['age', 'sex',"cp",'trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
        values = np.asarray([float(request.form[key]) for key in keys]).reshape(1,-1)
        prediction = model.predict(values)[0]
        if prediction == 0:
            return render_template('success.html')
        else:
            return render_template('failure.html')
    else:
        return "boom!get"

if __name__ == "__main__":
    model = load('hearthealth.joblib')
    app.run(debug=True)
