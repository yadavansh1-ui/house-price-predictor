# House Price Prediction System using Machine Learning

This project is a simple machine learning based tool that predicts the approximate price of a house.
The system takes three inputs: Area (sq ft), Number of Bedrooms and Age of the house. I built this project to understand how machine learning models can be applied in real life problem solving.

## Features
- Train a Linear Regression model on the dataset
- Predict price using user inputs
- View model accuracy (R2 Score and MAE)
- Graph of actual vs predicted values
- Simple command-line interface

## Technologies Used
- Python
- Pandas
- Scikit-Learn
- Matplotlib
- Joblib

## How to Run
1. Install Python 3
2. Download all files from this repository
3. Make sure `house_data.csv` is in the same folder
4. Run the project using the command:

```python 
python house_price.py
```

## Files Included
- `house_price.py` — main ML code
- `house_data.csv` — dataset used for training
- `statement.md` — project explanation
- `README.md` — documentation file

## Sample Menu (when the program runs)

```python 
=== House Price Predictor ===

Train Model

Predict House Price

Exit

```

## How the Model Works (simple explanation)
The dataset is loaded → divided into training & testing → Linear Regression model is trained → 
accuracy is calculated → graph shows comparison → prediction can be done anytime by giving input.

## Author
Ansh Yadav  
VIT Bhopal University
