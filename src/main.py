from utils import load_csv_pandas, fill_missing_values, encode_gender, normalize_fare
from module1 import survival_by_gender, survival_by_class, age_statistics
from module2 import save_to_sqlite, load_from_db
from visualization import plot_survival_count, plot_survival_by_gender, plot_age_distribution
import tkinter as tk
from gui import TitanicGUI


DATA_PATH = 'data/train.csv'


if __name__ == '__main__':
    df = load_csv_pandas(DATA_PATH)
    df = fill_missing_values(df)
    df = encode_gender(df)
    df = normalize_fare(df)

    save_to_sqlite(df)
    db_df = load_from_db()
    #print('Loaded from DB:', db_df.head())

    
    root = tk.Tk()
    app = TitanicGUI(root)
    root.mainloop()
