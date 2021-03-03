import numpy as np
import pandas as pd 

df = pd.read_csv('../FanGraphs Leaderboard.csv')

print(df)
print(df.columns)

off_stats = df[['Name', 'PA', 'HR', 'R', 'RBI', 'SB', 'BABIP', 'AVG', 'wOBA', 'playerid']]

print(off_stats.isnull().sum())

df2 = pd.read_csv('../FantasyofChatas.csv')
df2.dropna(axis=0)
print(df2)