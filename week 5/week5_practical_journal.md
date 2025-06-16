# Data Cleaning – Preparing Messy Data
### Pranav Balamurugan

## Task 2:

- Are labels readable?
    - Yes, the labels are readable.
- Does the chart title clearly explain what’s shown?
    - Yes, the chart title clearly explaisn what it is shown.

## Task 3:

- Is there a trend over time?
    - No, there is no trend in the graph. 
- Does this graph suggest changes in athlete demographics?
    - It shows the mean age for atheletes who participate in the Olympics

## Task 4:

- Change bins=30 to bins=10. What changes?
    - When you change bins to 10, the graph gets less detailed, hence less accurate.
- Describe the shape of the data: is it normal, skewed, or unusual?
    - It has an almost symetrical unimodal shape with most people lying in the middle of the graph

## Task 5:

- The percentage for Gold was 33.7%, silver was 32.7% and bronze was 33.6% of the population

## Task 6:

    avg_heights = df.groupby('Sport')['Height'].mean()

    avg_heights.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.xlabel("Sport")
    plt.ylabel("Average Height (cm)")
    plt.title("Average Height by Sport")
    plt.savefig("avg_height_per_sport.png")
    plt.show()


- Which chart was easiest to understand? Why?
    - The pie graph was the easiest to understand because it was simple and only had 3 sections.
- Which chart was hardest to interpret? Why?
    - The chart I created was the hardest to understand as the x axis was over-crowded.
- How can visualising data help you make better decisions?
    - It can help make decisions as we can view the past statistics for guidance.