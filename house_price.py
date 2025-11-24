import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
import joblib
import matplotlib.pyplot as plt

datafile = "house_data.csv"        # just using a variable so I remember
save_model = "model_saved.pkl"     # file where model will be stored

def loaddata():
    try:
        df = pd.read_csv(datafile)
        return df
    except:
        print("Error reading CSV file")
        return []

def train():
    print("\nTraining the model... this might take a few seconds")
    df = loaddata()

    X = df[["Area", "Bedrooms", "Age"]]   # selected 3 features
    y = df["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=10
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, save_model)

    predictions = model.predict(X_test)

    print("\nModel Performance:")
    print("R2 Score =", round(r2_score(y_test, predictions), 3))
    print("MAE =", round(mean_absolute_error(y_test, predictions), 3))

    # simple scatter plot to show the difference visually
    plt.scatter(y_test, predictions, color="blue")
    plt.title("Actual Price vs Predicted Price")
    plt.xlabel("Actual House Price")
    plt.ylabel("Predicted House Price")
    plt.show()

def predict():
    try:
        model = joblib.load(save_model)
    except:
        print("Model not trained yet. Please run option 1 first.")
        return
    
    print("\nPrediction mode (enter 0 for area to exit)")

    while True:
        try:
            area = float(input("Area (sq ft): "))
            if area == 0:
                break
            bed = int(input("Bedrooms: "))
            age = int(input("Age of house (years): "))

            output = model.predict([[area, bed, age]])[0]
            print("Estimated Price =", round(output, 2), "Lakhs")
        except:
            print("Invalid input, please try again")

def main():
    print("=== House Price Predictor ===")
    while True:
        print("\n1. Train Model")
        print("2. Predict House Price")
        print("3. Exit")
        ch = input("> ")
        if ch == "1":
            train()
        elif ch == "2":
            predict()
        else:
            print("Exiting...")
            break

main()
