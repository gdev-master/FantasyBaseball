import pandas as pd 

df18 = pd.read_csv('data/fantasy_chatas_standings_2018.csv')
df19 = pd.read_csv('data/fantasy_chatas_standings_2019.csv')
df20 = pd.read_csv('data/fantasy_chatas_standings_2020.csv')
df_per_year = [df18, df19, df20]
year = 2018

categories = ['R', 'HR', 'RBI', 'SB', 'AVG', 'K', 'WIN%', 'ERA', 'WHIP', 'SVHD']

for df in df_per_year:
    output_df = pd.DataFrame()

    for cat in categories:
        col_name = cat + "_RANK"
        cat_rank = df[cat].to_frame()
        cat_rank.insert(1, col_name, range(1,13))
        cat_rank[col_name] = cat_rank.rank(ascending=False).astype('int') 
        output_df = pd.concat([output_df, cat_rank], axis=1)

    output_df.insert(0, 'TEAM', df['TEAM'].values)
    output_df.to_csv("analysis/fantasy_chatas_rankings_per_cat_{}.csv".format(year), index=False)
    year += 1