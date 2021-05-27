from tkinter import *
root = Tk()
root.title("Calculator")

#entry section
e = Entry(root,width = 40, borderwidth = 5)
e.grid(row = 0, column = 0 ,columnspan =3, padx =10,pady = 10)

'''BUTTON FUNCTION
    this is where i m going to give all the button funtion
    so that when clicked it is displayed and is also calculated
'''
def click(n):
    i = e.get()
    e.delete(0,END)
    e.insert(0, str(i) +str(n))

def add():
    global f_num
    f_num = int(e.get())
    e.delete(0,END)
    global given
    given = "+"

def sub():
    global f_num
    f_num = int(e.get())
    e.delete(0,END)
    global given
    given = "-"

def multi():
    global f_num
    f_num = int(e.get())
    e.delete(0, END)
    global given
    given = "x"

def divide():
    global f_num
    f_num = int(e.get())
    e.delete(0, END)
    global given
    given = "/"

def mod():
    global f_num
    f_num = int(e.get())
    e.delete(0, END)
    global given
    given = "%"

def clear():
    e.delete(0,END)
def equal():
    global s_num
    s_num = int(e.get())
    e.delete(0,END)
    e.insert(0,value())

def value():
    if given == "+":
        soln = f_num + s_num
        return soln

    if given == "-":
        soln = f_num - s_num
        return soln

    if given == "x":
        soln = f_num * s_num
        return soln

    if given == "/":
        soln = f_num/s_num
        return soln

    if given == "%":
        soln = f_num%s_num
        return soln

#definiting number buttons
btn_1 = Button(root,text = "1", padx = 40, pady =20,command = lambda :click(1))
btn_2 = Button(root,text = "2", padx = 40, pady =20,command = lambda :click(2))
btn_3 = Button(root,text = "3", padx = 40, pady =20,command = lambda :click(3))
btn_4 = Button(root,text = "4", padx = 40, pady =20,command = lambda :click(4))
btn_5 = Button(root,text = "5", padx = 40, pady =20,command = lambda :click(5))
btn_6 = Button(root,text = "6", padx = 40, pady =20,command = lambda :click(6))
btn_7 = Button(root,text = "7", padx = 40, pady =20,command = lambda :click(7))
btn_8 = Button(root,text = "8", padx = 40, pady =20,command = lambda :click(8))
btn_9 = Button(root,text = "9", padx = 40, pady =20,command = lambda :click(9))
btn_0 = Button(root,text = "0", padx = 40, pady =20,command = lambda :click(0))

#defining calculation bottons

btn_mod = Button(root,text="%",padx = 40, pady = 20,command= mod)
btn_add = Button(root,text="+", padx=39,pady = 20,command = add)
btn_sub = Button(root,text = "-", padx = 40,pady=20,command = sub)
btn_multi = Button(root,text ="x",padx = 40,pady = 20,command = multi)
btn_divide = Button(root,text ="/",padx= 40,pady = 20,command = divide)
btn_equal = Button(root,text="=",padx=40,pady = 20,command = equal)
btn_clear = Button(root,text="Clear",padx=80,pady = 20,command = clear)

#placing number buttons
btn_1.grid(row=1,column = 0)
btn_2.grid(row=1,column = 1)
btn_3.grid(row=1,column = 2)

btn_4.grid(row=2,column = 0)
btn_5.grid(row=2,column = 1)
btn_6.grid(row=2,column = 2)

btn_7.grid(row=3,column = 0)
btn_8.grid(row=3,column = 1)
btn_9.grid(row=3,column = 2)

btn_0.grid(row=4,column = 1)

#placing calculation buttons
btn_add.grid(row=4,column=0)
btn_sub.grid(row=4,column=2)
btn_divide.grid(row=5,column=0)
btn_equal.grid(row=5,column=2)
btn_multi.grid(row=6,column=0)
btn_clear.grid(row=6,column=1,columnspan=2)
btn_mod.grid(row = 5, column = 1)

root.mainloop()
