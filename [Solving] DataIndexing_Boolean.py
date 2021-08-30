import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)
# 코드를 작성하세요.

boolean_KBS = df['KBS'] > 30   # boolean_KBS는 KBS가 30 초과인 모든 row의 값을 갖는다.
df.loc[boolean_KBS, 'KBS']
