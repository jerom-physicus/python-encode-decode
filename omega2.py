from tkinter import *
from tkinter import ttk
import base64

window = Tk()
window.geometry("500x400")
window.title("OMEGA CRYPTOGRAPHY")
window.config(background="#999999")
#icon = PhotoImage(file = 'omega2.png')
#window.iconphoto(True,icon)


 ############################################################

## encyption program
def newwin():

    msg = entry.get()
    cpw = bytes(msg, "utf-8")
    code = base64.b64encode(cpw)
    codex = base64.b64encode(code)
    codex1 = base64.b64encode(codex)


    entry2 = Entry(window , font=10 , bg = "#99ff99", bd =10)
    entry2.place(x=70,y=300,height=50,width=375,)
    entry2.insert(0,codex1)
    entry2.place(x=70,y=300,height=50,width=375)





##############################################################

## decryption programm

def newwin2():

    msg3 = entry.get()
    cpw3 = bytes(msg3, "utf-8")
    code2 = base64.b64decode(cpw3)
    codey2 = base64.b64decode(code2)
    codey3 = base64.b64decode(codey2)

    entry3 = Entry(window, font=10,bg="#ff8080",bd= 10)
    entry3.place(x=70,y=300,height=50,width=375)
    entry3.insert(0,codey3)
    entry3.place(x=70,y=300,height=50,width=375)

################################################################

def reset():
    entry.delete(0, END)


text = Label(window,text='Enter a message to encrypt or decrypt',font=(33))
text.pack()

entry= Entry(window,font= (20),bg = "powder blue",bd = 10)
entry.place(x=70,y=50,height=50,width=375,)

green_button = Button(window,text='ENCRYPT',bg='#52d904',font=(100),command=newwin,bd = 16)
green_button.place(x=80,y=120,width = 140)

red_button = Button(window,text='DECRYPT',bg='#fc0505',font=(100),command=newwin2,bd = 16)
red_button.place(x=300,y=120, width = 140)

blue_button = Button(window, text='RESET', bg='#352eff', font=(100),command=reset,bd = 16)
blue_button.place(x=150,y=210,width=200)

lable = Label(window,text="", )
lable.pack ()


window.mainloop()