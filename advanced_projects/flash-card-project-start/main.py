from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
#________________________________________
try:
    data =pd.read_csv('advanced_projects/flash-card-project-start/data/wordtolearn.csv')
    
except FileNotFoundError or data == None:
     o_data =pd.read_csv('advanced_projects/flash-card-project-start/data/french_words.csv')    
     to_learn=o_data.to_dict(orient='records')

else:
     o_data=pd.read_csv('advanced_projects/flash-card-project-start/data/wordtolearn.csv')
     to_learn=o_data.to_dict(orient='records')     
#print(to_learn)
currentcard={}

def flipcard():
    global currentcard
    canvas.itemconfig(cardtitle,text='English',fill='white')
    canvas.itemconfig(cardword,text=currentcard['English'],fill='white')
    canvas.itemconfig(cardbackground,image=imgb)
#______________________________________________
def next_card():
      global currentcard,flip_timer
      window.after_cancel(flip_timer)
      currentcard=random.choice(to_learn)
      canvas.itemconfig(cardbackground,image=imgf)
      canvas.itemconfig(cardtitle,text='French',fill='black')
      canvas.itemconfig(cardword,text=currentcard['French'],fill='black')  
      flip_timer=window.after(3000,func=flipcard)
      
#__________________iscorrect__________________#

def is_crt():
     to_learn.remove(currentcard)
     
     data = pd.DataFrame(to_learn)
     print(len(to_learn))
     data.to_csv('advanced_projects/flash-card-project-start/data/wordtolearn.csv',index=False)
     next_card()


#___________________UI interface______________##

window =Tk()
window.title("FLASH CARD")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flipcard)


canvas= Canvas(width=800,height=526)
imgf =PhotoImage(file="advanced_projects/flash-card-project-start/images/card_front.png")
imgb=PhotoImage(file='advanced_projects/flash-card-project-start/images/card_back.png')
cardbackground=canvas.create_image(400,263,image=imgf)
canvas.config(highlightthickness=0,bg=BACKGROUND_COLOR)

cardtitle=canvas.create_text( 400,150,text='French',font=('ariel',40,'italic'))
cardword=canvas.create_text( 400,263,text='Word',font=('ariel',60,'bold'))


canvas.grid(column=0,row=0,columnspan=2)

uimg=PhotoImage(file='advanced_projects/flash-card-project-start/images/wrong.png')
unknown_button =Button(image=uimg,bg=BACKGROUND_COLOR,highlightthickness=0,command=next_card)
unknown_button.grid(column=0,row=1)

cimg=PhotoImage(file='advanced_projects/flash-card-project-start/images/right.png')
c_button =Button(image=cimg,bg=BACKGROUND_COLOR,highlightthickness=0,command=is_crt)
c_button.grid(column=1,row=1)


next_card()


window.mainloop()