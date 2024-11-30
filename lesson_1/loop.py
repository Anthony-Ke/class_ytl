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
for i in range(10001):
    if (i % 13 == 0) or (i % 17 == 0) or (i % 19 == 0):
        numbers_list.append(i)
print(numbers_list)



# while: 没有止境，不固定长度，只与判断的statement有关
# for: 固定长度，缺少灵活性

"""
concise way to generate list
"""

"""
use of enumerate
"""
num_list_new = [[random.choice(range(100)) for i in range(35)] for j in range(20)]
# construct a dictionary to indicate how many odd numbers in each element of num_list_new

# construct a dictionary to indicate how many numbers divisible by 7 and how many
# divisible by 13 in each element of num_list_new

"""
use of continue
"""

"""
use of break
"""
