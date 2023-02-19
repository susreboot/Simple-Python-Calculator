from art import logo, exit, calculator_logo, warning, improper, exit_error
import time
from os import system, name
import sys

# Function for exiting program
def clear():
   # for windows
    if name == 'nt':
        _ = system('cls')

   # for mac and linux
    else:
        _ = system('clear')

# Assign text colors to variables
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
# Print the application logo in green 
print(bcolors.OKGREEN + logo + bcolors.ENDC)
time.sleep(2)
clear()

# Mathmatical formulas functions, according to operators
def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def division(n1, n2):
    if n2 == 0:
        return "Warning!! You cannot Divide by zero!"
    else:
        return n1 / n2

def multiplication(n1, n2):
    return n1 * n2

# Set dictionary for mathmatical operators 
operations = {
    "+": addition,
    "-": subtraction,
    "/": division,
    "*": multiplication
}  

# Calculator function
def calculator(): 
    print(bcolors.OKGREEN + calculator_logo + bcolors.ENDC)
    print("")
    num1 = float(input("What is the first number? \n > "))
    should_continue = True
    while should_continue:
        operation = input("Choose an operator: \n (+) --Addition \n (-) --Subtraction \n (/) --Division \n (*) --Multiplication \n > ")
        num2 = float(input("What is next number? \n > "))
        calculation_function = operations[operation]
        answer = calculation_function(num1, num2)
        if answer == "Warning!! You cannot Divide by zero!":
            clear()
            print(bcolors.RED + warning + bcolors.ENDC)
            time.sleep(2.5)
            clear()
            calculator()
        clear()
        print(bcolors.OKGREEN + f"The Current Calculation is: {num1} {operation} {num2} = {answer}" + bcolors.ENDC)
        print("")
        # Asks the user what they want to do after the first calculation
        decide_step = input(f"Type 'y' or 'yes' to continue calculating with current value: {bcolors.OKGREEN}{answer}{bcolors.ENDC}, \nType 'n' or 'no' to start a new calculation, \nType 'x' or 'exit' to exit the program: " '\n > ').lower() 
        print("")
        if decide_step == "y" or decide_step == "yes":
            num1 = answer
        elif decide_step == "n" or decide_step == "no":
            should_continue = False
            clear()
            calculator()
        elif decide_step == "x" or decide_step == "exit":
            clear()
            print(exit)
            time.sleep(2)
            clear()
            should_continue = False
            break
        # If anything else is entered other than the input above, the program will display a message and exit
        else: 
            clear()
            print(bcolors.RED + improper + bcolors.ENDC)
            print(bcolors.RED + exit_error + bcolors.ENDC)
            time.sleep(3)
            clear()
            sys.exit()  
            should_continue = False
            break

calculator()