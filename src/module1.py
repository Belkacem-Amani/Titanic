
# 1 Survival rate by gender
def survival_by_gender(df):
    return df.groupby('Sex')['Survived'].mean()


# 2 Survival rate by class
def survival_by_class(df):
    return df.groupby('Pclass')['Survived'].mean()


# 3 Age statistics
def age_statistics(df):
    return {
    'mean': df['Age'].mean(),
    'min': df['Age'].min(),
    'max': df['Age'].max()
    }