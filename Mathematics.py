#imports
from math import ceil
import random
import json
import urllib
import __future__
import os

# functions list
mathfunctions = {
    "Mathematics":{
        "hy": "calculate hypotenuse given the two other sides of the triangle",
        "qe": "solve quadratic equations (equations of the form ax^2 + bx + c)",
        "av": "given numbers seperated by commas, calculate the average.",
        "isprime": "is the number n prime?",
        "listnprimes": "list n primes",
        "listprimesuntil": "list all the primes until n",
        "any mathematical expression": "if you type in a mathematical expression that is not on of the commands listed, the program will automatically solve it for you (example: 12+123*1234)"
    },
    "Science": {
        "p": "find density from the formula p = m / V",
        "m": "find mass from the formula p = m / V",
        "V": "find volume from the formula p = m / V"
    },
    "Other": {
        "exit": "close the program"
    }
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
def ismath(string):
    array = ["0","1","2","3","4","5","6","7","8","9","(",")","*","/","-","+"]
    for i in [i for i in string if i != " "]:
        if i not in array:
            return False
    if len([i for i in string if i != " "]) != 0:
        return True
    else:
        return False
def m(p, V):
    return "The mass is: " + str(p * V)
def p(m, V):
    return "The density is: " + str(m / V)
def V(p, m):
    return "The volume is: " + str(m / p) 
def W(F, d):
    return "The Work is: " + str(F * d)
def F(W, d):
    return "The Force is: " + str(W / d)
def d(W, F):
    return "The Distance is: " + str(W / F)
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
            elif q2 == "p":
                m = float(raw_input("Enter mass: "))
                V = float(raw_input("Enter volume: "))
                if m != 0 and V != 0:
                    print pmvp(m, V)
                else:
                    print "The variables can not be 0"
            elif q2 == "m":
                p = float(raw_input("Enter density: "))
                V = float(raw_input("Enter volume: "))
                if p != 0 and V != 0:
                    print m(p, V)
                else:
                    print "The variables can not be 0"
            elif q2 == "V":
                m = float(raw_input("Enter mass: "))
                p = float(raw_input("Enter density: "))
                if m != 0 and p != 0:
                    print V(p, m)
                else:
                    print "The variables can not be 0" 
            elif q2 == "W":
                F = float(raw_input("Enter Force: "))
                d = float(raw_input("Enter Distance: ")) 
                if F != 0 and d != 0:
                    print W(F, d)
                else:
                    print "The variables can not be 0"
            elif q2 == "F":
                W = float(raw_input("Enter Work: "))
                d = float(raw_input("Enter Distance: "))
                if W != 0 and d != 0:
                    print F(W, d)
                else:
                    print "The variables can not be 0"
            elif q2 == "d":
                W = float(raw_input("Enter Work: "))
                F = float(raw_input("Enter Force: "))
                if W != 0 and F != 0:
                    print d(W, F)
                else:
                    print "The variables can not be 0"
            elif q2 == "exit":
                print "Bye!"
                exit()
            else:
                if ismath(q2):
                    print "Your answer is " + str(eval(compile("".join([i for i in q2 if i != " "]), '<string>', 'eval', __future__.division.compiler_flag)))
                else:
                    print "Not a valid command. Type 'help' to see a list of commands"

            print "I hope I could help you."
    elif q in ["play a game","play games"]:
        quizinput = raw_input("Here's a quiz game for you. There are 85 questions that will be randomly given to you, they are categorized easy, medium and hard. Easy questions gain 1 points, medium 2 points and hard 3 points. Type in anything to begin, 'exit' to exit and 'back' to go back.: ")
        if quizinput == "back":
            continue
        elif quizinput == "exit":
            print "Bye!"
            exit()
        else:
            thisfolder = os.path.dirname(os.path.abspath(__file__))
            myfile = os.path.join(thisfolder, 'trivia.json')
            trivia = open(myfile, "r")
            data = json.loads(trivia.read())["results"]
            random.shuffle(data)
            trivia.close()
            score = 0
            for i in range(len(data)):
                print "Question number " + str(i + 1) + ":"
                print data[i]["question"]
                choices = [data[i]["correct_answer"]] + data[i]["incorrect_answers"]
                random.shuffle(choices)
                print "A) " + choices[0]
                print "B) " + choices[1]
                print "C) " + choices[2]
                print "D) " + choices[3]
                while True:
                    quizanswer = raw_input("Which one do you choose? A, B, C or D?: ")
                    if quizanswer in "Aa":
                        if choices[0] == data[i]["correct_answer"]:
                            if data[i]["difficulty"] == "easy":
                                score += 1
                            elif data[i]["difficulty"] == "medium":
                                score += 2
                            elif data[i]["difficulty"] == "hard":
                                score += 3
                            print "You are absolutely correct! Your new score is " + str(score)
                            break
                        else:
                            print "You are WRONG! Your score is still " + str(score)
                            break
                    elif quizanswer in "Bb":
                        if choices[1] == data[i]["correct_answer"]:
                            if data[i]["difficulty"] == "easy":
                                score += 1
                            elif data[i]["difficulty"] == "medium":
                                score += 2
                            elif data[i]["difficulty"] == "hard":
                                score += 3
                            print "You are absolutely correct! Your new score is " + str(score)
                            break
                        else:
                            print "You are WRONG! Your score is still " + str(score)
                            break
                    elif quizanswer in "Cc":
                        if choices[2] == data[i]["correct_answer"]:
                            if data[i]["difficulty"] == "easy":
                                score += 1
                            elif data[i]["difficulty"] == "medium":
                                score += 2
                            elif data[i]["difficulty"] == "hard":
                                score += 3
                            print "You are absolutely correct! Your new score is " + str(score)
                            break
                        else:
                            print "You are WRONG! Your score is still " + str(score)
                            break
                    elif quizanswer in "Dd":
                        if choices[3] == data[i]["correct_answer"]:
                            if data[i]["difficulty"] == "easy":
                                score += 1
                            elif data[i]["difficulty"] == "medium":
                                score += 2
                            elif data[i]["difficulty"] == "hard":
                                score += 3
                            print "You are absolutely correct! Your new score is " + str(score)
                            break
                        else:
                            print "You are WRONG! Your score is still " + str(score)
                            break
                    else:
                        print "Not a valid answer, type only A, B, C or D."
                contprompt = raw_input("Wanna continue?: ")
                if contprompt == "no":
                    break
            print "End of trivia! You scored " + str(score)

    elif q in ["exit","quit","exit()"]:
        print "Bye!"
        exit()
    else:
        print "not a valid command (type 'exit' to exit)"
            
