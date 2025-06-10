import pandas as pd

# Load the dataset
df = pd.read_csv("athlete_events.csv")

# Show the first 5 rows
print(df.head())

# Show the column names
print(df.columns)

# Everything underneath this note is part of Activities 3
print(df['Sport'].value_counts().head())
print(df['Sex'].value_counts())
print(df.describe())
print(df['NOC'].nunique())
print(df['NOC'].unique())