#this is a tic tac toe game 
from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Tic_Tac_Toe")

frame1=Frame(root)
frame1.pack()

titleLabel = Label(frame1, text="Tic Tac Toe", font=("Arial", 40), bg="cyan")
titleLabel.pack()

frame2=Frame(root)
frame2.pack()

def play(event):
    button=event.widget

    button["text"]=X

#first row
button1=Button(frame2, text=" ",width=16,height=8)
button1.grid(row=0,column=0)
button1.bind("<Button-1>", play)

button2=Button(frame2,text=" ", width=16, height=8)
button2.grid(row=0,column=1)

button3=Button(frame2, text=" ", width=16, height=8)
button3.grid(row=0, column=2)

#second row
button1=Button(frame2, text=" ",width=16,height=8)
button1.grid(row=1,column=0)

button2=Button(frame2,text=" ", width=16, height=8)
button2.grid(row=1,column=1)

button3=Button(frame2, text=" ", width=16, height=8)
button3.grid(row=1, column=2)

#third row
button1=Button(frame2, text=" ",width=16,height=8)
button1.grid(row=2,column=0)

button2=Button(frame2,text=" ", width=16, height=8)
button2.grid(row=2,column=1)

button3=Button(frame2, text=" ", width=16, height=8)
button3.grid(row=2, column=2)







root.mainloop()