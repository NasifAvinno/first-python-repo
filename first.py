#chapter - 1

print("fuck you")
print("BITCH")
print("69+96")
print(69+96)
name = "avinno"
age = 23
gender = "sex" 
print(" Name = ", name)
print(" age = ", age)
print(" gender = ", gender)
a = 2
b =3
sum = a + b
print("Sum = ", sum)

name = input("Name = ")
print(name)
age = int(input("Age = "))
print(age)
price = float(input("price = "))
print(price)



if(age >= 18):
    print("Voter")
elif(age < 18):
    print("non voter")
else:
    print("jonmo hoini")

marks = int(input("Marks = "))
if marks >= 90:
    print("A")
elif marks >= 80 and marks <= 89:
    print("B")
elif marks >= 70 and marks <= 79:
    print("C")
elif marks >= 60 and marks <= 69:
    print("D")
elif marks < 60:
    print("F")
else:
    print("Absent")

a=50
b=30
print(a>=b)
print(a<=b)
print(a!=b)
print(a>b)
print(a<b)

num =30
num= num+10
print(num)

pos = input("favourite position : ")
print(pos, "Thats a good one")




#chapter - 2

str1 = "hey! this is Avinno.\n nice to meet u"
print(str1)

str1 = "fuck"
str2 = "you"
len1 = len(str1 + str2)
print(str1 + str2)
print(len1)

str = "Alisha"
print(str[0])
print(str[1])
print(str[1:4])
print(str[-3:-1])
print(str.replace("Alisha", "Avinno"))
print(str.find("A" ))



if (age>=18):
    print("Licence holder")
else:
   print("Not a license holder")


if(age>=18):
       if(age>=60):
          print("can not drive")
       else:
          print("can drive")
else:
       print("can not drive")






 #chapter - 3

marks = [60.6, 78.7, 90.2, 45.6, 37.8]
print(marks)
print(marks[0])
print(marks[4])
print(len(marks))
print(type(marks))
print(marks[0:3])

marks.append(89.6)
print(marks)

marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)

marks.insert(2, 77.9)
print(marks)

marks.remove(78.7)
print(marks)

marks.pop(3)
print(marks)


marks = (60.6, 78.7, 90.2, 45.6, 37.8)
print(marks)
print(marks[0])
print(marks[4])
print(len(marks))
print(type(marks))
print(marks[0:3])

marks.index(90.2)
print(marks.index(90.2))

marks.count(90.2)
print(marks.count(90.2))

list1 = [1,2,3,2,1]
list2 = list1.copy()

list2.reverse()

if(list1 == list2):
    print("Palindriome")
else:
    print("Not Palindrome")



#chapter - 4

info = {
    "key" : "value",
    "name" : "Avinno",
    "age" : 23,
    "price" : 35000,
    "Learning" : "Python",
    "Topic" : ("dictionary", "set"),
}
print(info)
info[name] = "Alisha"
print(info)

student = {
    "name" : "Avinno",
    "sub" : {
        "Math" : 90,
        "Physics" : 85,
        "Chemistry" : 80,
    }
}
print(student)

new_student = {"name" : "Avash", "age" : 22}
student.update(new_student)
print(student)


num = {1,2,3,4,5, "alisha", "nabila"}
print(num)
print(type(num))
num.add(6)
print(num)
num.remove(3)
print(num)
num.pop()
print(num)
num.clear()
print(num)



#chapter - 5

i=1
while i<=10:
    print(i)
    i +=1

i=10
while i>=1:
    print(i)
    i -=1

n = int(input("Enter n :"))
i=1
while i<=10:
    print(n*i)
    i +=1

i=1
while i<=10:
    print(i*i)
    i += 1

x = int(input("Enter x :"))
i=1
while i<=10:
    if(i==3):
        continue
    print(i*i)
    if(i*i == x*x):
        print("Found!")
        break
    else:
        print("Not Found!")
    i +=1



for i in range(1, 11):
    print(i * i)


x = int(input("Enter x: "))

found = False

for i in range(1, 11):
    if i == 3:
        continue
    
    square = i * i
    print(square)
    
    if square == x*x:
        print("Found!")
        found = True
        break

if not found:
    print("Not Found!")





#chapter - 6


a= int(input("Enter a :"))
b= int(input("Enter b :"))
def sum(a,b):
    sum = a+b
    print("sum = ", sum)
    return sum
sum(a,b)

n =int (input("Enter n :"))
def fac(n):
    for i in range(1,n+1):
        n=n*i
    return n
print("Factorial = ", fac(n))

fac(n)

n =int (input("Enter n :"))   #using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
def sum(n):
    if n==0:
        return 0
    else :
        return n + sum(n-1)

sum = sum(10)
print(sum)







#chapter - 7


import os
from tracemalloc import start 

f = open("demo.txt", "w+")
f.write("Go and learn Python\n")

f.seek(0)
data = f.read() 
print(data)

f.seek(0) 
print(f.read())

print(f.write("Another line\n")) 
print(type(data))

f.close() 


if os.path.exists("sample.txt"):
    os.remove("sample.txt")


with open("practice.txt", "w") as f:
    f.write("This is a practice file.\n")
    f.write("I'm learning python.\n")
    f.write("1,2,3,4,5,6,7,8,9\n")


with open("practice.txt", "r") as f:
    data = f.read()


ND = data.replace("practice", "advanced")

with open("practice.txt", "w") as f:
    f.write(ND)

print(ND)


word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if word in data:
        print("found\n")
    else:
        print("not found\n")






  #chapter - 8

class Car:
    tag = "Best car Company"

    def __init__(self, name, colour, speed, price):
        self.name = name
        self.color = colour
        self.speed = speed
        self.price = price

    def get_info(self):
        return self.name, self.color, self.speed, self.price


car1 = Car("BMW", "Black", 200, 50000)
car2 = Car("Audi", "White", 220, 60000)
car3 = Car("Mercedes", "Silver", 250, 70000)

print(car1.name)
print(car1.color)
print(car1.speed)
print(car1.price)
print(car1.tag)
print(car1.get_info())

print(car2.name)
print(car2.color)
print(car2.speed)
print(car2.price)
print(car2.tag)
print(car2.get_info())

print(car3.name)
print(car3.color)
print(car3.speed)
print(car3.price)
print(car3.tag)
print(car3.get_info())

@staticmethod
def car_info():
    print("Awkat ka bahar haen\n")


class car:                              #abstraction
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clt = False

    def start(self):
        self.acc = True
        self.clt = True
        print("car started...\n")
    
car1 = car()
car1.start()


class Account:
    def __init__(self, bal, acc, password):
        self.balance = bal
        self.account_no = acc
        self.__password = password

    def check_password(self, password):
        return self.__password == password

    def debit(self, amount, password):
        if self.check_password(password):
            self.balance -= amount
            print("Debited", amount, "from account no", self.account_no)
            print("Total balance =", self.balance)
        else:
            print("Wrong password!")

    def credit(self, amount, password):
        if self.check_password(password):
            self.balance += amount
            print("Credited", amount, "to account no", self.account_no)
            print("Total balance =", self.balance)
        else:
            print("Wrong password!")

    def get_balance(self, password):
        if self.check_password(password):
            return self.balance
        else:
            return "Access denied"
        
acc1 = Account(10000, 12345, "Alishanabila10")
acc1.debit(3200, "Alishanabila10") 
acc1.credit(2000, "Alishanabila10") 

acc2 = Account(25000, 678910, "0442Alishanabila10") 
acc2.debit(5000, "0442Alishanabila10") 
acc2.credit(1000, "0442Alishanabila10") 

print(acc1.balance) 
print(acc1.account_no) 
print(acc1._Account__password) 
print("Total balance =", acc1.get_balance("Alishanabila10")) 

print(acc2.balance) 
print(acc2.account_no) 
print(acc2._Account__password) 
print("Total balance =", acc2.get_balance("0442Alishanabila10")) 



class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started...\n")

    @staticmethod
    def stop():
        print("car stopped...\n")


class BMW(Car):
    def __init__(self, model, mileage, price, type):
        super().__init__(type)   # call parent constructor
        self.model = model
        self.mileage = mileage
        self.price = price


class X5(BMW):
    def __init__(self, model, mileage, price, type):
        super().__init__(model, mileage, price, type)


class X3(BMW):
    def __init__(self, model, mileage, price, type):
        super().__init__(model, mileage, price, type)


car1 = X5("X5", 20, 50000, "electric")
car2 = X3("X3", 25, 45000, "petrol")

print("car1 model :", car1.model)
print("car1 mileage :", car1.mileage)
print("car1 price :", car1.price)
print("car1 type :", car1.type)
car1.start()

print("car2 model :", car2.model)
print("car2 mileage :", car2.mileage)
print("car2 price :", car2.price)
print("car2 type :", car2.type)
car2.stop()


class person():
    name = "Avinno"

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name

p1 =person()
p1.change_name("Alisha")
print(p1.name)


class student():
    def __init__(self, phy, chem, bio, math):
        self.phy = phy
        self.chem = chem
        self.bio = bio
        self.math = math

    @property
    def percentage(self):
        total = self.phy + self.chem + self.math + self.bio
        return total / 4
    
s1 = student(90,86,98,88)
print("percentage =", s1.percentage)

s1.phy = 98
print("New percentage =", s1.percentage)



class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real, "+", self.img, "i")

    def __add__(self, num2):
        real_sum = self.real + num2.real
        img_sum = self.img + num2.img
        return Complex(real_sum, img_sum)   


num1 = Complex(2, 3)
num2 = Complex(7, 9)

num3 = num1 + num2

num1.showNum()
num2.showNum()
num3.showNum()


# end of learning python