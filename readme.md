# 🏠 House Price Prediction — AI / Machine Learning Project

This project predicts the selling price of a house based on multiple features such as area, bedrooms and age of the property using Machine Learning (Linear Regression).

---

## 📋 Project Summary
House pricing estimation is complex because multiple features affect the cost of a property. This project provides an automated ML-based solution that predicts house price using:
- **Area (sq ft)**
- **Bedrooms**
- **Age of house (years)**

The model learns patterns from historical data and predicts the price of new house inputs.

---

## ✨ Features
- Predicts house price instantly based on user inputs
- Implements **Linear Regression model**
- **Train / Test split** for accurate evaluation
- Shows **R² score & MAE**
- Saves trained model for future predictions (`model_saved.pkl`)
- Displays **Actual vs Predicted graph**

---

## ⚙ Technologies & Libraries Used
- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Joblib

---

## 🧠 Model Training Approach
1. Load and clean dataset
2. Select input features and target variable
3. Split dataset into training & testing
4. Train Linear Regression model
5. Evaluate performance
6. Save trained model (`model_saved.pkl`)

---

## 📁 Project Files
| File | Description |
|------|-------------|
| `HousePrice.ipynb / house_price.py` | Main ML program |
| `house_data.csv` | Dataset file |
| `model_saved.pkl` | Saved trained model |
| `README.md` | Documentation |
| `statement.md` | Project explanation |

---

## 🚀 How to Run
1. Install Python 3
2. Install required libraries:
   pip install pandas numpy matplotlib scikit-learn joblib
3. Open the terminal inside the project folder
4. Run:
   python house_price.py
OR open the notebook:
   HousePrice.ipynb

To use saved model:
```
joblib.load("model_saved.pkl")
model.predict([[area, bedrooms, age]])
```

---

## 🖥 Sample Prediction Output
User Input:
Area = 1650
Bedrooms = 3
Age = 5

Predicted Output:
Estimated Price → ₹ 78,56,500

---

## 🎯 Key Learnings
- Data preprocessing
- ML model development (Linear Regression)
- Performance evaluation (R², MAE)
- Model saving & deployment
- Real-world price prediction using ML

---

## 👤 Author
**Ansh Yadav**
House Price Prediction — AI/ML Project  
Academic Year: 2025 – 2026