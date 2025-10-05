# 🕵️‍♂️ Fraud Detection System

A machine learning pipeline designed to detect fraudulent financial transactions in real time.  
Built with **Python, Scikit-learn, LightGBM, Streamlit, Pandas, NumPy**, and data visualization libraries.

---

## 🚀 Features
- **Data Preprocessing & Balancing**
  - Handled class imbalance using **SMOTE** and undersampling techniques.
  - Cleaned and normalized transactional datasets for model readiness.

- **Feature Engineering**
  - Extracted **temporal patterns** (hour-of-day, day-of-week trends).
  - Incorporated **geolocation features** using `geopy` to improve contextual accuracy.

- **Model Training**
  - Tested multiple algorithms: Logistic Regression, Random Forest, XGBoost, LightGBM.
  - Achieved **~92% classification accuracy** with strong recall on fraud cases.
  - Hyperparameter tuning for improved performance and generalization.

- **Evaluation**
  - Metrics: **Precision, Recall, F1-score, ROC-AUC, Confusion Matrix**.
  - Balanced focus on minimizing false negatives (missed fraud) while maintaining precision.

- **Interactive Web App**
  - Deployed with **Streamlit** for real-time fraud detection.
  - Users can upload transaction data (CSV) and receive predictions + visualized insights.

---

## 🛠️ Tech Stack
- **Languages**: Python
- **Libraries**: Scikit-learn, LightGBM, Pandas, NumPy, Matplotlib, Seaborn
- **Deployment**: Streamlit
- **Other Tools**: Geopy (location features), Git for version control

---

## 📊 Example Workflow
1. Upload a CSV of financial transactions.
2. Backend preprocesses and balances the data.
3. Model predicts whether each transaction is **Fraudulent** or **Legitimate**.
4. Results visualized via charts and metrics on the Streamlit dashboard.

---

## 📈 Results
- **92% accuracy** across test datasets.
- Strong **recall** (catching fraudulent cases effectively).
- Real-time fraud flagging through an intuitive web interface.

---

## 🖼️ Screenshots
*(Add Streamlit app screenshots here — dashboard, confusion matrix, transaction upload UI)*

---

## ▶️ Run Locally
Clone the repo and install dependencies:

```bash
git clone https://github.com/AbdirahmanFree/fraud-detector.git
cd fraud-detector
pip install -r requirements.txt
streamlit run app.py
