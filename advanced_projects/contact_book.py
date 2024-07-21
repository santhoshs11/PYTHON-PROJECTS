
print("""________CONTACT BOOK________
      _________________________""")
data={}
def opt():
        global data
        print("""   1.Add contact...
            2.update contact...
            3.delete contact...
            4.all contact...""")
        d=input("enter your option : ") 
        if d == "1":
            name =input("name :")
            phone =input("phone.no :")
            address = input("address :")
            if input('save contact...') =='yes':
                data['name'] = name 
                data['number']= phone
                data['address'] = address     
        elif d == '4':
            print(data)
        elif d =='2':
             pass    
repeat = True                      
while repeat :
    opt()
    wc = input('will continue .....')
    if wc == 'no':
         repeat = False
         
