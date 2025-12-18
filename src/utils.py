import pandas as pd
import numpy as np
import csv

# 1 Load CSV using pandas
def load_csv_pandas(path):
    return pd.read_csv(path)

# 2 Load CSV using csv module
def load_csv_native(path):
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

# 3 Handle missing values
def fill_missing_values(df):
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    return df

# 4 Encode gender
def encode_gender(df):
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    return df

# 5 Encode embarked
def encode_embarked(df):
    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    return df

# 6 Normalize fare
def normalize_fare(df):
    df['Fare'] = (df['Fare'] - df['Fare'].mean()) / df['Fare'].std()
    return df
