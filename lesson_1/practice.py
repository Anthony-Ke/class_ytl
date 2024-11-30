import json
import pandas as pd

## gbk 编码：专门为中文开发的编码
## utf-8 expensive 通用

with open('./agentSimulate_new.json', "r", encoding="gbk") as f:
    resident_list = json.load(f)

print(resident_list[0].keys())

# 定位出前100个居民
# 创建一个字典 resident_dict 展示前100个居民的属性，
# 以居民的"id"为key，对应的value为一个字典。
# 这个字典里面包含了姓名，性别，house_ue_id，职业这些信息


"""
homework_11_30
"""
# 定位出前100个居民
# 创建一个字典，表示每一个"house_ue_id"对应了几个居民
# Q1
# 利用这个字典，找出住的人最多的"house_ue_id"，不需要体现是否并列第一

# Q2
# 展示出是否并列第一

#
#


