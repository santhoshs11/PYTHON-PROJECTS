while (True):   
    import random

    list =["rock","scissor","paper"]
    list1 =random.randint(0,len.list)
    com = list[list1]
    user = input("choose your choice  : ")
    choice = user.lower()
    if choice =="rock" and com == "scissor" :
        print(f"compuer choice : {com}\n your choice : {choice} \n you win")   
    elif choice =="rock" and com =="paper":
        print(f"compuer choice : {com}\n your choice : {choice} \n you lose")   
    elif choice =="scissor" and com =="rock":
        print(f"compuer choice : {com}\n your choice : {choice} \n you lose")   
    elif choice =="scissor" and com == "paper" :
        print(f"compuer choice : {com}\n your choice : {choice} \n you win")   
    elif choice == "paper" and com == "rock"  :
        print(f"compuer choice : {com}\n your choice : {choice} \n you win") 
    elif choice == "paper" and com == "scissor":
        print(f"compuer choice : {com}\n your choice : {choice} \n you lose")   
    elif choice == com:
        print ("draw")     
    else:
        print("error")