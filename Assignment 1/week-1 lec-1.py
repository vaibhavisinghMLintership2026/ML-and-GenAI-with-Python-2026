#week -1 Lect-1
#Assignment

#find the area of rectangle
a=int(input("enter the first side"))
b=int(input("enter the second side"))
area=a*b
print("the area of Rectangle is:",area)

#find simple interest
P=int(input("enter the Principle Amount"))
R=int(input("enter the rate of interest"))
T=int(input("enter the duration/time"))
SI=P*R*T/100
print("the simple interest is",SI)

#Convert temperature from celsius to fahrenheit
C=int(input("enter the temperature in celsius"))
F=(C*(9/5))+32
print("the temperature in Fahrenheit is:",F)

#Calculate average of 3 numbers
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
avg=(a+b+c)/3
print("the average of three given numbers are",avg)

#find square and cube of a number
x=int(input("enter the number"))
sq=x**2
cb=x**3
print("the square of the given number is:",sq ,"the cube of the given number is:", cb)

#Swap two numbers without third variable.
a=int(input("enter the number"))
b=int(input("enter the number"))
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b=",b)

#Create a student report program that take student details using input(),Store marks in variable ,Calculate total and percentage ,Use comments, Use proper identation

name=input("enter student's name")
ID=int(input("enter the student's id"))
python_score=int(input("enter the student's marks"))
WAD_score=int(input("enter the student's marks"))
EVS_score=int(input("enter the student's marks"))
maths_score=int(input("enter the student's marks"))
physics_score=int(input("enter the student's marks"))
#total score of an individual student
total=python_score+WAD_score+EVS_score+maths_score+physics_score
#percentage score of an individual student
percentage=total/5
print("the total marks obtained",total)
print("percentage score:",percentage)


