bill=float(input("total Bill : "))
tip_percentage=int(input("percentage : "))
split_bill=int(input("how many people should pay : "))
total_bil=(tip_percentage/bill*100)+bill
total_sbil=total_bil/split_bill
final_amount= round(total_sbil,2)
print(f"total bill per person {final_amount}")
