import pandas as pd

# Load the dataset
df = pd.read_csv("athlete_events.csv")

# Filter for female athletes only
female_athletes = df[df['Sex'] == 'F']
print(female_athletes.head())

# Filter for athletes older than 35
older_athletes = df[df['Age'] > 35]
print(older_athletes[['Name', 'Age', 'Sport']].head())

print("")
print("")
print("")

# The amount of rows in the table
print(len(older_athletes[['Name', 'Age', 'Sport']].head()))

print("")
print("")
print("")

# Female athletes over 30
combo_filter = df[(df['Sex'] == 'F') & (df['Age'] > 30)]
print(combo_filter[['Name', 'Age', 'Sport']].head())

print("")
print("")
print("")

# Male athletes in Basketball
basketball_males = df[(df['Sex'] == 'M') & (df['Sport'] == 'Basketball')]
print(basketball_males.head())

print("")
print("")
print("")


# Australian Swimmers
australian_swimmers = df[(df['Team'] == 'Australia') & (df['Sport'] == 'Swimming')]
print(australian_swimmers.head())

print("")
print("")
print("")

# Sort by age
sorted_by_age = df.sort_values(by='Age', ascending=False)
print(sorted_by_age[['Name', 'Age', 'Sport']].head())

print("")
print("")
print("")

# Sort by weight
sorted_by_weight = df.sort_values(by='Weight', ascending=False)
print(sorted_by_weight[['Name', 'Weight', 'Sport']].head(10))

print("")
print("")
print("")

# Sort by height
sorted_by_height = df.sort_values(by='Height', ascending=False)
print(sorted_by_height[['Name', 'Height', 'Sport']].head(10))

print("")
print("")
print("")

# Count participants in each sport
sport_counts = df['Sport'].value_counts()
print(sport_counts.head())

print("")
print("")
print("")

# Count medals per team
medals_by_team = df[df['Medal'].notnull()].groupby('Team')['Medal'].count()
print(medals_by_team.sort_values(ascending=False).head())

print("")
print("")
print("")

female_participants = df[df['Sex'] == 'F'].groupby('Sport')['Sex'].count()
print(female_participants.sort_values(ascending=False).head())

# Average height per sport
avg_height = df.groupby('Sport')['Height'].mean().sort_values(ascending=False)
print(avg_height.head())

print("")
print("")
print("")

# Median age by year
median_age_by_year = df.groupby('Year')['Age'].median()
print(median_age_by_year.tail())

print("")
print("")
print("")

# Average weight by sex and sport
average_weight = df.groupby(['Sex', 'Sport'])['Weight'].mean()
print(average_weight.head(100)) # I made it show 100 rows so it could show it for both female and males

print("")
print("")
print("")

# Filter gymnasts and save to new CSV
gymnasts = df[df['Sport'] == 'Gymnastics']
gymnasts.to_csv('gymnastics_athletes.csv', index=False)

print("")
print("created gymnastics_athletes.csv")
print("")

# Athletes undetr 18 years of Age
all_athletes_under_18 = df[df['Age'] < 18]
all_athletes_under_18.to_csv('all_athletes_under_18.csv', index=False)

print("")
print("created all_athletes_under_18.csv")
print("")

# Gold Medal
Gold_Medal = df[df['Medal'] == 'Gold']
Gold_Medal.to_csv('Gold_Medal_Athletes.csv', index=False)

print("")
print("created Gold_Medal_Athletes.csv")
print("")

'''
Internal, Exporting and Loading Data Files
'''

import pandas as pd

def main():
    # Create a DataFrame with some sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    
    df = pd.DataFrame(data)
    
    # Display the DataFrame
    print("DataFrame:")
    print(df)

    # Save the DataFrame to a CSV file
    df.to_csv('sample_data.csv', index=False)
    print("\nDataFrame saved to 'sample_data.csv'.")

    # Read the DataFrame from the CSV file
    df_loaded = pd.read_csv('sample_data.csv')

    print("\nDataFrame loaded from 'sample_data.csv':")

    # Display the loaded DataFrame
    print(df_loaded)