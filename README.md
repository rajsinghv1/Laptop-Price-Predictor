# 💻 Laptop Price Predictor

An end-to-end Machine Learning project that predicts laptop prices based on hardware specifications using regression and ensemble learning techniques. The project includes a Streamlit-based user interface for local execution and real-time price prediction.

---

## 📄 Project Demo

You can view the complete demo of the application here:

🔗 **Demo PDF:**  
https://github.com/rajsinghv1/Laptop-Price-Predictor/blob/main/demo.pdf

📌 The demo showcases:
- Streamlit user interface
- Laptop feature selection
- Price prediction output
- Complete project workflow

---

## 🔍 Problem Statement

Laptop prices depend on multiple factors such as brand, RAM, processor, storage, display quality, and operating system.  
This project aims to build a machine learning model that accurately predicts laptop prices based on user-selected specifications.

---

## 📁 Dataset

- **Source:** Kaggle Laptop Dataset  
- **Total Records:** 1300+  
- **Target Variable:** Price  

### Features:
- Company  
- TypeName  
- RAM  
- Weight  
- Touchscreen  
- IPS Display  
- Screen Resolution (converted to PPI)  
- CPU Brand  
- HDD  
- SSD  
- GPU Brand  
- Operating System  

---

## 🛠️ Technologies Used

- Python  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- Streamlit  
- Pickle  

---

## ⚙️ Project Workflow

1. Data cleaning and preprocessing  
2. Feature engineering (PPI calculation)  
3. Encoding categorical features  
4. Model training using regression techniques  
5. Model evaluation using R² Score and MAE  
6. Ensemble learning for better performance  
7. Model saving using Pickle  
8. Local execution using Streamlit  

---

## 🤖 Machine Learning Models Used

- Linear Regression  
- Ridge & Lasso Regression  
- K-Nearest Neighbors Regressor  
- Decision Tree Regressor  
- Random Forest Regressor  
- Extra Trees Regressor  
- Gradient Boosting Regressor  
- XGBoost Regressor  
- **Voting Regressor (Final Model)**  

---

## 📊 Model Performance

- **Best Model:** Voting Regressor  
- **R² Score:** ~0.88  
- **MAE:** ~0.15  

The ensemble approach improved accuracy and reduced prediction error.

---

## 🚀 Streamlit Application (Local Run Only)

The Streamlit app allows users to:
- Select laptop specifications
- Automatically compute PPI
- Predict laptop prices instantly

### ▶️ How to Run the App Locally

```bash
pip install -r requirements.txt
streamlit run app.py
