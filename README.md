# 🔍 SONAR Mine and Rock Prediction

A Machine Learning-powered web application that predicts whether a sonar reading reflects from a **Mine** or a **Rock**, based on 60 numerical features extracted from the UCI Sonar Dataset.

---

## 📌 Features

✅ Input 60 sonar readings (comma-separated)  
✅ Real-time prediction using trained ML model  
✅ Displays **prediction result** (Mine / Rock)  
✅ Shows **confidence score (%)**  
✅ Fully integrated **Flask backend + HTML/CSS frontend**  
✅ Scalable for cloud deployment (Render, Netlify, etc.)

---

## 🧠 Tech Stack

- **Machine Learning**: `Logistic Regression` trained on sonar data  
- **Backend**: Python `Flask`, `Joblib` for model loading  
- **Frontend**: HTML, CSS, JavaScript (Vanilla)  
- **Model Training**: Google Colab  

---

## 🛠️ Installation

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
