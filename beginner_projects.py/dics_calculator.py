def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def div(a,b):
    return a/b

operations ={
    '+': add,
    '-': sub,
    '*':multiply,
    '%': div
}
for symbol in operations:
    print(symbol)

num1 = int(input('first no : ')) 
choose_operator =input('choose the operation :')   
num2 =int(input('second no: '))

ans = operations[choose_operator]
answer = ans(num1,num2)

print(f'{num1} {choose_operator} {num2} = {answer}')
cont = input(f'do you continue with {answer} or not ? ')
if cont == "yes":
    num1=answer
    choose_operator =input('choose the operation :')   
    num2 =int(input('second no: '))
    ans = operations[choose_operator]
    answer = ans(num1,num2)
    print(f'{num1} {choose_operator} {num2} = {answer}')
    
    