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

    