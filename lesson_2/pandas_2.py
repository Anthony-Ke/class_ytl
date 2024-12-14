import pandas as pd
import random

random.seed(0)
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
# df["building_number"] = df["address"].apply(lambda x:x.split("栋")[0])
# print(df.head())
#
# df_grouped_by_building = df.groupby("building_number")
# # name 为值 group为对应的小df
# for name, group in df_grouped_by_building:
#     print(name)
#
#     print(group.groupby('age').size())



"""
home_work_12_7
"""

# 尝试
# df.groupby('age').size()


#初始化存储所以最终数据的dict
# ageDictByHouse = {}
# #添加楼栋号码
# df["building_number"] = df["address"].apply(lambda x:x.split("栋")[0])
# #通过address分组，得到tuple里面0为对应的房子，1为这个房子内人的df数据，对这个遍历
# for groupedByHouse1 in df.groupby("building_number"):
#     #获取对应数据
#     house = groupedByHouse1[0]
#     persons = groupedByHouse1[1]
#     #初始化单独房内的dict
#     ageDictInHouse = {}
#     #遍历房中的人
#     for lineNumber in range(len(persons)):
#         age = persons["age"].iloc[lineNumber]
#         #判断年龄是否记录
#         if age in ageDictInHouse:
#             #当年龄已经记录，则记录加一
#             ageDictInHouse[age] += 1
#         else:
#             #没被记录，则记录为一
#             ageDictInHouse[age] = 1
#     #加入到整体大dict里面
#     ageDictByHouse[house] = ageDictInHouse
# #遍历输出结果
# for item in ageDictByHouse.items():
#     print(item)


# name 为值 group为对应的小df
#    print(name)
#    print(group.iloc[0:2])

"""
home_work_12_7
"""

# 尝试
# df.groupby('age').size()
# ageDictByHouse.clear()
# #groupby
# for groupedByHouse2 in df.groupby("building_number"):
#     house = groupedByHouse2[0]
#     persons = groupedByHouse2[1]
#     #通过size（）得到人数
#     ageDictByHouse[house] = persons.groupby("age").size()
#     print(ageDictByHouse[house])

"""
pd concatenate
"""
#分为横竖，按行和按列，某人直接加到下方（axis = 0）
#需要左右就可以axis = 1

# # 生成一个新的df, 表头为"address" , "num_residents"
# # address 仍然为 地址 num_residents 为这一户住了多少人
# df_grouped_by_address = df.groupby("address")
#初始化了一个list
# df_list = []
# for name, group in df_grouped_by_address:
#     df_temp = pd.DataFrame({
#         "address": [name],
#         "num_residents": [len(group)]
#     })
#     df_list.append(df_temp)
# df_list没每个元素都是个df，每个df只有一行
# 这个只会接受list
# df_num_residents = pd.concat(df_list,axis=0)
# print(df_num_residents)
#
# income_level = ["low", "medium_low", "medium", "medium_high", "high"]
# length = len(df)
# income = [random.choice(income_level) for i in range(length)]
# num_friends = [random.choice(range(1,6)) for i in range(length)]
# df_new = pd.DataFrame({
#     "income": income,
#     "num_friends":num_friends
# })
# 左右拼接
# df = pd.concat([df,df_new],axis = 1)
# print(df.head())
#
# # 查看某一个属性的独立值
# print(df["age"].unique())

# 建立新的规则，基于层高和年纪
# 层高为3层或以下的居民收入不可能为"high"
# 层高为5层或以下的居民收入不可能为"low"
# infant 和 children收入为"None"