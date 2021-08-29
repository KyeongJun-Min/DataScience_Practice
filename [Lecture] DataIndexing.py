import pandas as pd

iphone_df = pd.read_csv('data/iphone.csv')
iphone_df2 = pd.read_csv('data/iphone.csv', index_col = 0) # index 값을 column 0번 값으로 사용하라는 의미
iphone_df2

iphone_df2.loc['iPhone 8', '메모리']
iphone_df2.loc['iPhone X', :]
iphone_df2.loc['iPhone X']
iphone_df2.loc[:, '출시일']
type(iphone_df2.loc['iPhone 8', '메모리'])
