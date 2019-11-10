import sys
import math
import os
print('''
Author: Nashiro-Chan
Github: Nashiro-Chan
Discord: @Asuka#1935
Date of latest edit: 10/11/2019
''')
print("(Fullscreen recommended)")
password = input("\nEnter the password: \n")

if password == "1234":
    print("ACCESS GRANTED!")
    print('''
 ________  ________  ___       ________  ___  ___  ___       ________  _________  ________  ________     
|\   ____\|\   __  \|\  \     |\   ____\|\  \|\  \|\  \     |\   __  \|\___   ___\\   __  \|\   __  \    
\ \  \___|\ \  \|\  \ \  \    \ \  \___|\ \  \\\  \ \  \    \ \  \|\  \|___ \  \_\ \  \|\  \ \  \|\  \   
 \ \  \    \ \   __  \ \  \    \ \  \    \ \  \\\  \ \  \    \ \   __  \   \ \  \ \ \  \\\  \ \   _  _\  
  \ \  \____\ \  \ \  \ \  \____\ \  \____\ \  \\\  \ \  \____\ \  \ \  \   \ \  \ \ \  \\\  \ \  \\  \| 
   \ \_______\ \__\ \__\ \_______\ \_______\ \_______\ \_______\ \__\ \__\   \ \__\ \ \_______\ \__\\ _\ 
    \|_______|\|__|\|__|\|_______|\|_______|\|_______|\|_______|\|__|\|__|    \|__|  \|_______|\|__|\|__|
    Version 2                                                                                                    
    Author GitHub: Nashiro-Chan

    All possible operators:   
    *===========Basic==========*    *===========Other==========*
    ||Plus         |   +      ||    ||Powers       |   ^      ||
    ||Minus        |   -      ||    ||square root  |   sqrt   ||
    ||Divide       |   /      ||    *==========================*
    ||Multiply     |   *      ||
    *==========================*
    
    *=========Angular conversion=========*
    ||radians to degrees     |   rtd    ||
    ||degrees to radian      |   dtr    ||
    *====================================*
    
    *======Trigonometric functions=======*
    ||cosine     |    cos               ||
    ||sine       |    sin               ||
    ||tangent    |    tan               ||
    *====================================*
    
    ''')
    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    if op != "sqrt" and op != "rtd" and op != "dtr" and op != "cos" and op != "sin" and op != "tan" and op != "pi" and op != "e":
        num2 = float(input("Enter second number: "))
    if op == "+":
        result = num1 + num2
        print(str(num1) + " " + op + " " + str(num2) + " = " + str(result))
    elif op == "-":
        result = num1 - num2
        print(str(num1) + " " + op + " " + str(num2) + " = " + str(result))
    elif op == "/":
        result = num1 / num2
        print(str(num1) + " " + op + " " + str(num2) + " = " + str(result))
    elif op == "*":
        result = num1 * num2
        print(str(num1) + " " + op + " " + str(num2) + " = " + str(result))
    elif op == "^":
        result = num1 ** num2
        print(str(num1) + " " + op + " " + str(num2) + " = " + str(result))
    elif op == "sqrt":
        result = math.sqrt(num1)
        print("The root square of " + str(num1) + " Is " + str(result))
    elif op == "rtd":
        result = math.degrees(num1)
        print(str(num1) + " radians, to degrees = " + str(result))
    elif op == "dtr":
        result = math.radians(num1)
        print(str(num1) + " degrees, to radians = " + str(result))
    elif op == "cos":
        result = math.cos(num1)
        print("The cosine of " + str(num1) + " = " + str(result))
    elif op == "sin":
        result = math.sin(num1)
        print("The sine of " + str(num1) + " = " + str(result))
    elif op == "tan":
        result = math.tan(num1)
        print("The tangent of " + str(num1) + " = " + str(result))
else:
    print("ACCESS DENIED!")
    sys.exit()

print(" ")
input("[Press ENTER to close calculator]")