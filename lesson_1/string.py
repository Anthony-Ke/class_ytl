"""
operation of strings
"""

str_1 = "Hello"

"""
section1: index and slice and length
"""
str_2 = str_1[1]
str_3 = str_1[2:]
print(str_2,str_3)

"""
section2: concatenate
"""
str_2 = "World"

print(str_1+str_2)
"""
section3: f-string
"""
formatted_string = f"{str_1} and {str_2}"
print(formatted_string)

"""
section4: string split
"""
str4 = "Hello,World.China"
lst_4 = str4.split(sep = ".")
print(lst_4)