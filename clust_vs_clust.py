import pandas as pd

cpairs = pd.read_csv('player_to_player.csv')
del cpairs['batsman']
del cpairs['bowler']

final = cpairs.groupby(['batclustno','bowlclustno']).mean()    					
final.to_csv('clust_to_clust.csv')
