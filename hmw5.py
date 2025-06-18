from tkinter import Tk, Label, Button, Entry
from tkinter.messagebox import showinfo


root = Tk()




label2 = Label(root,text='K')
label2.grid(row=4,column=2)

def press():
    """ lol """

   
   

pressEnt = Label(root, text='N')
pressEnt.grid(row=3,column=2)

player_n = Entry(root)
player_n.grid(row=3,column=5)
player_k = Entry()
player_k.grid(row=4,column=5)


button = Button(root, text='Start',command=press)
button.grid(row=5,column=3)
    
    



root.mainloop()









