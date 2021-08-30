import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)
# 코드를 작성하세요.

boolean_data = df['SBS'] < df['TV CHOSUN']
df.loc[boolean_data, ['SBS', 'TV CHOSUN']]
