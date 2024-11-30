
"""
section1: create a list
"""
lst_1 = [1, 3, 5, 7, 9]
lst_2 = [2, 4, 6, 8, 10]
lst_3 = ["a", "b", "c", "d", "e"]

"""
section2: list index and length
"""
# get the value of a list element
a = lst_1[1]

# get the second element of lst_1
a = lst_1[1]

# get the last element of lst_2
b = lst_2[-1]
b = lst_2[len(lst_2)-1]


# change the value of a list element
lst_2[-1] = 12
print(lst_2)

# change the second element of lst_1
lst_1[1] = 12
print(lst_2)

# change the last element of lst_2
lst_2[-1] = 12
print(lst_2)

"""
section3: list slice
"""
lst_temp = lst_1[2:-1]
print(lst_temp)

"""
section4: append element
"""
lst_1.append(9)

"""
section5: remove element
"""
lst_1.remove(9)
# remove by value

"""
section6: list concatenate
"""
lst_all = lst_1+lst_2+lst_3
print(lst_all)

"""
section7: operation in copied list
"""
# lst_4 = lst_1
#
# lst_4.append(100)
# print(lst_1)
# print(lst_4)
#
# lst_4.remove(1)
# print(lst_1)
# print(lst_4)

# 浅copy
# lst_4 = lst_1.copy()
lst_4 = lst_1[:]
lst_4.append(100)
print(lst_1)
print(lst_4)

lst_4.remove(1)
print(lst_1)
print(lst_4)


"""
section8: range
"""
range(10)
# [0,1,2,....,9]

range(1,11)
# [1,2,...,10]
