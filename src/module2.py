import sqlite3
from sqlalchemy import create_engine
import pandas as pd


DB_NAME = 'titanic.db'


# 1 Save DataFrame to SQLite using sqlite3
def save_to_sqlite(df):
    conn = sqlite3.connect(DB_NAME)
    df.to_sql('titanic', conn, if_exists='replace', index=False)
    conn.close()


# 2 Load data using SQLAlchemy
def load_from_db():
    engine = create_engine(f'sqlite:///{DB_NAME}')
    return pd.read_sql('SELECT * FROM titanic', engine)