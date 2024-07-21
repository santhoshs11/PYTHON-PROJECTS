def bmi_calculator_2():
  height = float(input("height : "))
  weight = int(input("weight : "))
  bmi = weight / height**2
  bmi1 = round(bmi,2)
  if bmi < 18.5:
    print(f"Your BMI is {bmi1}, your are under weight")
  elif bmi1>=18.5 and bmi1<25:
    print(f"Your BMI is {bmi1}, you have a normal weight.")
  elif bmi1>=25 and bmi1<30:
    print(f"Your BMI is {bmi1}, you are slightly overweight.")
  elif bmi1 >=30 and bmi1<35 :
    print(f"Your BMI is {bmi1}, you are obese.")
  else:
    print(f"Your BMI is {bmi1}, you are clinically obese.")

bmi_calculator_2()