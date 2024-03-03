height=float(input("hieght in metre :"))
weight=int(input("weight in kg :"))
bmi=weight/height**2
bmi_value=round(bmi,2)
print(f"your BMI is : {bmi_value}")