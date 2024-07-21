print("Thank you for choosing Python Pizza Deliveries!")
size1 = input('SIZE : ')
size = size1.upper()
add_pepperoni1 = input('do you want pepperoni ? : ')
add_pepperoni = add_pepperoni1.upper() 
extra_cheese1 = input('Add extra cheese : ')
extra_cheese = extra_cheese1.upper()

price=0
if size=="S" :
  price=15
  if add_pepperoni=="Y":
    price+=2
  else:
    price=15
elif size=="M":
  price=20
  if add_pepperoni=="Y":
    price+=3
  else:
    price=20
elif size =="L":
  price=25
  if add_pepperoni=="Y":
    price+=3
  else:
    price=25

if extra_cheese == "Y":
  price+=1
  
print(f"Your final bill is: ${price}.")
