from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x400')

fram = Frame(master=root, bg='purple', height=200, width=360)


lb1 = Label(fram, text="FULL NAME", bg="grey", fg='black', width=16)
lb2 = Label(fram, text="Email ID", bg="grey", fg='black', width=16)
lb3 = Label(fram, text="Password", bg="grey", fg='black', width=16)


nentry = Entry(fram)  
eentry = Entry(fram)   
pentry = Entry(fram, show='*') 

def display():
    name = nentry.get()
    email = eentry.get()
    password = pentry.get() 
    
    greet = 'Hey name!'+name
    message = 'Congratulations for your new account\n'
    
    
    
    textbox.delete(1.0, END)
    
    textbox.insert(END, greet)
    textbox.insert(END, message)
    

textbox = Text(root, bg='#BEBEBE', fg='black', height=8, width=50)  


btn = Button(root, text='Create account', command=display, bg='red')


fram.place(x=20, y=0)
lb1.place(x=20, y=20)
nentry.place(x=150, y=20)
lb2.place(x=20, y=80)
eentry.place(x=150, y=80)
lb3.place(x=20, y=140)
pentry.place(x=150, y=140)
btn.place(x=120, y=210)
textbox.place(x=20, y=250)  

root.mainloop()