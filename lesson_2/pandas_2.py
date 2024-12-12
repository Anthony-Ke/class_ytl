import pandas as pd

df = pd.read_csv('.\lesson_2\population.csv')

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
#初始化存储所以最终数据的dict
ageDictByHouse = {}
#添加楼栋号码
df["building_number"] = df["address"].apply(lambda x:x.split("栋")[0])
#通过address分组，得到tuple里面0为对应的房子，1为这个房子内人的df数据，对这个遍历
for groupedByHouse1 in df.groupby("building_number"):
    #获取对应数据
    house = groupedByHouse1[0]
    persons = groupedByHouse1[1]
    #初始化单独房内的dict
    ageDictInHouse = {}
    #遍历房中的人
    for lineNumber in range(len(persons)):
        age = persons["age"].iloc[lineNumber]
        #判断年龄是否记录
        if age in ageDictInHouse:
            #当年龄已经记录，则记录加一
            ageDictInHouse[age] += 1
        else:
            #没被记录，则记录为一
            ageDictInHouse[age] = 1
    #加入到整体大dict里面
    ageDictByHouse[house] = ageDictInHouse
#遍历输出结果
for item in ageDictByHouse.items():
    print(item)


# name 为值 group为对应的小df
#    print(name)
#    print(group.iloc[0:2])

"""
home_work_12_7
"""

# 尝试
# df.groupby('age').size()
ageDictByHouse.clear()
for groupedByHouse2 in df.groupby("building_number"):
    house = groupedByHouse2[0]
    persons = groupedByHouse2[1]
    ageDictByHouse[house] = persons.groupby("age").size()
    print(ageDictByHouse[house])
"""
pd concatenate
"""