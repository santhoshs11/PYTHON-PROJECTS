print("The Love Calculator is calculating your score...")
name1 = input() 
name2 = input() 

combined_name=(name1+name2)
lower = combined_name.lower()
t= lower.count("t")
r= lower.count("r")
u= lower.count("u")
e= lower.count("e")
final1=t+r+u+e
l= lower.count("l")
o= lower.count("o")
v= lower.count("v")
e= lower.count("e")
final=l+o+v+e
score=int(str(final1)+str(final))
if score <10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
  print(f"Your score is {score}, you are alright together.")

else:
   print(f"Your score is {score}.")
