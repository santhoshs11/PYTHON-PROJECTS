from tkinter import *

window=Tk()
window.title("MILES TO KILOMETER CONVERTER")
window.minsize(width=600,height=600)
window.config(padx=500,pady=250)

def milestokilo():
    
    miles=float(entry.get())
    kilo =round((miles*1.609344),3)
    kilometer.config(text=kilo)
  
    


button =Button(text="convert",width=8,foreground="red",command=milestokilo)
button.grid(column=1,row=2)


entry =Entry(width=10)
entry.grid(column=1,row=0)


miles=Label(text="MILES")
miles.grid(column=2,row=0)

isequal =Label(text="is equal to")
isequal.grid(column=0,row=1)

kilometer=Label(text='_______')
kilometer.grid(column=1,row=1)

kilo =Label(text="KILOMETER")
kilo.grid(column=2,row=1)






window.mainloop()