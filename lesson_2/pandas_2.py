import pandas as pd

df = pd.read_csv('./population.csv')

"""
group by 方法
"""
# .groupby()会产生一个可便利的对象，这里面每一个元素都是一个包含分类值和对应df的tuple
# for group in df.groupby('age'):
#     print(group[1])

# grouped_df = df.groupby('age')
#
# for name, group in grouped_df:
#     print(name)
#     print(group.iloc[0:2])

"""
将居民按照住的楼栋分组，打印出每一组里面各个age的人有多少
"""
df["building_number"] = df["address"].apply(lambda x:x.split("栋")[0])
print(df.head())

df_grouped_by_building = df.groupby("building_number")
# name 为值 group为对应的小df
for name, group in df_grouped_by_building:
    print(name)
    print(group.iloc[0:2])

"""
home_work_12_7
"""

# 尝试
# df.groupby('age').size()


"""
pd concatenate
"""