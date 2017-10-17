# functions list
mathfunctions = {
    "hy": "calculate hypotenuse given the two other sides of the triangle",
    "qe": "solve quadratic equations (equations of the form ax^2 + bx + c)"
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
#init
print "Hi, I am solverman"
name = raw_input("What is your name?: ")

while True:
    q = raw_input("Would you like to solve math problems or play games %s ?: "% (name))
    if q == "math problems":
        while True:    
            q2 = raw_input("So you want to solve math problems, which math problem you want to solve?(quadratic equations(qe) or hypotenuse(hy) or exit (exit) ): ")

            if q2 == "qe":
                print "Write variables"
                a = float(raw_input("a: ")) 
                b = float(raw_input("b: "))
                c = float(raw_input("c: "))
                print qe(a, b, c)
                print "I hope I could help you."

                q3 = str(raw_input("Would you like to continue?: "))
                if q3 == "yes":
                    continue;
                if q3 == "no": 
                    break;
            elif q2 == "hy":
                l = float(raw_input("l: "))
                h = float(raw_input("h: "))
                print hy(l, h)
                print "I hope I could help you."

                q3 = str(raw_input("Would you like to continue?: "))
                if q3 == "yes":
                    continue;
                if q3 == "no": 
                    break;
            
            elif q2 == "exit":
                break;
    elif q in ["play a game","play games"]:
        print "Alright do you want to play a game"
    elif q in ["exit","quit","exit()"]:
        print "Bye!"
        break
    else:
        print "not a valid command (type 'exit' to exit)"
            
