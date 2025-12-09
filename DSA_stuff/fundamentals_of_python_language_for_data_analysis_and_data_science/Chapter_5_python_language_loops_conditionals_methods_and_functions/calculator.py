# Calculator v 0.1

# Factorial function
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    
    return fact

while True:

    # Menu
    menu = """
    ------------------- Welcome to your new Python calculator -------------------

    1- Addition +
    2- Subtraction -
    3- Multiplication x
    4- Division /
    5- Potentiation ²
    6- Factorial !

    7- Exit
    """
    print(menu)
    
    option = int(input("Select one of the options: "))
    if option == 7:
        print("Thank you for using our calculator!! We hope to see you soon...")
        break
    elif option == 5:
        n1 = int(input("Type the number to pontentiation: "))
        n2 = int(input("And type the number to be the potention: "))
        # Potentiation lambda function
        potentiation = lambda n1,n2: n1**n2
        print(f"The potentiation of {n1} in {n2} is {potentiation(n1,n2)}!")
        
    elif option == 6:
        n1 = int(input("Type the number to factorial: "))
        print(f"The factorial of {n1} is {factorial(n1)}!")
    
    elif option not in [1,2,3,4,5,6,7]:
        print("Please, type a valid option!")
    
    else:
        n1 = int(input("Type the first number: "))
        n2 = int(input("Type the second number: "))
        
        if option == 1:
            # Addition lambda function
            addition = lambda n1,n2: n1+n2
            print(f"{n1} + {n2} = {addition(n1,n2)}")
            
        elif option == 2:
            # Subtraction lambda function
            subtraction = lambda n1,n2: n1-n2  
            print(f"{n1} - {n2} = {subtraction(n1,n2)}")

        elif option == 3:
            # Multiplication lambda function
            multiplication = lambda n1,n2: n1*n2  
            print(f"{n1} x {n2} = {multiplication(n1,n2)}")

        elif option == 4:
            # Division lambda function
            division = lambda n1,n2: n1/n2  
            print(f"{n1} / {n2} = {division(n1,n2)}")
