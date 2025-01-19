from tkinter import *
from tkinter import messagebox
import ast

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(True,True)

def signin():
  username=user.get()
  password=code.get()

  file=open('datasheet.txt','r')
  d=file.read()
  r=ast.literal_eval(d)
  file.close()
  #print(r.keys())
  #print(r.values())

  if username in r.keys() and password==r[username]:
    screen=Toplevel(root)
    screen.title("Sunny's App")
    screen.geometry('925x500+300+200')
    screen.config(bg="Steel blue")
    Label(screen,text="Hello Everyone!\n My Name is sunny",bg='steel blue',font=("Comic Sans MS",50,'bold')).pack(expand=True)
    screen.mainloop()
  else:
    messagebox.showerror('Invalid','Invalid username or password')
#################################!!!!!!!!!!!!!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def signup_command():
  window=Toplevel(root)
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
  
  signin=Button(frame,width=7,text='Sign In',border=0,bg='Steel blue',cursor='hand2',fg='midnight blue',font=("Microsoft yaHei UI Light",11),command=sign)
  signin.place(x=200,y=340)
  
  
  
  
  
  
  
  window.mainloop()
    
  
  
  
#######################################################@@@@@@@@@@@@@@@@@@@@@@@@@@@
img=PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)
heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=130,y=5)

def on_enter(e):
  user.delete(0,'end')

def on_leave(e):
  name=user.get()
  if name=='':
    user.insert(0,'Username')

user=Entry(frame,width=30,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
user.place(x=50,y=80)
user.insert(0,"Username")
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

def on_enter(e):
  code.delete(0,'end')

def on_leave(e):
  name=code.get()
  if name=='':
    code.insert(0,'Password')
code=Entry(frame,width=30,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
code.place(x=50,y=150)
code.insert(0,"Password")
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)





root.mainloop() 