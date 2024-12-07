import pandas as pd

df = pd.read_csv('./population.csv')

"""
group by 方法
"""
# for group in df.groupby('age'):
#     print(group)

# grouped_df = df.groupby('age')
#
# for name, group in grouped_df:
#     print(name)
#     print(group.iloc[0:2])

"""
将居民按照住的楼栋分组，打印出每一组里面各个age的人有多少
"""

df.groupby('age').size()


"""
pd concatenate
"""