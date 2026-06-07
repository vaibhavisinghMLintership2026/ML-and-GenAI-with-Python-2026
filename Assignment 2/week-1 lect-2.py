#Find sum of first 10 natural numbers.
count=1
sum=0
while count<=10:
    sum+=count
    count+=1
    print("the sum of first 10 natural numbers are:",sum)

#Find factorial of a number
num=int(input("enter the number"))
count=1
fact=1
while count<=num:
    fact*=count
    count+=1
    print("the factorial of the given number is:",fact)

a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))

# Fibonacci series 
try:
    n = int(input("Enter the number of terms: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        a, b = 0, 1  # First two terms
        print("Fibonacci Series:", end=" ")

        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b  # Update values
except ValueError:
    print("Invalid input! Please enter an integer.")


#Find largest among 3 numbers
if (a>b and a>c):
    print("the largest number among the 3 is:",a)
elif (b>a and b>c):
    print("the largest number among the 3 is:",b)
elif (c>a and c>b):
    print("the largest number among the 3 is:",c)
else:
    print("none is greater")

#Create Student Result System  Reverse a number
#Input student details Input marks Calculate percentage Display grade Use: if-elif-else loops
num=int(input("enter the no. of stud"))
for i in range(num):
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
    print("the name of student",name)
    print("the total marks obtained",total)
    print("percentage score:",percentage)


























