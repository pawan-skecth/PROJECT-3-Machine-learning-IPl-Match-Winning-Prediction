# PROJECT-3-Machine-learning-IPl-Match-Winning-Prediction

## 📌 Introduction  
Cricket is one of the most loved sports worldwide, and predicting match outcomes based on real-time match conditions has always been a challenge. This project aims to **predict the probability of an IPL team's victory** based on match conditions using **machine learning**. The model considers **batting team, bowling team, target, current score, overs, wickets, and city** to provide real-time win probability.  

Using **historical IPL match data**, we have trained a **Logistic Regression model** within a **machine learning pipeline** to predict match outcomes. The project also includes an **interactive Gradio-based web application** where users can input live match details and get **winning probabilities for both teams**.  

---

## 📂 Dataset  
We used two IPL datasets:  

1. **matches.csv** – Contains information about IPL matches, such as teams, venue, winner, and match ID.  
2. **deliveries.csv** – Contains ball-by-ball data of IPL matches, including runs, wickets, and match ID.  

After preprocessing, the data is structured to focus on **match-level statistics** and the **second innings' chase scenario**.  

---

## 🛠️ Technologies Used  

- **Python** – Core programming language  
- **Pandas, NumPy** – Data manipulation and preprocessing  
- **Scikit-Learn** – Machine learning model training  
- **Matplotlib, Seaborn** – Data visualization  
- **Gradio** – Web interface for real-time prediction  
- **Pickle** – Model serialization  

---

## 🔍 Exploratory Data Analysis (EDA)  

We performed **EDA** to clean and analyze the dataset, ensuring it is suitable for machine learning. Key steps:  

✔ **Data Cleaning:** Handled missing values and standardized team names.  
✔ **Feature Engineering:** Created key features like `runs_left`, `balls_left`, `wickets_remaining`, `current run rate (CRR)`, and `required run rate (RRR)`.  
✔ **Data Filtering:** Focused on second innings only, removed rain-affected matches (DLS method applied).  
✔ **Visualizations:**  
   - **Win percentage of teams**  
   - **Distribution of runs per over**  
   - **Wickets fall pattern in second innings**  

---

## 🎯 Model Training  

We trained a **Logistic Regression model** within a **Pipeline** that includes:  

1️⃣ **One-Hot Encoding** for categorical variables (`batting_team`, `bowling_team`, `city`).  
2️⃣ **Feature Scaling** for numerical variables (`runs_left`, `balls_left`, `wickets`, etc.).  
3️⃣ **Logistic Regression Model** for probability-based classification.  

🔹 **Training Set Split:** 80% training, 20% testing  
🔹 **Model Evaluation:** **Accuracy = 78%**  

---

## 📊 Features Used in Model  

- **Batting Team** 🏏  
- **Bowling Team** 🎯  
- **City (Venue)** 🏟️  
- **Target Score** 🎯  
- **Current Score** 🔢  
- **Overs Completed** ⏳  
- **Wickets Fallen** ❌  
- **Runs Left to Win** 🔢  
- **Balls Left** ⏳  
- **Current Run Rate (CRR)** 📈  
- **Required Run Rate (RRR)** 📉  

These features help the model predict **real-time winning probability** for the batting team.  

---

## 🎮 Web App using Gradio  

We built an **interactive web app** using **Gradio**, where users can enter match details and get **winning probabilities**.  

### 🔹 **How It Works:**  
1️⃣ Select **Batting Team** and **Bowling Team**.  
2️⃣ Choose **Match Venue (City)**.  
3️⃣ Enter **Target Score**, **Current Score**, **Overs Completed**, and **Wickets Fallen**.  
4️⃣ Click **"Predict Probability"** to get the **win probabilities** of both teams.  

### 🖥️ **User Interface (UI)**  
✅ Dropdowns for **teams and city selection**  
✅ Number inputs for **target, current score, overs, wickets**  
✅ **Real-time probability prediction** on button click  

---

## 📁 Model Deployment  

1️⃣ **Model Serialization** – Saved using **Pickle (`pipe.pkl`)**  
2️⃣ **Gradio App** – Runs locally and can be deployed on cloud platforms  

---

## 🚀 How to Run the Project  

### 🖥️ Install Dependencies  
```bash
pip install pandas numpy scikit-learn gradio pickle-mixin
```

### 📌 Run the Web App  
```bash
python app.py
```
or use  
```bash
demo.launch()
```

---

## 🏆 Conclusion  

This project successfully predicts **IPL match-winning probabilities** in real-time based on various match conditions. By using **Logistic Regression with feature engineering**, we achieved **high accuracy** and created an **interactive Gradio-based web app** for predictions.  

### 📌 Key Takeaways:  
✔ Machine Learning can provide **real-time predictions** for sports analytics.  
✔ **Feature engineering** plays a crucial role in improving accuracy.  
✔ **Gradio** makes it easy to deploy an ML model as a web app.  
✔ The model can be further **improved** using **advanced algorithms** like XGBoost or Neural Networks.  

---

## 📜 Future Improvements  

🔹 **Use Advanced ML Models** – Try **Random Forest, XGBoost** for better accuracy.  
🔹 **Live IPL Data Integration** – Fetch real-time match data for live predictions.  
🔹 **Enhance Web UI** – Improve Gradio app design for better user experience.  
🔹 **Deploy Online** – Host the model on **Hugging Face, Streamlit, or Flask-based web servers**.  


