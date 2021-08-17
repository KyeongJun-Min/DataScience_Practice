import pandas as pd

two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]
my_df = pd.DataFrame(two_dimensional_list, columns=['name', 'english_score', 'math_score'], index=['a','b','c','d'])
my_df

type(my_df)
my_df.columns
my_df.index
my_df.dtypes

# object는 pandas에서 문자열을 나타낸다.
# 단, 같은 column 내에서는 모두 같은 자료형이여야 한다.
