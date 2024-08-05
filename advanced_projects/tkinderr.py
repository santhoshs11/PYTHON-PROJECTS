from tkinter import *

window = Tk()
window.title("SANTHOSH")
window.minsize(width=600,height=600)

my_label=Label(text="good morning",foreground='blue',font=("Arial",24,"bold"))

my_label.pack()

def click():
    inp =input.get()

    my_label.config(text=inp,background='yellow',foreground='blue',font=('courier',24,'bold'))
     


button=Button(text="oh yeah",background="yellow",foreground='red',width=4,height=1,command=click)
button.pack(side='right')
input =Entry(width=30)
input.pack(expand=True)

text =Text(width=40,height=5,background="yellow",foreground='red',font=('courier'))
text.focus()
text.insert(END,"example of multiphgfhgjmhghghgmjhfjjhgkjghgjhjhjhgle line")
print(text.get("2.0",END))
text.pack(expand=True)



def spin():
    print(spinbox.get())
spinbox=Spinbox(width=20,from_=0,to=10,command=spin)
spinbox.pack()
def ce():
    print(checkvar.get())
checkvar =IntVar()
check=Checkbutton(text='u are a gay',variable=checkvar,command=ce)
checkvar.get()
check.pack()

def radio():
    print(radiovar.get())
radiovar =IntVar()
radio1 = Radiobutton(text="option 1",variable=radiovar,value=1,command=radio)
radio2 = Radiobutton(text="option 2",variable=radiovar,value=2,command=radio)
radio1.pack(expand=True)
radio2.pack(expand=True)



def listboxx(event):
    print(listb.get(listb.curselection()))

listb = Listbox(height=5)
l =["apple",'orange','guava','pineapple','pomagranade']
for item in l:
    listb.insert(l.index(item),item)
listb.bind("<<ListboxSelect>>",listboxx)
listb.pack(expand=True)

window.mainloop()