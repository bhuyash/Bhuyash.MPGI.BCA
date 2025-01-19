from tkinter import *
from tkinter import messagebox
import ast

window=Tk()
window.title("Sign-Up Page")
window.geometry('925x500+300+200')
window.configure(bg="cyan")
window.resizable(False,False)
def signup():
  username=user.get()
  password=code.get()
  conform=c_code.get()

  if password==conform:
    try:
      file=open('datasheet.txt','r+')
      d=file.read()
      r=ast.literal_eval(d)

      dict2={username:password}
      r.update(dict2)
      file.truncate(0)
      file.close()

      file=open('datasheet.txt','w')
      w=file.write(str(r))

      messagebox.showinfo('SignUp','Succesfully Signed Up')
    except:
      file=open('datasheet.txt','w')
      pp=str({'username':'password'})
      file.write(pp)
      file.close()
  else:
    messagebox.showerror('Invalid',"Both Password should Match")
            
def sign():
  window.destroy()


img=PhotoImage(file='page.png')
Label(window,image=img,border=0,bg='cyan').place(x=50,y=90)
frame=Frame(window,width=350,height=390,bg='steel blue')
frame.place(x=480,y=50)

heading=Label(frame,text='Sign up',fg="#57a1f8",bg='black',font=('impact',25))
heading.place(x=115,y=5)
#####----------------------------------------------
def on_enter(e):
  code.delete(0,'end')

def on_leave(e):
  name=code.get()
  if name=='':
    code.insert(0,'Password')

code=Entry(frame,width=25,fg='black',border=0,bg='Steel blue',font=("Comic Sans MS",20))
code.place(x=30,y=150)
code.insert(0,"Password")
code.bind("<FocusIn>",on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=3,bg="black").place(x=25,y=183)
#####----------------------------------------------
def on_enter(e):
  c_code.delete(0,'end')

def on_leave(e):
  name=c_code.get()
  if name=='':
    c_code.insert(0,'Conform Password')

c_code=Entry(frame,width=25,fg='black',border=0,bg='Steel blue',font=("Comic Sans MS",20))
c_code.place(x=30,y=220)
c_code.insert(0,"Conform Password")
c_code.bind("<FocusIn>",on_enter)
c_code.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=3,bg="black").place(x=25,y=253)
#####----------------------------------------------
def on_enter(e):
  user.delete(0,'end')

def on_leave(e):
  name=user.get()
  if name=='':
    user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',border=0,bg='Steel blue',font=("Comic Sans MS",20))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind("<FocusIn>",on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=3,bg="black").place(x=25,y=113)

#--------------------------------------------------
Button(frame,width=24,pady=7,text="Sign Up",bg="Blue",fg="Black",border=0,command=signup,font=("Georgia",15)).place(x=35,y=280)
label=Label(frame,text="I have an account",fg="black",bg="Steel blue",font=("Microsoft yaHei UI Light",10))
label.place(x=90,y=340)

signin=Button(frame,width=7,text='Sign In',border=0,bg='Steel blue',cursor='hand2',fg='midnight blue',font=("Microsoft yaHei UI Light",11,command=sign))
signin.place(x=200,y=340)







window.mainloop()