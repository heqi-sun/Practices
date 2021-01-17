# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:14:54 2021

@author: Heqi Sun
"""

from tkinter import *
from random import *

num = "0123456789"
alpha_num = "abcdefghijklmnopqrstuvwxyz0123456789"
spec_alpha_num = "!@#$%^&*()+~<>?:`-_=|\}]{[;abcdefghijklmnopqrstuvwxyz0123456789"



def Create_Pass():
    
    pswd_type = typeChoice.get()
    
    if pswd_type == "":
        resultBox.delete(0.0,END)
        resultBox.insert(END, "\n Please select the type of password you prefer.")

    length = int(pass_len.get())
    rand_pass = []
    for i in range(length):
        rand_pass.append(choice(pswd_type))
    
    
    result = "".join(rand_pass)
    
    final_result = "\n *** Your password is :" + result + " ***\n"
    
    resultBox.delete(0.0,END)
    resultBox.insert(END, final_result)
    
    
    
    

# Create a user interface.
window = Tk()
window.geometry("800x500")
window.title("Random Password Generator")

progName = Label(window,font=("Georgia",15,"bold"),
                 text="Password Generator",
                 fg='blue')
progName.grid(row=1,column=3,padx=200,pady=10)

chooseType = Label(window,font=("Georgia",11,"bold"),
                   text="Choose a password type among the 3 options")
chooseType.place(relx=.1,rely=.15)

typeChoice = StringVar()
numChoice = Radiobutton(window,font=("corbel",10,'italic'),
                        text="Numeric",
                        variable=typeChoice,
                        value=num)
numChoice.place(relx=.3,rely=.25)
alphaNumChoice = Radiobutton(window,font=("corbel",10,'italic'),
                        text="Alpha Numeric",
                        variable=typeChoice,
                        value=alpha_num)
alphaNumChoice.place(relx=.3,rely=.3)
specAlphaNumChoice = Radiobutton(window,font=("corbel",10,'italic'),
                        text="Special",
                        variable=typeChoice,
                        value=spec_alpha_num)
specAlphaNumChoice.place(relx=.3,rely=.35)

size = Label(window,font=("corbel",10,'bold'),text="Length")
size.place(relx=.6,rely=.25)

pass_len = Spinbox(window,from_=8,to=100)
pass_len.place(relx=.68,rely=.25)
pass_len.config(state="readonly")

genButton = Button(window,font=('corbel',10,'bold'),
                   text="Generate",
                   command=Create_Pass)
genButton.place(relx=.48,rely=.5)

resultBox = Text(window,height=6,width=80,wrap=WORD)
resultBox.place(relx=.1,rely=.6)


window.mainloop()