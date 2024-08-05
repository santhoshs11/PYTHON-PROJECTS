from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps =0
timer =None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1

    if reps %8==0:
        count_down(LONG_BREAK_MIN*60)
        title.config(text="LONG BREAK",fg=PINK)
    elif reps %2==0:
        count_down(SHORT_BREAK_MIN*60)
        title.config(text="SHORT BREAK",fg=YELLOW)
    else:
        count_down(WORK_MIN*60)
        title.config(text="WORK",fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min =count//60
    sec=count%60
    canvas.itemconfig(timer_text,text=f"{min:02d}:{sec:02d}")
    if count > 0:
       global timer
       timer= window.after(1000,count_down,count-1)
    else:
        
        timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)    
# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("pomodoro")
window.config(padx=100,pady=100,bg="#7D8F69")


TexT="✔"
canvas =Canvas(width=200,height=224,background="#7D8F69",highlightthickness=0)
tomato =PhotoImage(file="/home/santhosh/Documents/python projects/advanced_projects/pomodoro-start/tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

button_s= Button(text="start",bg='#E6E5A3',fg='#557153',highlightthickness=0,command=start_timer)
button_s.grid(column=0,row=2)

button_r= Button(text="Reset",bg='#E6E5A3',fg='#557153',highlightthickness=0,command=reset_timer)
button_r.grid(column=2,row=2)

title =Label(text="TIMER",bg='#7D8F69',fg='#E6E5A3',font=('georgia',25,'bold'))
title.grid(column=1,row=0)

checkmark=Label(text=TexT,fg='#CFB997',bg='#7D8F69',highlightthickness=0,font=("arial",25,'bold'))
checkmark.grid(column=1,row=3)



window.mainloop()





