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


turn ="X"
def play(event):
    global turn
    button=event.widget

    if turn=="X":
        button["text"]="X"
        turn="O"
    else:
        button["text"]="O"
        turn="X"

#first rowwidth=4,height=3, font=("Arial",40)
button1=Button(frame2, text=" ",width=4,height=2, font=("Arial",35), relief=RAISED, bg="orange", borderwidth=5)
button1.grid(row=0,column=0)
button1.bind("<Button-1>", play)

button2=Button(frame2,text=" ",width=4,height=2, font=("Arial",35),relief=RAISED, bg="orange", borderwidth=5)
button2.grid(row=0,column=1)
button2.bind("<Button-1>", play)


button3=Button(frame2, text=" ", width=4,height=2, font=("Arial",35),relief=RAISED, bg="orange", borderwidth=5)
button3.grid(row=0, column=2)
button3.bind("<Button-1>", play)

#second row
button1=Button(frame2, text=" ",width=4,height=2, font=("Arial",35),relief=RAISED, bg="orange", borderwidth=5)
button1.grid(row=1,column=0)
button1.bind("<Button-1>", play)

button2=Button(frame2,text=" ", width=4,height=2, font=("Arial",35),relief=RAISED, bg="orange", borderwidth=5)
button2.grid(row=1,column=1)
button2.bind("<Button-1>", play)

button3=Button(frame2, text=" ", width=4,height=2, font=("Arial",35),relief=RAISED, bg="orange", borderwidth=5)
button3.grid(row=1, column=2)
button3.bind("<Button-1>", play)

#third row
button1=Button(frame2, text=" ",width=4,height=2, font=("Arial",35),relief=RAISED, bg="orange", borderwidth=5)
button1.grid(row=2,column=0)
button1.bind("<Button-1>", play)

button2=Button(frame2,text=" ", width=4,height=2, font=("Arial",35),relief=RAISED, bg="orange", borderwidth=5)
button2.grid(row=2,column=1)
button2.bind("<Button-1>", play)

button3=Button(frame2, text=" ", width=4,height=2, font=("Arial",35),relief=RAISED, bg="orange", borderwidth=5)
button3.grid(row=2, column=2)
button3.bind("<Button-1>", play)


root.mainloop()


