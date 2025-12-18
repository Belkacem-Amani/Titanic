import matplotlib.pyplot as plt


# 1 Survival count visualization
def plot_survival_count(df):
    counts = df['Survived'].value_counts()
    plt.figure()
    plt.bar(counts.index, counts.values)
    plt.xlabel('Survived (0 = No, 1 = Yes)')
    plt.ylabel('Count')
    plt.title('Survival Count')
    plt.show()

# 2 Survival by gender visualization
def plot_survival_by_gender(df):
    gender_survival = df.groupby('Sex')['Survived'].mean()
    plt.figure()
    plt.bar(gender_survival.index, gender_survival.values)
    plt.xlabel('Gender (0 = Male, 1 = Female)')
    plt.ylabel('Survival Rate')
    plt.title('Survival Rate by Gender')
    plt.show()


# 3 Age distribution visualization
def plot_age_distribution(df):
    plt.figure()
    plt.hist(df['Age'], bins=20)
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Age Distribution')
    plt.show()