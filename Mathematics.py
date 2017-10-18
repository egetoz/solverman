#imports
from math import ceil
import json

# functions list
mathfunctions = {
    "hy": "calculate hypotenuse given the two other sides of the triangle",
    "qe": "solve quadratic equations (equations of the form ax^2 + bx + c)",
    "av": "given numbers seperated by commas, calculate the average.",
    "isprime": "is the number n prime?",
    "listnprimes": "list n primes",
    "listprimesuntil": "list all the primes until n",
    "exit": "close the program",
    "any mathematical expression": "if you type in a mathematical expression that is not on of the commands listed, the program will automatically solve it for you (example: 12+123*1234)"
}
mainfunctions = {
    "math problems": "solve various math problems",
    "play games": "play a fun game in the command line",
    "exit": "quit the program"
}

#functions
def qe(a, b, c):
    if a != 0 and b != 0 and c != 0:
        if (b ** 2 - 4 * a  *c) < 0:
            return "Can not be solved!"
        x1 = (-b + (b ** 2 - 4 *a *c) ** 0.5 ) / (2 * a)
        x2 = (-b - (b ** 2 - 4*a*c) ** 0.5)  / (2 * a)
        return "The two answers are: " + str(x1) + " and " + str(x2)
    else:
        return "a, b and c must be different than 0"
def hy(l, h):
    if l <= 0 or h <= 0:
        return "Can not be solved"
    else:
        return "The hyptoneuse's length is " + str((l ** 2 + h ** 2) ** 0.5)

def av(array):
    if len(array) > 0:
        return "The average is: " + str(sum(array) / len(array))
    else:
        return "The list is empty" 
#primes
def isprime(n): #dependencies: math.ceil()
    if n == 1:
        return False
    elif n % 2 == 0:
        return False
    for i in range(3, int(ceil(n ** 0.5)), 2):
        if n % i == 0:
            return False
    return True

def listnprimes(n): #dependencies: isprime()
    list = [2]
    cursor = 3
    while len(list) < n:
        if isprime(cursor):
            list.append(cursor)
        cursor += 2
    return list

def listprimeston(n): #dependencies: isprime()
    list = [2]
    cursor = 3
    while cursor < n:
        if isprime(cursor):
            list.append(cursor)
        cursor += 2
    return list
def ismath(str):
    array = ["0","1","2","3","4","5","6","7","8","9","(",")","*","/","-","+"]
    for i in str:
        if i not in array:
            return False
    return True
#init
print "Hi, I am solverman"
name = raw_input("What is your name?: ")

while True:
    q = raw_input("Would you like to solve math problems or play games %s ?: "% (name))
    if q == "math problems":
        while True:
            print "Write 'help' to get a list of commands and 'exit' to exit"    
            q2 = raw_input("Which math problem do you want to solve? (type 'help' to see a list of commands): ")

            if q2 == "help":
                print json.dumps(mathfunctions, indent=4)
            elif q2 == "qe":
                print "Write variables"
                a = float(raw_input("a: ")) 
                b = float(raw_input("b: "))
                c = float(raw_input("c: "))
                print qe(a, b, c)
            elif q2 == "hy":
                l = float(raw_input("l: "))
                h = float(raw_input("h: "))
                print hy(l, h)
            elif q2 == "av":
                array = raw_input("Type in the list of numbers seperated by commas (example: 1,2,3,4,5): ").split(",")
                array = [float(i) for i in array]
                print av(array)
                
            elif q2 == "isprime":
                n = int(raw_input("Type in a number to find out if it's prime: "))
                if isprime(n):
                    print str(n) + " is prime!"
                else:
                    print str(n) + " isn't prime!"
            elif q2 == "listnprimes":
                n = int(raw_input("How many primes do you want to list? "))
                print listnprimes(n)
            elif q2 == "listprimesuntil":
                n = int(raw_input("List all the primes until number: "))
                print listprimesuntil(n)
            elif q2 == "exit":
                print "Bye!"
                exit()
            else:
                if ismath(q2):
                    print "Your answer is " + str(eval(q2))
                else:
                    print "Not a valid command. Type 'help' to see a list of commands"

            print "I hope I could help you."
            q3 = str(raw_input("Would you like to continue?: "))
            if q3 == "yes":
                continue;
            elif q3 == "no": 
                break;
    elif q in ["play a game","play games"]:
        print "Alright do you want to play a game"
    elif q in ["exit","quit","exit()"]:
        print "Bye!"
        exit()
    else:
        print "not a valid command (type 'exit' to exit)"
            
