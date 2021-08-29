import pandas as pd

samsong_df = pd.read_csv('data/samsong.csv')
hyundee_df = pd.read_csv('data/hyundee.csv')

# 코드를 작성하세요.
day_ser = samsong_df.loc[:, '요일']
sam_ser = samsong_df.loc[:, '문화생활비']
hyun_ser = hyundee_df.loc[:, '문화생활비']
data_list = {
    'day' : day_ser,
    'samsong' : sam_ser,
    'hyundee' : hyun_ser
}

df = pd.DataFrame(data_list)
df
