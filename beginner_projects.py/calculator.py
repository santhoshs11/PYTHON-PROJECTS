print("""____________CALCULATOR____________""")
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2


repeat = True

while  repeat:
    num1 = int(input("\nenter first number : "))
    num2 = int(input("\nenter second number : "))

    choice = input("\nenter your choice (add/sub/multiply/divide): ").lower()
    if choice == 'add':
        print(f"answer : {add(num1,num2)}")
    elif choice == 'sub':
        print(f"answer : {sub(num1,num2)}")
    elif choice == 'multiply':
        print(f"answer : {multiply(num1,num2)}") 
    elif choice == 'divide':
        print(f"answer : {divide(num1,num2)}")           
    else:
        print("INVALID CHOICE....!!")

    an = input("do u want to continue...").lower()
    if an =='no':
        repeat = False
    else :
        repeat = True    