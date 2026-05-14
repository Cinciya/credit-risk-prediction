import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

# Load dataset
df = pd.read_csv("data/credit_risk_dataset.csv")

# Features and target
X = df.drop("loan_status", axis=1)
y = df["loan_status"]

# Categorical columns
categorical_cols = [
    "person_home_ownership",
    "loan_intent",
    "loan_grade",
    "cb_person_default_on_file"
]

# Preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
    ],
    remainder="passthrough"
)

# Pipeline
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", XGBClassifier(
        use_label_encoder=False,
        eval_metric="logloss"
    ))
])

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train
pipeline.fit(X_train, y_train)

# Predict
predictions = pipeline.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.2f}")

# Save pipeline
joblib.dump(pipeline, "models/credit_risk_pipeline.pkl")

print("Pipeline saved successfully!")