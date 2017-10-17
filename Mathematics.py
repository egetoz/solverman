print "Hi, I am solverman"

name = str(raw_input("What is your name?: "))
q = str(raw_input("Would you like to solve math problems or play games %s ?: "% (name)))
if q == "math problems":
    while True:    
        q2 = str(raw_input("So you want to solve math problems, which math problem you want to solve?(quadric_equation(qe) or hypotenuse(hy) or exit (exit) ): "))

        if q2 == "qe":
            print "Write variables"
            a = int(raw_input("a: ")) 
            b = int(raw_input("b: "))
            c = int(raw_input("c: "))
            if a != 0 and b != 0 and c != 0:
                if (b ** 2 - 4 *a *c) < 0:
                    print "Can not be solved"
                    continue;
                x1 = (-b + (b ** 2 - 4 *a *c) ** 0.5 ) / (2 * a)
                x2 = (-b - (b ** 2 - 4*a*c) ** 0.5)  / (2 * a)
                print x1, x2 
                print "I hope I could help you."
                q3 = str(raw_input("Would you like to continue?: "))
                if q3 == "yes":
                    continue;
                if q3 == "no": 
                    break;




            else: 
                print "a * b * c must be greater than 0" 
        if q2 == "hy":

            l = int (raw_input("l: "))
            h = int (raw_input("h: "))

            (d) = ((l * l) + (h * h)) ** 0.5
            print "Hypotenuse is %s" % (d) 
            print "I hope I could help you."
            q3 = str(raw_input("Would you like to continue?: "))
            if q3 == "yes":
                continue;
            if q3 == "no": 
                break;
        
        if q2 == "exit":
            break;
if q in ["play a game","play games"]:
    print "Alright do you want to play a game"
print "Bye!"
        
