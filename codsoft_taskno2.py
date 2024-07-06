while True:
    a = None
    b = None
    a = eval(input("Enter the first number:"))
    operator= None
    print('''Choose one operator to perform the particular operation:
                    +, -, *, / ''')
    operator=input("Enter the operator: ")
    b=eval(input("Enter the second number: "))
    if operator == '+':
        sum=a + b
        print(f"Sum of {a} and {b} is {sum}")
    elif operator == '-':
        Difference= a-b
        print(f"Difference of {a} and {b} is {Difference}")
    elif operator == '*':
        Product = a*b
        print(f"Product of {a} and {b} is {Product}")
    elif operator == '/':
        Quotient = a/b
        print(f"Quotient of {a} and {b} is {Quotient}")
    Response = None
    Response = input("Do you want to continue? (y/n): ").strip().lower()
    if Response == 'y':
        continue
    else:
        print("Exiting the program")
        break