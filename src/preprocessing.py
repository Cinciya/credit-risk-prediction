import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE


def load_data(path):
    df = pd.read_csv(path)
    return df


def preprocess_data(df):

    df = df.dropna()

    
    categorical_cols = df.select_dtypes(include=['object']).columns

    le = LabelEncoder()

    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])


    X = df.drop("loan_status", axis=1)
    y = df["loan_status"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    smote = SMOTE(random_state=42)

    X_train, y_train = smote.fit_resample(X_train, y_train)

    return X_train, X_test, y_train, y_test