from tkinter import *

window = Tk()
window.title('Calculator')
window.geometry("640x400+100+100")

lb1 = Label(window,text="이름")
lb1.grid(row=0,column=0)
txt = Entry(window)
txt.grid(row=0,column=1)
btn = Button(window,text='OK',width=15)
btn.grid(row=1,column=1)


window.mainloop()
