import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C://Users/NAGUL/Downloads/matches.csv")

matches_won_by_team = data['Winner'].value_counts()
print("Number of matches won by each team:")
print(matches_won_by_team)

# Plotting the results as a bar chart
matches_won_by_team.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel('Team')
plt.ylabel('Number of Matches Won')
plt.title('Number of Matches Won by Each Team')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
