import random

num_list = [random.choice(range(1,100)) for i in range(500)]

"""
if statement
"""
# if 的indent是有意义的

"""
while loop
"""
# determine whether the number 20 is in the num_list
# if it is in the list, tell how many elements are there before it

# idx = 0
# number = None
#
# while idx < len(num_list) and number != 20:
#     # 检查list 的索引不超过范围
#     number = num_list[idx]
#     idx += 1
# if number == 20:
#     print("20 is in the list")
#     number_before = idx-1
#     print(f"There are {number_before} numbers before the element 20.")
# else:
#     print("20 is not in the list")

"""
用list解决
"""
idx = 0
number = None
before_list = []

while idx < len(num_list):
    # 检查list 的索引不超过范围
    number = num_list[idx]
    if number == 20:
        before_list.append(idx)
    idx += 1

for i in range(len(before_list)):
    print(f"The {i+1}th 20 has {before_list[i]} elements before it.")

"""
用dict解决
"""
idx = 0
number = None
num_of_20 = 0
before_dict = {}

while idx < len(num_list):
    # 检查list 的索引不超过范围
    number = num_list[idx]
    if number == 20:
        num_of_20 += 1
        formatted_key = f"{num_of_20}th_20"
        before_dict[formatted_key] = idx
    idx += 1

print(before_dict)


"""
for loop
"""
# find all the numbers divisible by 13 or 17 or 19 between 0 and 10000
numbers_list = []
for num in range(10001):
    if (num % 13 == 0) or (num % 17 == 0) or (num % 19 == 0):
        numbers_list.append(num)
print(numbers_list)

# while: 没有止境，不固定长度，只与判断的statement有关
# for: 固定长度，缺少灵活性

# keys: "divisible_by_13_only"
#       "divisible_by_17_only"
#       "divisible_by_19_only"
#       "divisible_by_13_and_17_only"
#       "divisible_by_13_and_19_only"
#       "divisible_by_17_and_19_only"
#       "divisible_by_13_17_and_19"


divisible_dict = {
    "divisible_by_13_only":[],
    "divisible_by_17_only":[],
    "divisible_by_19_only": [],
    "divisible_by_13_and_17_only": [],
    "divisible_by_13_and_19_only": [],
    "divisible_by_17_and_19_only": [],
    "divisible_by_13_17_and_19":[]
                  }
for num in range(10001):
    remainder_13 = num % 13
    remainder_17 = num % 17
    remainder_19 = num % 19
    if remainder_13 == 0 and remainder_17 == 0 and remainder_19 == 0:
        divisible_dict["divisible_by_13_17_and_19"].append(num)
    elif remainder_13 == 0 and remainder_17 == 0:
        divisible_dict["divisible_by_13_and_17_only"].append(num)
    elif remainder_13 == 0 and remainder_19 == 0:
        divisible_dict["divisible_by_13_and_19_only"].append(num)
    elif remainder_17 == 0 and remainder_19 == 0:
        divisible_dict["divisible_by_17_and_19_only"].append(num)
    elif remainder_13 == 0:
        divisible_dict["divisible_by_13_only"].append(num)
    elif remainder_17 == 0:
        divisible_dict["divisible_by_17_only"].append(num)
    elif remainder_19 == 0:
        divisible_dict["divisible_by_19_only"].append(num)

for key , value in divisible_dict.items():
    print(f"{key} : {value}")

# for num in range(10001):
#     remainder_13 = num % 13
#     remainder_17 = num % 17
#     remainder_19 = num % 19
#     if remainder_13 == 0:
#         if remainder_17 == 0:
#             if remainder_19 == 0:
#                 divisible_dict["divisible_by_13_17_and_19"].append(num)
#             else:
#                 divisible_dict["divisible_by_13_and_17_only"].append(num)
#         else:
#             if remainder_19 == 0:
#                 divisible_dict["divisible_by_13_and_19_only"].append(num)
#             else:
#                 divisible_dict["divisible_by_13_only"].append(num)
#     else:
#         if remainder_17== 0:
#             if remainder_19 == 0:
#             else:
#         else:


"""
concise way to generate list
"""
list_temp = [i*2 for i in range(100)]

"""
use of enumerate
"""
num_list_new = [[random.choice(range(100)) for i in range(35)] for j in range(20)]
# construct a dictionary to indicate how many odd numbers in each element of num_list_new

odd_num_dic = {}

for j,small_list in enumerate(num_list_new):
    num_odd = 0
    for num in small_list:
        if num % 2 != 0:
            num_odd += 1
    key_name = f"the_amount_of_odd_numbers_in_{j+1}th_list"
    odd_num_dic[key_name] = num_odd
print(odd_num_dic)

# construct a dictionary to indicate how many numbers divisible by 7 and how many
# divisible by 13 in each element of num_list_new
divisableAmountDict = {}
for numberOfList,smallList in enumerate(num_list_new):
    keyName = f"The {numberOfList + 1}th list"
    divisableAmountDict[keyName] = {}
    amountOfDivisableBy7 =0
    amountOfDivisableBy13 =0
    for num in smallList:
        if num % 7 == 0:
            amountOfDivisableBy7 += 1
        if num % 13 == 0:
            amountOfDivisableBy13 += 1

    divisableAmountDict[keyName]["divisableBy7"] = amountOfDivisableBy7
    divisableAmountDict[keyName]["divisableBy13"] = amountOfDivisableBy13

# 当dict没有声明的时候不能够越级赋值

for key, value in divisableAmountDict.items():
    print(f"{key} : {value}")

"""
use of continue
"""
for i in range(20):
    if i ==2:
        continue
    print(i)

"""
use of break
"""
for i in range(20):
    if i ==2:
        break
    print(i)
