import pandas as pd

# 코드를 작성하세요.
data_list = [['Taylor Swift', 'December 13, 1989', 'Singer-songwriter'],
['Aaron Sorkin', 'June 9, 1961', 'Screenwriter'],
['Harry Potter', 'July 31, 1980', 'Wizard'],
['Ji-Sung Park', 'February 25, 1981', 'Footballer']]

my_df = pd.DataFrame(data_list, columns = ['name', 'birthday', 'occupation'], index = ['0', '1', '2', '3'])

# 정답 출력
my_df
