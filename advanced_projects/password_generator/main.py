from tkinter import *
from tkinter import messagebox
import json
import random
COLOR1="#61481C"
COLOR2="#A47E3B"
COLOR3='#BF9742'
COLOR4='#E6B325'
COLOR5='#'

#_____________password genarate_________________#
def gen_pass():
    
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['!','@','#','$','%','^','&','*','?','/','<','>']

    u_letter =random.randint(6,8)
    u_number =random.randint(2,4)
    u_symbol =random.randint(2,4)

    passwordlist = []
    for p in range(1,u_letter+1):
        passwordlist.append(random.choice(letters))
    
    for p in range(1,u_number+1):
        passwordlist.append(random.choice(numbers))
    
    for p in range(1,u_symbol+1):
        passwordlist.append(random.choice(symbols))

    random.shuffle(passwordlist)   

    password_gen = ""
    for char in passwordlist: 
        password_gen+=char
    p_entry.delete(0,END)
    p_entry.insert(0,password_gen)    
   
#_______________save data_________________#

def save():
    website = w_entry.get()
    email =e_entry.get()
    password =p_entry.get()
    new_data={
        website:{
            "email":email,
            'password':password
        }
    }
    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Oopsss!!!",message="don't empty the column")
    else:
        is_on=messagebox.askyesno(title='data',message=f'Do You Want To Save ?\nWebsite : {website}\nEmail : {email}\nPassword : {password}')
    
        if is_on:
            try:
                with open("data.json", "r") as data_file:
                #Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "a") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
            #Updating old data with new data
                data.update(new_data)

                with open("data.json", "a") as data_file:
                #Saving updated data
                    json.dump(new_data, data_file, indent=4)
            finally:
                w_entry.delete(0, END)
                #e_entry.delete(0,END)
                p_entry.delete(0, END)
                
#____________________password search_____________#
def find_password():
    website = w_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
                
    
#__________________UI SETUP______________________##
window=Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50,pady=50,bg=COLOR1)
canvas =Canvas(width=250,height=250,bg=COLOR1,highlightthickness=0)
lock = PhotoImage(file="/home/santhosh/Documents/python projects/advanced_projects/password_generator/logo.png")
canvas.create_image(125,125,image=lock)
canvas.grid(column=1,row=1)

w_label=Label(text="WEBSITE                  :",bg=COLOR1,fg=COLOR4,height=2)
w_label.grid(column=0,row=3,rowspan=2)

e_label=Label(text="EMAIL / USERNAME :",bg=COLOR1,fg=COLOR4,height=2)
e_label.grid(column=0,row=5,rowspan=2)

p_label=Label(text="PASSWORD              :",bg=COLOR1,fg=COLOR4,height=2)
p_label.grid(column=0,row=7,rowspan=2)

w_entry=Entry(width=25,bg=COLOR4)
w_entry.grid(column=1,row=3,rowspan=2)

e_entry=Entry(width=40,bg=COLOR4)
e_entry.insert(0,'santhosh@gmailcom')
e_entry.grid(column=1,columnspan=2,row=5,rowspan=2)

p_entry=Entry(width=25,bg=COLOR4)
p_entry.grid(column=1,row=7,rowspan=2)

search_button = Button(text="Search", width=4, command=find_password)
search_button.grid(row=3, column=2)

generate =Button(text="genarate",bg=COLOR2,fg=COLOR4,width=5,command=gen_pass)
generate.grid(column=2,row=7)
 
add =Button(text='ADD',bg=COLOR2,fg=COLOR4,width=3,command=save) 
add.grid(column=1,row=9,rowspan=2)

window.mainloop()

