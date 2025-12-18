import tkinter as tk 
from tkinter import messagebox
from utils import load_csv_pandas, fill_missing_values, encode_gender, encode_embarked, normalize_fare
from module1 import survival_by_gender, survival_by_class
from visualization import plot_survival_count, plot_survival_by_gender, plot_age_distribution

DATA_PATH = 'data/train.csv'

class TitanicGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Titanic Data Analysis')
        self.root.geometry('400x350')

        tk.Label(root, text='Titanic Dataset GUI', font=('Arial', 16)).pack(pady=10)

        tk.Button(root, text='Load & Clean Data', width=25, command=self.load_data).pack(pady=5)
        tk.Button(root, text='Show Survival Stats', width=25, command=self.show_stats).pack(pady=5)
        tk.Button(root, text='Plot Survival Count', width=25, command=self.plot_survival).pack(pady=5)
        tk.Button(root, text='Plot Survival by Gender', width=25, command=self.plot_gender).pack(pady=5)
        tk.Button(root, text='Plot Age Distribution', width=25, command=self.plot_age).pack(pady=5)

        self.df = None

    def load_data(self):
        self.df = load_csv_pandas(DATA_PATH)
        self.df = fill_missing_values(self.df)
        self.df = encode_gender(self.df)
        self.df = encode_embarked(self.df)
        self.df = normalize_fare(self.df)
        messagebox.showinfo('Success', 'Data loaded and cleaned successfully!')

    def show_stats(self):
        if self.df is None:
            messagebox.showerror('Error', 'Load data first!')
            return
        gender_stats = survival_by_gender(self.df)
        class_stats = survival_by_class(self.df)
        msg = f'Survival by Gender:\n{gender_stats}\n\nSurvival by Class:\n{class_stats}'
        messagebox.showinfo('Statistics', msg)

    def plot_survival(self):
        if self.df is not None:
            plot_survival_count(self.df)
        else:
            messagebox.showerror('Error', 'Load data first!')

    def plot_gender(self):
        if self.df is not None:
            plot_survival_by_gender(self.df)
        else:
            messagebox.showerror('Error', 'Load data first!')

    def plot_age(self):
        if self.df is not None:
            plot_age_distribution(self.df)
        else:
            messagebox.showerror('Error', 'Load data first!')

if __name__ == '__main__':
    root = tk.Tk()
    app = TitanicGUI(root)
    root.mainloop()
