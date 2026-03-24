# 🎓 EduPulse – Student Performance Prediction System
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-green)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

## 🔎 TL;DR (Quick Summary)
- 📌 End-to-end Machine Learning project (EDA → Modeling → Deployment)
- 🎯 Goal: Predict student final grades (G3) by analysing (G2)
- 🏆 Best Model: Decision Tree Regressor (R² ≈ 0.78)
- 🌐 Deployed using Flask with interactive UI
- 🛠 Tech: Python, Pandas, Scikit-learn, Flask

EduPulse is an end-to-end **Machine Learning project** designed to predict a student’s final academic grade (**G3**) using historical academic performance, behavioral, and lifestyle factors.  
The project combines **data analysis, machine learning modeling, and a Flask-based web application** to demonstrate a real-world ML pipeline.

---

## 🚀 Project Overview

Educational institutions often identify academic risk too late. EduPulse aims to provide an **early performance prediction system** that can assist educators in understanding student outcomes and enabling timely academic intervention.

The system:
- Analyzes student data using EDA
- Trains multiple regression models
- Selects the best-performing model
- Deploys predictions via a Flask web interface

---

## 🎯 Problem Statement

Manual evaluation of student performance is:
- Subjective  
- Time-consuming  
- Reactive rather than proactive  

This project uses **machine learning** to predict final grades early, helping identify students who may need additional support.

---

## 🧠 Key Features

-Conducted in-depth Exploratory Data Analysis (EDA) to uncover patterns, trends, and key business insights
-Applied feature engineering and selection techniques (correlation analysis, feature importance) to improve model performance
-Built and compared multiple regression models (e.g., Linear Regression, Random Forest, XGBoost) for optimal prediction accuracy
-Evaluated models using robust performance metrics such as MAE, RMSE, and R² to ensure reliability
-Developed a Flask-based interactive web application for real-time predictions and user input handling
-Visualized predicted vs actual results using graphs to assess model accuracy and performance
-Implemented end-to-end ML pipeline from data preprocessing to deployment

---

## 📊 Dataset Information

- **Dataset:** Student Performance Dataset  
- **Records:** ~300–400 students  
- **Features:** 33  
- **Target Variable:** `G3` (Final Grade)

### Feature Categories:
- Academic: `G1`, `G2`, `failures`, `studytime`
- Behavioral: `absences`, `activities`, `freetime`
- Social & Lifestyle: `internet`, `paid`, `health`, `alcohol`

---

## 🧪 Exploratory Data Analysis (EDA)

Key insights from EDA:
- **G1 and G2** are the strongest predictors of G3
- Study time has a moderate positive effect
- Absences negatively impact performance but include outliers
- Behavioral and lifestyle features provide additional context

Visualizations used:
- Histograms
- Scatter plots
- Box plots
- Correlation heatmaps

---

## 🤖 Machine Learning Models Used

Three regression models were trained and evaluated:

### 1️⃣ Linear Regression
- Baseline model
- High interpretability
- Assumes linear relationships

### 2️⃣ Decision Tree Regressor ✅ (Best Model)
- Captures non-linear relationships
- Provides feature importance
- Achieved the best balance of accuracy and explainability

### 3️⃣ Random Forest Regressor
- Ensemble model
- Reduces variance
- Requires further tuning for small datasets

---

## 📈 Model Performance

| Model | MAE | RMSE | R² |
|-----|-----|------|----|
| Linear Regression | ~1.40 | ~2.19 | ~0.76 |
| Decision Tree Regressor | ~1.38 | ~2.11 | ~0.78 |
| Random Forest Regressor | ~1.52 | ~2.40 | ~0.71 |

**Decision Tree Regressor** was selected as the final model.

---

## 🌐 Flask Web Application

The project includes a **Flask-based web interface** where users can:
- Enter academic and behavioral inputs
- Get real-time prediction of final grade (G3)
- View a visual comparison between G2 and predicted G3

```markdown
### 📸 Application Preview
![EduPulse UI](screenshots/app_ui.png)


```
---

## 🛠 Tech Stack

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
- **Web Framework:** Flask  
- **Environment:** Jupyter Notebook

---
 ## 📂 Project Structure

```text
EduPulse/
│
├── app.py
│   └── Flask application entry point for running the web app
│
├── data/
│   └── Contains cleaned and processed student datasets used for training
│
├── Notebooks/
│   ├── Notebook_01_Data_Loading.ipynb
│   ├── Notebook_02_Data_Understanding.ipynb
│   ├── Notebook_03_Data_Cleaning.ipynb
│   ├── Notebook_04_Exploratory_Data_Analysis.ipynb
│   ├── Notebook_05_Model_Training.ipynb
│   └── Notebook_06_Model_Interpretation.ipynb
│
├── templates/
│   └── HTML templates used by the Flask application
│
├── Outputs/
│   └── Generated plots, evaluation results, and intermediate outputs
│
├── Screenshots/
│   └── UI screenshots and visual assets for documentation
│
├── internship_Weekly_reports/
│   └── Weekly internship progress reports
│
├── anaconda_projects/
│   └── Environment-specific or experimentation-related files
│
├── student_model.pkl
│   └── Trained machine learning model (Decision Tree Regressor)
│
├── model_features.pkl
│   └── Serialized feature list used during prediction
│
├── environment.yml
│   └── Conda environment configuration file
│
├── requirements.txt
│   └── Python dependencies required to run the project
│
├── Edupulse_project_demonstration.mp4
│   └── Screen-recorded project demonstration video
│
└── README.md
    └── Project documentation

```
---

## 🔮 Future Improvements

- Hyperparameter tuning using GridSearch or RandomSearch
- Cross-validation for more robust evaluation
- Inclusion of psychological and attendance-quality metrics
- Deployment on cloud platforms (AWS / Render / Heroku)

---

## 🙏 Acknowledgements

- Student Performance Dataset
- Scikit-learn & Pandas documentation
- Netleap Internship Program

---

## ▶️ How to Run the Project Locally

1. Clone the repository:
```bash
git clone https://github.com/yourusername/EduPulse.git
cd EduPulse
pip install -r requirements.txt
http://127.0.0.1:5000
```

## 📘 Learning Outcomes

- Built a complete ML pipeline from data analysis to deployment
- Understood model selection and evaluation trade-offs
- Learned to deploy ML models using Flask
- Improved ability to explain ML results clearly



## 📬 Contact

**Author:** Om Thombare
**Contributers:** Sameer Bhor ,Ramessh Rathod
**Domain:** Data Science / Machine Learning  

Feel free to connect or provide feedback!


