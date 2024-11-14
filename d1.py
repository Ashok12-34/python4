import pandas as pd

data=pd.read_csv("C://Users/NAGUL/Downloads/matches.csv")
matches_per_season = data.groupby('Season').size().reset_index(name='Match_Count')
print(matches_per_season)