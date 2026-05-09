import joblib
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

from preprocessing import load_data, preprocess_data

df = load_data("../data/credit_risk_dataset.csv")


X_train, X_test, y_train, y_test = preprocess_data(df)


model = XGBClassifier()


model.fit(X_train, y_train)


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")

print(classification_report(y_test, y_pred))

joblib.dump(model, "../models/credit_risk_model.pkl")

print("Model saved successfully!")