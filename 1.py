from tkinter import *
root =Tk()
root.title("number pad")
root.geometry("400x300")
nums =[[0,9,8],[7,6,5],[4,3,2],['*',1,'#']]
for i in range (4):
    root.columnconfigure(i,weight=1,minsize=75)
    root.rowconfigure(i,weight=1,minsize=50)
for i in range (4):
    for j in range (3):
        farm=Frame(master=root,bg="purple",borderwidth=1,relief=RAISED)
        farm.grid(row=i,column=j,sticky='nsew')
        lable=Label(master=farm,text=nums[i][j],bg='#0defff',font=('Arial',18))
        lable.pack(expand=True,fill='both',padx=5,pady=5)
root.mainloop()