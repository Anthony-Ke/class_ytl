import json
import pandas as pd

with open(file = "./lesson_1/agentSimulate_new.json",mode="r", encoding="gbk") as f:
    resident_list = json.load(f)

print(resident_list[0].keys())

# 定位出前100个居民
# 创建一个字典 resident_dict 展示前100个居民的属性，
# 以居民的"id"为key，对应的value为一个字典。
# 这个字典里面包含了姓名，性别，house_ue_id，职业这些信息
residentDict = {}
templeList = resident_list[:101]
for resident in templeList:
    id = resident["id"]
    name = resident["姓名"]
    sex = resident["性别"]
    houseUEID = resident["house_ue_id"]
    job = resident["职业"]
    residentAdded = {"姓名":name,"性别":sex,"house_ue_id":houseUEID,"职业":job}
    residentDict[id] = residentAdded

for key,value in residentDict.items():
    print(f"{key} : {value}")
# 定位出前100个居民
# 创建一个字典，表示每一个"house_ue_id"对应了几个居民
# Q1
# 利用这个字典，找出住的人最多的"house_ue_id"，不需要体现是否并列第一
houseUEIDDict = {}
templeList = resident_list[:101]
for resident in templeList:
    houseUEID = houseUEID = resident["house_ue_id"]
    if houseUEID in houseUEIDDict.keys():
        houseUEIDDict[houseUEID] += 1
    else:
        houseUEIDDict[houseUEID] = 1
keyOfFirst = []
largestValue = 0
for key, value in houseUEIDDict.items():
    if value > largestValue:
        keyOfFirst.clear()
        keyOfFirst.append(key)
        largestValue = value
    elif value == largestValue:
        keyOfFirst.append(key)
print(f"{keyOfFirst} have the most resident ({largestValue})")

# Q2
# 展示出是否并列第一

resident_df = pd.read_csv("./leeson_1/population.csv")
#
