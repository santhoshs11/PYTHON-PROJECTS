import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','?','/','<','>']

u_letter = int(input("How many letters in password : "))
u_number = int(input("How many numbers in password : "))
u_symbol = int(input("How many symbols in password : "))

passwordlist = []
for p in range(1,u_letter+1):
    passwordlist.append(random.choice(letters))
   
for p in range(1,u_number+1):
    passwordlist.append(random.choice(numbers))
  
for p in range(1,u_symbol+1):
    passwordlist.append(random.choice(symbols))

random.shuffle(passwordlist)   

password = ""
for char in passwordlist: 
    password+=char
print(f"YOUR PASSWORD IS  : {password}")    


