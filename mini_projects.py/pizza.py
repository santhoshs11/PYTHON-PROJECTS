print("Thank you for choosing Python Pizza Deliveries!")
size = input() 
add_pepperoni = input() 
extra_cheese = input() 

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