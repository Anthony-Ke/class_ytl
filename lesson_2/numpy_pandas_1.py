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
#一般的公认是row为数据，columm为属性

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
df_student = pd.DataFrame({"ID":[str(loopnumber) for loopnumber in range(100)],
                          "Gender":[random.choice(["Male","Femele"]) for _ in range(100)],
                          "Class_Number":[f"Class_{random.choice(range(1,5))}" for _ in range(100)],
                          "Math_Grade":[random.choice(range(101)) for _ in range(100)],
                          "English_Grade":[random.choice(range(101)) for _ in range(100)],
                          "Economy_Grade":[random.choice(range(101)) for _ in range(100)],
                          })
print(df_student.head())
"""
iloc
"""
#用于输出对应的行
#此种数据类型被称为series
#iloc不对应index
# print(df_2.iloc[1])

"""
index
"""
#Index将会选择某一列作为index
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
# 得出的不一定是一行
# 根据index内容查找
# 返回值还是一个dataframe
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
#返回值为dataseries
# tolist操作

"""
找出不同age各有多少人 和 各个gender有多少人 
"""
# 读取文件
df_population = pd.read_csv(".\lesson_2\population.csv")
# 获取数据，然后转化为list
ageList = df_population["age"].tolist()
genderList = df_population["gender"].tolist()
#
ageResultDict = {}
genderResultDict = {}
# 初始化一个最终的list
resultDict = {}
# 同时遍历age和gender，故采取person的
for personIndex in range(len(ageList)):
    # 当这个age已经在result中
    if ageList[personIndex] in ageResultDict.keys():
        # 把对应的人数统计起来，故都加一
        ageResultDict[ageList[personIndex]] += 1
    # 当这个age不在result中
    else:
        # 就新建并初始化为一
        ageResultDict[ageList[personIndex]] = 1
    if genderList[personIndex] in genderResultDict.keys():
        # 把对应的人数统计起来，故都加一
        genderResultDict[genderList[personIndex]] += 1
    else:
        # 当这个gender不在result中
        genderResultDict[genderList[personIndex]] = 1
# 存储为一个字典
resultDict = {"age":ageResultDict,"gender":genderResultDict}
print(resultDict)
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
# 读取dataframe为list
IDList = df_student["ID"].tolist()
mathGradeList = df_student["Math_Grade"].tolist()
# 分数从0到100，所以初始值为-1
higestGrade = -1
# 新建列表包含所有最高分学生的list
studentHaveHigestGrade = []
for personIndex in range(len(IDList)):
    # 出现新的最高分
    if mathGradeList[personIndex] > higestGrade:
        # 清除记录的list
        #（一般可以直接赋值空值来清空数组,但是clear会是修改内存，重新赋值则是在内存中再建立一块）
        studentHaveHigestGrade.clear()
        studentHaveHigestGrade.append(IDList[personIndex])
        higestGrade = mathGradeList[personIndex]
    # 出现了一样的最高分
    elif mathGradeList[personIndex] == higestGrade:
        # 添加记录
        studentHaveHigestGrade.append(IDList[personIndex])
print(f"{studentHaveHigestGrade} have  the higest grabe on math ({higestGrade})")


    


"""
add new row
"""
#相当于添加一堆键值对
#可以传入一个dict
#还可以用list来进行一些额外操作
#一般在遍历等里面常用
# df_3 = df_3._append({"A":10, "B":20, "C":30, "D":40, "E":40},ignore_index=True)
# #ignore_index = True 不可省略
# print(df_3)

"""
添加一行展示各个学科的平均分,identity, gender, class number全部写 "All"
"""

"""
add new column
"""
# 获取的是行数用len的话
# length = len(df_3)
# df_3["F"] = [random.choice(range(100)) for i in range(length)]
# print(df_3.head())

"""
apply method
"""
# 对一个panda series进行同样操作
# df_3["A"] = df_3["A"].apply(lambda x : x * 2)
# print(df_3.head()["A"])

"""
添加一列表现学生的数学成绩和平均分的差值
"""
#加载数学的平均成绩并且初始化差值
allMathGrade = df_student["Math_Grade"].tolist()
averageMathGrade = sum(allMathGrade)/len(allMathGrade)
differenceMathGradeList = []
#获取行数
length = len(df_student)
#加对应行数的list，用来存放差值
for studentNumber in range(length):
    #计算差值
    differenceMathGrade = df_student["Math_Grade"].iloc[studentNumber] - averageMathGrade
    #添加到数组
    differenceMathGradeList.append(differenceMathGrade)
df_student["Difference_In_Math"] = differenceMathGradeList
print(df_student.head) 
"""
将最终的df写成csv的格式
"""
df_student.to_csv("outpu.csv",index = False)
# index = False 防止csv出错,除非index有名字，不然加上能爬避免打印index