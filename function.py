import functools
import os
import pathlib

print("hello")

user_name = input("Enter your name : ")
print(f"Hello, {user_name}!")

mx = max([1,2,3,4,5])
print(f"Maximum value : {mx} , {mx*5}")


# useer define function
def my_function():

    x =[1,2,3,4,5,6,7,8,9,10]

    for i in x:
        if(i%2==0):
            print("Even number")
        else:
            print("Odd number")
    print("Odd number")

my_function()

def add_numbers(a,b):
    print(a+b)

result = add_numbers(5, 3)


def mulpy_numbers(a,b,c):

    return a*b*c

result = mulpy_numbers(2,3,4)
print(result)

def Fuck_you():
    return "Fuck you"

insulting = Fuck_you()
print(insulting)


# arguments

def addition(*nums):
    return sum(nums)
    
r = addition(10,20,34,46,79)
print(r)

# key arguments

def my_func(f_name, l_name, age):

    print(f"Hey! I am {f_name} {l_name}. I am {age} years old.")

my_func(f_name="Nasif", l_name="Avinno", age=25)


# arbitary numbers of keyword arguments

def my_func(**kwargs):

    print(f"Hey! I am {kwargs['f_name']} {kwargs['l_name']}. I am {kwargs['age']} years old. I live in {kwargs['city']}.")

my_func(f_name="Nasif", l_name="Avinno", age=25, city="Dhaka")



# default parameter

def print_name(f_name, l_name ="Khan"):
    print(f_name, l_name)

print_name("Rashid")
print_name("Sakib", "Al Hasan")


# lambda function

sqrt = lambda x : x*x
print(sqrt(5))

students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
sorted_students = sorted(students, key = lambda x : x[1])
print(sorted_students)

students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]

sorted_students = sorted(students, key = lambda x : x[1], reverse = True)

print(sorted_students)


nums = [1,2,3,4,5,6,7,8,9,10]
sqrt_nums =list(map(lambda x : x*x, nums))
print(sqrt_nums)

even = list(filter(lambda x : x%2 == 0, nums))
print(even)

even = list(map(lambda x : x, filter(lambda x : x%2 == 0, nums)))
print(even)


sum = functools.reduce(lambda x,y : x+y, nums)
print(sum)



# scope resolution

x = 10

def func():
    y = 19     # local variable
    x = 200
    print("y =", y)
    print('x =', x)
func()

print('x =', x)



# LEGB Rule
# local, Enclosing, Global, Built-in scope (print,sum,max, input, etc)

n = "Global variable"

def outer():
    n1 = "Enclosing variable"

    def inner():
        global n
        n = "Local variable"
        print(n)

    inner()

    print(n1)

outer()
print(n)


# file handeling

file = open('name.txt', 'r')
content = file.read()
print(content)
file.close()

with open('age.txt', 'r') as f:
    c2 = f.read()
    print(c2)

with open ('name.txt', 'w') as f:
    f.write('Nasif Avinno\n')
    f.write('Nabila\n')
    f.write('Alisha\n')
    f.write('Mrynmoyi\n')

with open ('name.txt', 'a') as f:
    f.write('Nasif Avinno\n')
    f.write('Nabila\n')
    f.write('Alisha\n')
    f.write('Mrynmoyi\n')


lines = ['Nasif Avinno\n', 'Nabila\n', 'Alisha\n', 'Mrynmoyi\n']
with open('name.txt', 'a') as f:
    f.writelines(lines)


if os.path.exists('age.txt'):
    print("File exists")
else:
    print("File does not exist")


if os.path.exists('remove.txt'):
    os.remove('remove.txt')


file_path = pathlib.Path('remove.txt')

if file_path.exists():
    print("File exists")
else:
    print("File does not exist")

if file_path.exists():
    print('File exists')
print(os.path.abspath('name.txt'))
print(os.path.getsize('name.txt'))

with open('name.txt', 'r') as f:
    print(f.tell())
    print(f.read(5))
    print(f.tell())


# Error vs Exception

try:
    

    with open('rahim.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")

try:
    with open('age.txt', 'r') as f:
        print(f.read())

    print(10/10)
except ZeroDivisionError:
    print("Cannot divide by zero")

except FileNotFoundError:
    print("File not found")

    x = int(123)
except ValueError:
    print("Invalid value for conversion to integer")
else:
    print("No exception occurred")


finally:
    print("Must be printed")


def check_file(file_name):         # user made exception
    if not file_name.endswith('.txt'):
        raise ValueError("Invalid file type. Please provide a .txt file.")
    print("File is valid.")

check_file('name.txt')


try:
    check_file('name.txt')
except Exception as e:
    print(e)

