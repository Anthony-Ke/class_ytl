import numpy as np
import pandas as pd
import random

"""
numpy 结构
"""
# arr_1 = np.array([1, 2, 3, 4, 5])
# print(arr_1)
# arr_2 = np.array([[1,2,3,4,5],
#                   [6,7,8,9,10],
#                   [2,4,6,8,10]])
# print(arr_2)

"""
convert numpy array to pandas dataframe
"""
# df_1 = pd.DataFrame(arr_2)
# print(df_1)

# add columns to the df
# df_1 = pd.DataFrame(arr_2,columns=["A","B","C","D","E"])
# print(df_1)

"""
convert dict to pandas dataframe
"""
# random.seed(0)
# df_2 = pd.DataFrame({"A":[random.choice(range(100)) for i in range(35)],
#                      "B":[random.choice(range(100)) for i in range(35)],
#                      "C":[random.choice(range(100)) for i in range(35)],
#                      "D":[random.choice(range(100)) for i in range(35)],
#                      "E":[random.choice(range(100)) for i in range(35)]})
# print(df_2.head())

"""
practice: generate a df of 100 students with different identity id, gender, class number (1-4)
random math grade, random english grade and random economics grade
"""


"""
iloc
"""
# print(df_2.iloc[1])

"""
index
"""
# random.seed(1)
# df_3 = pd.DataFrame({"A":[random.choice(range(100)) for i in range(10000)],
#                      "B":[random.choice(range(100)) for i in range(10000)],
#                      "C":[random.choice(range(100)) for i in range(10000)],
#                      "D":[random.choice(range(100)) for i in range(10000)],
#                      "E":[random.choice(range(100)) for i in range(10000)]},
#                     index = [str(random.choice(range(100))) for i in range(10000)])
# print(df_3.head())
#
# df_3.index = df_3["A"]
# print(df_3.head())

"""
使用loc进行访问
"""
# print(df_3.loc[8])
# # 得出的不一定是一行

"""
get column
"""
# random.seed(2)
# df_3 = pd.DataFrame({"A":[random.choice(range(100)) for i in range(10000)],
#                      "B":[random.choice(range(100)) for i in range(10000)],
#                      "C":[random.choice(range(100)) for i in range(10000)],
#                      "D":[random.choice(range(100)) for i in range(10000)],
#                      "E":[random.choice(range(100)) for i in range(10000)]}
#                     )
# print(df_3.head()["A"])

# tolist操作

"""
找出不同age各有多少人 和 各个gender有多少人 
"""
df_population = pd.read_csv("./population.csv")

"""
get element of dataframe
"""
# print(type(df_3["A"].iloc[4]))
# print(df_3.iloc[4]["A"])
# print(df_3.loc[4,"A"])
# print(df_3.iloc[4,0])
# print(df_3["A"].iloc[4] + 6)

"""
find the student with the highest math grade
"""

"""
add new row
"""
# df_3 = df_3._append({"A":10, "B":20, "C":30, "D":40, "E":40},ignore_index=True)
# #ignore_index = True 不可省略
# print(df_3)

"""
添加一行展示各个学科的平均分，identity, gender, class number全部写 "All"
"""


"""
add new column
"""
# length = len(df_3)
# df_3["F"] = [random.choice(range(100)) for i in range(length)]
# print(df_3.head())

"""
apply method
"""
# df_3["A"] = df_3["A"].apply(lambda x : x * 2)
# print(df_3.head()["A"])

"""
添加一列表现学生的数学成绩和平均分的差值
"""

"""
将最终的df写成csv的格式
"""