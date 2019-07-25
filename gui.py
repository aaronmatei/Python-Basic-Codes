from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")
def btnEqualsInput():
    global operator
    result=str(eval(operator))
    text_Input.set(result)
    operator = ""



my_app = Tk()
my_app.title("My Calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry (my_app, font=('arial', 20, 'bold'),textvariable=text_Input, bd=30, insertwidth=4,
                    bg="powder blue", justify='right').grid(columnspan=4)
bt7= Button(my_app,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="7",command=lambda:btnClick(7),bg="powder blue").grid(row=1, column=0)
bt8= Button(my_app,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="8",command=lambda:btnClick(8),bg="powder blue").grid(row=1, column=1)
bt9= Button(my_app,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="9",command=lambda:btnClick(9),bg="powder blue").grid(row=1, column=2)
Addition= Button(my_app,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="+",command=lambda:btnClick("+")).grid(row=1, column=3)
bt4= Button(my_app,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="4",command=lambda:btnClick(4),bg="powder blue").grid(row=2, column=0)
bt5= Button(my_app,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="5",command=lambda:btnClick(5),bg="powder blue").grid(row=2, column=1)
bt6= Button(my_app,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="6",command=lambda:btnClick(6),bg="powder blue").grid(row=2, column=2)
Minus= Button(my_app,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="-",command=lambda:btnClick("-")).grid(row=2, column=3)
bt1= Button(my_app,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="1",command=lambda:btnClick(1),bg="powder blue").grid(row=3, column=0)
bt2= Button(my_app,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="2",command=lambda:btnClick(2),bg="powder blue").grid(row=3, column=1)
bt3= Button(my_app,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="3",command=lambda:btnClick(3),bg="powder blue").grid(row=3, column=2)
Multiplication= Button(my_app,padx=16,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="*",command=lambda:btnClick("*")).grid(row=3, column=3)
Zero= Button(my_app,padx=16,pady=15,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="0", command=lambda:btnClick(0),bg="powder blue").grid(row=4, column=0)
Clear= Button(my_app,padx=16,pady=15,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="C",command=btnClearDisplay).grid(row=4, column=1)
Equals= Button(my_app,padx=16,pady=15, bd=8, fg="black",font=('arial', 20, 'bold'),
            text="=", command=btnEqualsInput).grid(row=4, column=2)
Division= Button(my_app,padx=16,pady=15,bd=8, fg="black",font=('arial', 20, 'bold'),
            text="/",command=lambda:btnClick("/")).grid(row=4, column=3)





# name = Label(my_app, text="But1", bg="black", fg="white", font="Consolas", borderwidth=2, relief="groove", padx="2",pady="2")
# name.grid(row=0, column=0, sticky=N+S+E+W)
# name = Label(my_app, text="But2", bg="black", fg="white", font="Consolas", borderwidth=2, relief="groove", padx="2",pady="2")
# name.grid(row=0, column=1, sticky=N+S+E+W)
# name = Label(my_app, text="But3", bg="black", fg="white", font="Consolas", borderwidth=2, relief="groove", padx="2",pady="2")
# name.grid(row=0, column=2, sticky=N+S+E+W)
# name = Label(my_app, text="But4", bg="black", fg="white", font="Consolas", borderwidth=2, relief="groove", padx="2",pady="2")
# name.grid(row=0, column=3, sticky=N+S+E+W)
# name = Label(my_app, text="But5", bg="black", fg="white", font="Consolas", borderwidth=2, relief="groove", padx="2",pady="2")
# name.grid(row=0, column=4, sticky=N+S+E+W)

my_app.mainloop()
print("Program executed successfully")