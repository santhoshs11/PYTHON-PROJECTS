def rps_game():   

    while (True):   
        import random

        list =["rock","scissor","paper"]
        list1 =random.randint(0,2)
        com = list[list1]
        user = input("choose your choice  : ")
        choice = user.lower()
        if choice =="rock" and com == "scissor" :
            print(f"computer choice : {com} \n you win")   
        elif choice =="rock" and com =="paper":
            print(f"computer choice : {com} \n you lose")   
        elif choice =="scissor" and com =="rock":
            print(f"computer choice : {com} \n you lose")   
        elif choice =="scissor" and com == "paper" :
            print(f"computer choice : {com} \n you win")   
        elif choice == "paper" and com == "rock"  :
            print(f"computer choice : {com}\n  \n you win") 
        elif choice == "paper" and com == "scissor":
            print(f"computer choice : {com} \n you lose")   
        elif choice == com:
            print (f"computer choice {com}\n draw")     
        else:
            print("error")

rps_game()            