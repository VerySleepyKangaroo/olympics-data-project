# Filtering, Sorting & Grouping
### Pranav Balamurugan

## Task 1: Filtering Basics
- What did these filters do?
    - The first filter filtered out the female group and printed out the first few rows.
- How many rows were returned? Use len().
    - 5 rows were returned.

## Task 2: Combine Filters
Write a filter from athlethes from **Australia** in **swimming**:

    australian_swimmers = df[(df['Team'] == 'Australia') & (df['Sport'] == 'Swimming')]
    print(australian_swimmers.head())

## Task 3: Sorting Data
Sorting by Height:

    # Sort by height
    sorted_by_height = df.sort_values(by='Height', ascending=False)
    print(sorted_by_height[['Name', 'Height', 'Sport']].head(10))

Sorting by Weight:

    # Sort by weight
    sorted_by_weight = df.sort_values(by='Weight', ascending=False)
    print(sorted_by_weight[['Name', 'Weight', 'Sport']].head(10))

## Task 4: Grouping Data

- Which **sport** has the most **female** participants
    - The sport which has the most amount of female paricipants is Athletics with 11666 female participants.

** 
# More Sorting Activities
### Pranav Balamurugan

## Task 5: Aggregating with groupby()

    # Average weight by sex and sport
    average_weight = df.groupby(['Sex', 'Sport'])['Weight'].mean()
    print(average_weight.head(100))

## Task 6: Exploring A Subset()

Athletes Under 18 years of Age

    # Athletes Under 18 years of Age
    all_athletes_under_18 = df[df['Age'] < 18]
    all_athletes_under_18.to_csv('all_athletes_under_18.csv', index=False)

Athletes Who Got a Gold Medal

    # Gold Medal
    Gold_Medal = df[df['Medal'] == 'Gold']
    Gold_Medal.to_csv('Gold_Medal_Athletes.csv', index=False)


## Reflection Journal:

1. **What was the easiest filtering task and why?**

    Task 1 (Filtering basics) was the easiest filtering task as that was literally the 'basic' tasks

2. **What was the most difficult grouping or sorting task?**

    I felt that exporting the 'atheletes with gold medal' quite hard as I needed to use most the skills I learnt for it

3. **What trends surprised you in the Olympic data?**

    I was suprised to learn that there were children that were 14 competing the Olympics

4. **What kinds of real-world questions could this kind of analysis help answer?**

    It could help people check who got the most medals or which country has the most medals.

**
# Internal, Exportinh and Loading Data Files

Why do you think these three operations are key to working with data and information?

- Creating, Saving and Loading which are essential for data analysis and decision making