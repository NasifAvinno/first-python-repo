age = 25
f_name = "Nasif"
l_name = "Erfan"

txt = "My name is {f_name} {l_name} and my age is {age}".format(f_name = f_name, l_name = l_name, age = age)
txt2 = f"My name is {f_name} {l_name} and my age is {age}"

print(txt)
print(txt2)

import math
from unittest import result
print(math.pi)

x = 3.1415

print(math.ceil(x))
print(math.floor(x))
print(round(x))

for i in range(1,101):
    print(f"NASA is being Hacked...   {i}%")

print("NASA is HACKED!!!")


#list comprehension

list = [1,2,3,4,5,6,7,8,9,10]

# normal way
result = []
for i in list:
    if i%2 == 0:
        result.append(i)

print(result)


new_list = [i for i in list if i%2 == 0]
print(new_list)

b= [1,2,3,4,5]

b_new = [i*i if i%2== 0 else i for i in b]
print(b_new)


a = {'rahim': 12, 'karim': 15, 'salam': 18, 1: [1,2,3,4,5], 2 : {6,7,8,89,9,10}}

for k,v in a.items():
    print(f"key items : {k}, value items : {v}")



x = [1,2,3]
y = ["arafat", "mumpy", "mumtaha"]


print(dict(zip(x,y)))

# dictionary comprehension

num = (range(1,11))

result = { i: "Even" if i % 2 == 0 else "Odd" for i in num }

print(result)