target = int(input("enter a number : ")) # Enter a number between 0 and 1000

even_sum = 0
for num in range(2,target+1,2):#(2 is refers to start range, target+1 is refers stop range, 2 is refers to 1,3,5,7,9,(or)if 3 is there 1,4,7,10)
  even_sum+=num
  
print(f"The sum of even number in {target} is : {even_sum}")