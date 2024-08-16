from tkinter import *
import requests  

def get_quote():
    res=requests.get('https://api.kanye.rest')
    data=res.json()
    qoute=data['quote']
    canvas.itemconfig(quote_text,text=qoute)



window = Tk()
window.title("kanye")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="advanced_projects/kanye-quotes-start/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Quotes", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="advanced_projects/kanye-quotes-start/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()