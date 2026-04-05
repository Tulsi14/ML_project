# 🎓 Student Performance Indicator 🚀

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

### 🌟 Project Overview
Yeh ek **End-to-End Machine Learning** project hai jo student ki demographic details (gender, ethnicity, parental education, etc.) ke basis par unke **Maths/Exam Scores** ko predict karta hai. Is project ko modular coding standards ke saath banaya gaya hai.

🔗 **Live Demo:** [Streamlit URL](https://mlproject-xhhctxpfmxsv2bhctexp7g.streamlit.app/)

---

## 🛠️ Tech Stack & Tools
- **Language:** Python 🐍
- **Frontend:** Streamlit 🎈 (Converted from Flask)
- **ML Libraries:** Scikit-Learn, XGBoost, CatBoost
- **Data Handling:** Pandas, NumPy
- **Visualization:** Seaborn, Matplotlib
- **Pipeline Management:** Logging, Custom Exception Handling

---

## 🏗️ Project Structure
```text
ml_project/
├── artifacts/           # Model and Preprocessor pickle files
├── notebook/            # Jupyter Notebooks for EDA and Model Training
├── src/
│   ├── components/      # Ingestion, Transformation, Model Trainer
│   ├── pipeline/        # Training and Prediction Pipelines
│   ├── logger.py        # Logging of events
│   └── exception.py     # Custom Exception handling
├── app.py               # Streamlit web application
├── requirements.txt     # List of dependencies
└── setup.py             # Packaging the project