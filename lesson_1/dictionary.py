"""
section 1: create a dictionary
"""
my_dict = {'a': 1, 'b': 2, 'c': 3}

"""
section 2: index of a dictionary
"""
# print an element of the dictionary
value_1 = my_dict["a"]
print(my_dict["a"])

"""
section 3: keys of a dictionary
"""
# print the keys of the dictionary
print(my_dict.keys())
for key in my_dict.keys():
    print(key)

for key in my_dict:
    print(key)

for key, value in my_dict.items():
    print(f"key: {key}, value: {value}")

# convert the keys to a list
list(my_dict.keys())
"""
section 4: values of a dictionary
"""
# print the values of the dictionary
# convert the values to a list

"""
section 5: add element to dictionary
"""
# add the key "d" and assign the value 4 to it
my_dict['d'] = 4
print(my_dict)

