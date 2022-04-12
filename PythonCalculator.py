#PythonCalculator made by Stelios Miskedakis 27/03/22 

#Packages
import time
import math
import sys


#The Maths
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
def pi():
    return math.pi
def modulus(num1, num2):
    return num1 % num2
def exponentiation(num1, num2):
    return num1 ** num2
def floordivision(num1, num2):
    return num1 // num2


#The Calculation
def calculation():
 while True:
    choice = input("Select(1/2/3/4/5/6/7/8/9/10/11/12): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'):
        if choice == '1':
            num1 = float(input("Enter your 1st number: "))
            num2 = float(input("Enter your 2nd number: "))
            print(num1, '+', num2, '=', add(num1, num2))
        elif choice == '2':
            num1 = float(input("Enter your 1st number: "))
            num2 = float(input("Enter your 2nd number: "))
            print(num1, '-', num2, '=', subtract(num1, num2))
        elif choice == '3':
            num1 = float(input("Enter your 1st number: "))
            num2 = float(input("Enter your 2nd number: "))
            print(num1, '*', num2, '=', multiply(num1, num2))
        elif choice == '4':
            num1 = float(input("Enter your 1st number: "))
            num2 = float(input("Enter your 2nd number: "))
            print(num1, '/', num2, '=', divide(num1, num2))
        elif choice == '5':
            print(math.pi)
        elif choice == '6':
            num1 = float(input("Enter your 1st number: "))
            num2 = float(input("Enter your 2nd number: "))
            print(num1, '%', num2, '=', modulus(num1, num2))
        elif choice == '7':
            num1 = float(input("Enter your 1st number: "))
            num2 = float(input("Enter your 2nd number: "))
            print(num1, '**', num2, '=', exponentiation(num1, num2))
        elif choice == '8':
            num1 = float(input("Enter your 1st number: "))
            num2 = float(input("Enter your 2nd number: "))
            print(num1, '//', num2, '=', floordivision(num1, num2))
        elif choice == '9':
            num1 = float(input("Enter your 1st number: "))
            print(f"Square Root of {num1} is ", '=', math.sqrt(num1))
        elif choice == '10':
            num1 = float(input("Enter your 1st number: "))
            print(f"Cos of {num1} is ", '=', math.cos(num1))
        elif choice == '11':
            num1 = float(input("Enter your 1st number: "))
            print(f"Sin of {num1} is ", '=', math.sin(num1))
        elif choice == '12':
            aboutme = "Hello programmers, if you are running this program thank you very much since this is my first Python project , I made this program on March 27, 2022 as a 16 year old teenager. My name is Stelio Miskedakis and my dream is to become a web developer in a big company. I put in a lot of work to do as many projects as I can to practice my skills to become a successful programmer. If you like the program or not, I really appreciate it."
            print(aboutme)
        another_calculation = input("Do you want another calculation? (yes/no)")
        if another_calculation == "no":
            print("Have a good time")
            break

    else:
        print("Invalid Input")
        sys.exit()

#The Calculator
def Calculator():
    print("Select Operation.")
    print("1. for add +")
    print("2. for subtract -")
    print("3. for multiply *")
    print("4. for divide /")
    print("5. for pi 3.14")
    print("6. for modulus %")
    print("7. for exponentiation **")
    print("8. for floordivision //")
    print("9. for squareroot")
    print("10.for cos")
    print("11.for sin")
    print("12. Learn About me")
    calculation()

#The Start
def start():
    time.sleep(0.5)
    startnow = input("Do you want to start? Answer with yes or no: ")
    print(startnow)
    if startnow == 'yes':
        Calculator()
    else:
        print("Have a nice day")
        sys.exit()

#The Intro
def intro():
    welcome = "Welcome! The Python Calculator is made by Stelios Miskedakis"
    print(welcome)
    time.sleep(0.5)
    start()


#The 1st intro
intro1 = input("Start?(yes/no): ")
if intro1 == 'yes':
    intro()
else:
    print("Have a good time")
    sys.exit()
