def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b !=0:
        return a/b
    else:
        print("division by Zero is invalid") 
def mod(a,b):
    return a%b

choice=int(input("""
            1. Enter 1 for addition
            2. Enter 2 for substraction
            3. Enter 3 for multipication
            4. Enter 4 for division
            5. Enter 5 for to get mod
            """))


a=float(input("Enter the first no. -> "))
b=float(input("Enter the second no. -> "))

if choice==1:
    print("Addition")
    print("--------------------------")
    print(add(a,b))
elif choice == 2:
    print("substraction")
    print("--------------------------")
    print(sub(a,b))
elif choice == 3:
    print("Multiplication")
    print("--------------------------")
    print(mul(a,b))
elif choice == 4:
    print("Division")
    print("--------------------------")
    print(div(a,b))
elif choice == 5:
    print("modulus")
    print("--------------------------")
    print(mod(a,b))
else:
    print("Invalid Choice!!")