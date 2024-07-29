import time

def collatz(number):
    
    if (number % 2 == 0):
        #print("Number is even")
        result = (number // 2)
        print(result)
    
    elif (number % 2 == 1):
        #print("Number is odd")
        result = (3 * number + 1)
        print(result)    
    return result

def getinput():
    while True:
        try:
            sequence = []
            user_input = int(input("Please enter an integer: "))
            time.sleep(1.5)
            print("Processing...")
            if user_input <= 0:
                raise ValueError
            
            time.sleep(3)
            print(user_input)
            while user_input != 1:
                sequence.append(user_input)
                user_input = collatz(user_input) 
                time.sleep(1) 
            sequence.append(1)
            print(f"Collatz Sequence: {sequence}")         
            break  

        except ValueError:
            time.sleep(3)
            print("An error occured: Input Must be a non-zero positive integer.")    



def area_of_a_Cirle():
    print("\nSet to find the Area of your circle?")
    uservalue = input("Press 'r' to input radius or 'd' to input diameter: ")
    while True:
        if (uservalue == "r") or (uservalue == "R"):
            print("Area of a circle, A = πr²;\nWhere r = radius of the circle")
            print("Value of π = 3.14\n")
            userinput = int(input("Enter the radius of your circle: "))
            area = 3.14*userinput**2
            result = float(area)
            print(f"The Area of your circle with radius {userinput}cm is: {result}cm²")
            break    
        elif (uservalue == "d") or (uservalue == "D"):
            print("Area of a circle, A = ¼πd²\nWhere d = diameter of the circle")
            print("Value of π = 3.14\n")
            userinput = int(input("Enter the diameter of your circle: "))
            area = 3.14*(userinput/2)**2
            result = float(area)
            print(f"The Area of your circle with diameter {userinput}cm is: {result}cm²")
            break
        else:
            if uservalue:
                time.sleep(3)
                print("Invalid input!")
                time.sleep(2)
                area_of_a_Cirle()
            else:
                print("No input provided")
            break

username = input("Welcome!\nPlease enter your name: ")
if username == "":
    username = "USER"
def greet():
    print(f"Welcome {username.capitalize()}!, Please choose which operation to perform:")
    operation = input("C: Collatz Sequence, A: Area of a Circle\n")
    operation = operation.upper()
    
    if operation == "C":
        print("\nCOLLATZ SEQUENCE:")
        getinput()

    elif operation == "A":
        print("\nAREA OF A CIRCLE:")
        area_of_a_Cirle()
    else:
        if operation:
            print("Invalid input!\n")
            greet()
        else:
            print("No input detected!\n")
            greet()

greet()
