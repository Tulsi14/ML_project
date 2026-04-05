# 🎓 Student Performance Indicator 🚀

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

### 🌟 Project Overview
This is an **End-to-End Machine Learning** project designed to predict a student's **Maths/Exam Score** based on various demographic and academic factors such as gender, ethnicity, parental level of education, and test preparation course status. 

The project follows **Modular Coding Standards**, making it scalable, maintainable, and production-ready.

🔗 **Live Demo:** [Insert your Streamlit Cloud URL here]

---

## 🏗️ Project Architecture & Workflow
The project is built using a robust pipeline architecture:
1. **Data Ingestion:** Loads data from source and splits it into Train/Test sets.
2. **Data Transformation:** Handles missing values, scaling, and encoding using a `ColumnTransformer`.
3. **Model Training:** Evaluates multiple algorithms (Linear Regression, XGBoost, CatBoost, etc.) and selects the best performer.
4. **Prediction Pipeline:** A user-friendly Streamlit interface to get real-time predictions.

---

## 🛠️ Tech Stack & Tools
- **Language:** Python 🐍
- **Web Framework:** Streamlit 🎈 (Deployed via Streamlit Cloud)
- **ML Libraries:** Scikit-Learn, XGBoost, CatBoost
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Seaborn, Matplotlib
- **DevOps:** GitHub Actions, Logging, and Custom Exception Handling

---

## 📂 Project Structure
```text
ml_project/
├── artifacts/           # Contains model.pkl and preprocessor.pkl
├── notebook/            # Jupyter Notebooks for EDA and Model Training
├── src/                 # Source code for the project
│   ├── components/      # Ingestion, Transformation, and Trainer modules
│   ├── pipeline/        # Training and Prediction scripts
│   ├── logger.py        # Event logging script
│   ├── utils.py         # Utility functions (Save/Load objects)
│   └── exception.py     # Custom Exception handling
├── app.py               # Main Streamlit application
├── requirements.txt     # Project dependencies
└── setup.py             # Metadata for packaging
