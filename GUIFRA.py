from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
main = Tk()

main.mainloop

main.title('Login')

main. geometry ( '925x500+300+200')
main. configure (bg="brown")
main.resizable(False,False)


def open_program():
    attendence = 'C:/SEM 6 PROJECT/FRA.py'
    os.system('"%s"' % attendence)
    
def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        screen=Toplevel(main)
        screen.title("STANFORD TECHNOLOGY UNIVERSITY")
        screen.geometry('925x500+300+200')
        screen.iconbitmap('C:/Users/vinay/Downloads/stanford-icon.ico')
        attendence = ('C:/SEM 6 PROJECT/FRA.py')
        os.system('"%s"' % attendence)
        
          
    elif username!='admin':
        messagebox.showerror("Invalid","invalid username and password")

    elif password!='1234':
        messagebox.showerror("Invalid","invalid username and password")

img = PhotoImage(file='C:/Users/vinay/OneDrive/Desktop/GUIFRA/STANFORD TECHNOLOGY UNIVERSITY 13.png')
Label(main,image=img,bg='brown').place(x=-75,y=30)

img2 = PhotoImage(file='C:/Users/vinay/OneDrive/Desktop/GUIFRA/56.png')
Label(main,image=img,bg='brown').place(x=-75,y=-4)


frame=Frame(main,width=350, height=350,bg="BROWN")
frame.place(x=480,y=80)

heading=Label (frame, text='SIGN IN',fg='yellow',bg='brown',font=('Microsoft YaHei UL Light',28, 'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=( 'Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame (frame,width=295,height=2,bg='black').place(x=25,y=107)


def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        code.insert(0,'Username')
code = Entry(frame,width=25,fg='black',border=0,bg="white",font=( 'Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame (frame,width=295,height=2,bg='black').place(x=25,y=177)

Button(frame,width=39,pady=7,text='SIGN IN',bg='#57a1f8',fg='black',border=0,command=signin).place(x=35,y=204)

main.mainloop()



