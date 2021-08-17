import pandas as pd

iphone_df = pd.read_csv('data/iphone.csv')
iphone_df
type(iphone_df)

iphone_df_none = pd.read_csv('data/iphone.csv', header=None) # pandas는 맨 첫줄을 헤더로 인식한다. header를 없애고 싶은 경우, header=None 값을 추가한다.
iphone_df_none

iphone_df2 = pd.read_csv('data/iphone.csv', index_col = 0) # index 값을 column 0번 값으로 사용하라는 의미
iphone_df2
