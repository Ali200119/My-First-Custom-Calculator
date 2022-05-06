# Calculator

from colorama import init
from colorama import Fore, Back, Style

init()

What = input("What we will do, my friend? (+, -, *, /): ")

a = float(input("write first number: "))
b= float(input("write second number: "))

if What == "+":
    c = a + b
    print("Result: " + str(c))

elif What == "-":
    c = a - b
    print("Result: " + str(c))

elif What == "*":
    c = a * b
    print("Result: " + str(c))

elif What == "/":
    c = a / b
    print("Result: " + str(c))

print("Have a nice day!")

input()