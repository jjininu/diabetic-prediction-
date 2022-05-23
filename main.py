from flask import Flask, render_template,request
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsClassifier

import requests





app  = Flask(__name__)


@ app.route('/',methods = ["GET","POST"])
def home_page():
    return render_template('index.html')

@ app.route("/outcome",methods = ["GET","POST"])
def outcome():
    Pregnancies = request.form["Pregnancies"]
    Glucose = request.form["Glucose"]
    BloodPressure= request.form["BloodPressure"]
    SkinThickness = request.form["SkinThickness"]
    Insulin = request.form["Insulin"]
    BMI= request.form["BMI"]
    DiabetesPedigreeFunction = request.form["DiabetesPedigreeFunction"]
    Age= request.form["Age"]
    features = [float(x) for x in request.form.values()]
    arr  = np.array(features)
    arrs = arr.reshape(1, -1)
    loaded_model = pickle.load(open("model.pkl", 'rb'))
    predict  =loaded_model.predict(arrs)
    if predict[0] == 1:
        return render_template("index.html", prediction_text="There is 80 % chance are you are diabeic")
    else:
        return render_template("index.html", prediction_text="There is 80 % chance are you are not diabeic")




if __name__ == '__main__':
    app.run(debug=True)
