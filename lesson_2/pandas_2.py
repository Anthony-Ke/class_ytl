import pandas as pd

df = pd.read_csv('.\lesson_2\population.csv')

"""
group by 方法
"""
# 将会给产生一个可遍历的对象，每一个元素都是包含分类具体值，dataframe
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
#初始化存储所以最终数据的dict
ageDictByHouse = {}
#通过address分组，得到tuple里面0为对应的房子，1为这个房子内人的df数据，对这个遍历
for groupByHouse in df.groupby("address"):
    #获取对应数据
    house = groupByHouse[0]
    persons = groupByHouse[1]
    #初始化单独房间内的dict
    ageDictInHouse = {}
    #遍历房间中的人
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


df.groupby('age').size()


"""
pd concatenate
"""