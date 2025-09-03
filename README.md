# Insurance_multilinear_project

🏥 Insurance Cost Prediction using Multiple Linear Regression

📌 Overview :

The Insurance Cost Prediction project predicts an individual's medical insurance charges based on demographic and health-related features. Using a Multiple Linear Regression (MLR) model, the project analyzes several independent variables to accurately estimate healthcare costs.


Key Highlights :

📈 Built a regression-based prediction model

🧹 Cleaned and preprocessed real-world insurance data

🔍 Performed EDA (Exploratory Data Analysis)

📊 Evaluated model performance with R² score and RMSE

🐳 Dockerized deployment for real-time predictions


📂 Dataset :

* Source :[Kaggle - Medical Insurance Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)

* Shape : 1339 rows × 7 features

* Features :

   age → Age of the individual

   sex → Gender (male/female)

   bmi → Body Mass Index

   children → Number of dependents

   smoker → Smoking status (yes/no)

   region → Residential region

   charges → Target → Annual medical cost in USD


  🧠 Tech Stack :

* Language → Python 

* ML Algorithm → Multiple Linear Regression

* Libraries → Pandas, NumPy, Scikit-learn

* Visualization → Matplotlib, Seaborn

* Deployment → Docker


🚀 Features :

✅ Data Cleaning & Preprocessing

✅ One-Hot Encoding for Categorical Variables

✅ Multiple Linear Regression Model Building

✅ Model Evaluation using R² & RMSE

✅ Interactive Dockerized Deployment


📊 Model Evaluation :

| Metric                              | Score |
| ----------------------------------- | ----- |
| **R² Score**                        |  80%  |
| **RMSE**                            | 4500  |


🌐 Deployment (Dockerized) :

1️⃣ Build Docker Image :

docker build -t ml-insurance-app .

2️⃣ Run Docker Container :

docker run -d -p 5000:5000 ml-insurance-app

3️⃣ Access the Application :http://localhost:5000


🤝 Contribution :

Contributions are welcome! 🎉, If you'd like to improve this project:

- Fork the repository 🍴
  
- Create a feature branch

- Submit a pull request 🚀


👨‍💻 Author :

Abinnu John Peter.P

📧 Email: abinnu75@gmail.com

🔗 LinkedIn : www.linkedin.com/in/abinnu
