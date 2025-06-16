import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("athlete_events_cleaned.csv")

"""
Task 2:
"""

sport_counts = df['Sport'].value_counts().head(10)

sport_counts.plot(kind='bar', title='Top 10 Sports by Athlete Count')
plt.xlabel('Sport')
plt.ylabel('Number of Athletes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_10_sports.png")
plt.show()

"""
Task 3:
"""

median_age = df.groupby('Year')['Age'].median()

median_age.plot(kind='line', title='Median Athlete Age Over Time')
plt.xlabel('Olympic Year')
plt.ylabel('Median Age')
plt.grid(True)
plt.tight_layout()
plt.savefig("median_age_line.png")
plt.show()

"""
Task 4:
"""

df['Weight'].plot(kind='hist', bins=30, title='Distribution of Athlete Weights')
plt.xlabel('Weight (kg)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("weight_distribution_bins30.png")
plt.show()

# Part B 

df['Weight'].plot(kind='hist', bins=10, title='Distribution of Athlete Weights')
plt.xlabel('Weight (kg)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("weight_distribution_bins10.png")
plt.show()

"""
Task 5:
"""

medal_counts = df[df['Medal'] != 'None']['Medal'].value_counts()

medal_counts.plot(kind='pie', autopct='%1.1f%%', title='Distribution of Medal Types')
plt.ylabel('')  # Removes default y-axis label
plt.tight_layout()
plt.savefig("medal_pie_chart.png")
plt.show()

"""
Task 6:
"""

avg_heights = df.groupby('Sport')['Height'].mean()

avg_heights.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel("Sport")
plt.ylabel("Average Height (cm)")
plt.title("Average Height by Sport")
plt.savefig("avg_height_per_sport.png")
plt.show()


