#Create a function to print first 10 natural numbers
def nat_numbers():
    for i in range (1,11):
        print("The first 10 natural numbers are:",i)

nat_numbers()


#Create a function to calculate sum of first N natural numbers.
N=int(input("enter the number"))
count=1
sum=0
while count<=N:
    sum+=count
    count+=1
    print("The sum of first N natural numbers",sum)

#Create a function to reverse a number.
def rev():
    a=int(input("enter the number"))
    b=int(input("enter the number"))

    temp=a
    a=b
    b=temp
    print("a",a)
    print("b",b)
rev()

#Create a function to count digits in a number.
a=int(input("enter the number"))
num=(len(str(a)))
print("The length of the given number is:",num)

#Create a function to check palindrome number.

num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome number")


#Create a function to generate Fibonacci series.

try:
    n = int(input("Enter the number of terms: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        a, b = 0, 1
        # First two terms
        print("Fibonacci Series:", end=" ")

        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b  # Update values
except ValueError:
    print("Invalid input! Please enter an integer.")



#Calculator Using Functions that contains the following features; User selects operation ;Program performs calculation ;Display result.

#Function for displaying Welcome statement
def hello():
    print("welcome")
hello()

#The sum of the given two numbers 
def add(a,b):
    return a+b
sum=add(7,8)
print(sum)

#The cube of the given number
def cb(x):
    return x**3
cube=cb(3)
print(cube)

#The area of a rectangle
def area():
  a=int(input("enter the number"))
  b=int(input("enter the number"))
  print("area of reactangle",a*b)

area()

#Create a text file and store student details.

file = open("students.txt", "w")

try:
    count = int(input("Enter number of students: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    file.close()
    exit()

for i in range(count):
    print(f"\nEnter details for student {i+1}:")
    name = input("Name: ")
    roll = input("Roll Number: ")
    marks = input("Marks: ")

    file.write(f"Name: {name}, Roll: {roll}, Marks: {marks}\n")

file.close()

print("\nStudent details saved to 'students.txt'")


#Read data from a file.

with open('students','r'):
    content=name
    print(name)
    f.close()

#Handle division by zero using exception handling
try:
    # Take input from user
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))

    # Perform division
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")


#Create a Student class with name and marks
class Student:
    name=input("enter your name")
    marks=int(input("enter your grades"))

s1= Student()
s1.name="Vaibhavi"
s1.marks=97

print("Name",s1.name)
print("marks",s1.marks)
