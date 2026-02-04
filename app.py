from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

# Create Flask app
app = Flask(__name__)

# Load model and feature list
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "student_model.pkl"))
model_features = joblib.load(os.path.join(BASE_DIR, "model_features.pkl"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Collect input data
    data = {
        "G1": int(request.form["G1"]),
        "G2": int(request.form["G2"]),
        "studytime": int(request.form["studytime"]),
        "failures": int(request.form["failures"]),
        "health": int(request.form["health"]),
        "freetime": int(request.form["freetime"]),
        "Dalc": int(request.form["Dalc"]),
        "Walc": int(request.form["Walc"]),
        "famsup": request.form["famsup"],
        "schoolsup": request.form["schoolsup"],
        "paid": request.form["paid"],
        "internet": request.form["internet"],
        "activities": request.form["activities"]
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([data])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=model_features, fill_value=0)

    # Predict
    prediction = model.predict(input_df)[0]
    prediction = round(float(prediction), 2)

    # Grade category
    if prediction >= 15:
        category = "Excellent Performance "
    elif prediction >= 10:
        category = "Average Performance "
    else:
        category = "At Risk " \
        ""

    return render_template(
        "index.html",
        prediction=prediction,
        category=category,
        g2=data["G2"]     # this for chart 
    )


if __name__ == "__main__":
    app.run(debug=True)
