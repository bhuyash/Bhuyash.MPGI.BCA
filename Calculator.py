from tkinter import *
root=Tk()
root.title("Simple Calculator")
root.configure(bg="#36454F")
e=Entry(root,width=17,borderwidth=5,font=("Comic Sans MS",20),bg="#301934",fg="white")
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10,ipady=10)
Label(root,text="Calculator",bg="grey",fg="white",font=("Comic Sans Ms",17)).grid(row=0,column=4)

def button_click(number):
  current=e.get()
  e.delete(0,END)
  e.insert(0, str(current) + str(number))
  return


def clear():
  e.delete(0,END)
  return

def substract():
  first=e.get()
  global math
  global f_num
  math="Substraction"
  f_num=float(first)
  e.delete(0,END)

def mult():
  first=e.get()
  global math
  global f_num
  math="Multiplication"
  f_num=float(first)
  e.delete(0,END)

def div():
  first=e.get()
  global math
  global f_num
  math="Divison"
  f_num=float(first)
  e.delete(0,END)


def add():
  first=e.get()
  global math
  global f_num
  math="Addition"
  f_num=float(first)
  e.delete(0,END)

def power():
  first=e.get()
  global math
  global f_num
  math="Power"
  f_num=int(first)
  e.delete(0,END)

def percentage():
  first=e.get()
  global math
  global f_num
  math="Percentage"
  f_num=float(first)
  e.delete(0,END)

def equal():
  second_number=e.get()
  e.delete(0,END)
  if math=="Addition": 
    e.insert(0,f_num+float(second_number))
  elif math=="Substraction":
    e.insert(0,f_num-float(second_number))
  elif math=="Multiplication":
    e.insert(0,f_num*float(second_number))
  elif math=="Divison":
    e.insert(0,f_num/float(second_number))
  elif math=="Power":
    e.insert(0,f_num**int(second_number))
  elif math=="Percentage":
    e.insert(0,f_num*(float(second_number)/100))
  else:
    pass



button1=Button(root,text="1",padx=40,pady=15,font=("Comic Sans MS",10),bg="#023020",fg="white",command=lambda:button_click(1))
button2=Button(root,text="2",padx=40,pady=15,font=("Comic Sans MS",10),bg="#023020",fg="white",command=lambda:button_click(2))
button3=Button(root,text="3",padx=40,pady=15,font=("Comic Sans MS",10),bg="#023020",fg="white",command=lambda:button_click(3))
button4=Button(root,text="4",padx=40,pady=15,font=("Comic Sans MS",10),bg="#023020",fg="white",command=lambda:button_click(4))
button5=Button(root,text="5",padx=40,pady=15,font=("Comic Sans MS",10),bg="#023020",fg="white",command=lambda:button_click(5))
button6=Button(root,text="6",padx=40,pady=15,font=("Comic Sans MS",10),bg="#023020",fg="white",command=lambda:button_click(6))
button7=Button(root,text="7",padx=40,pady=15,font=("Comic Sans MS",10),bg="#023020",fg="white",command=lambda:button_click(7))
button8=Button(root,text="8",padx=40,pady=15,font=("Comic Sans MS",10),bg="#023020",fg="white",command=lambda:button_click(8))
button9=Button(root,text="9",padx=40,pady=15,font=("Comic Sans MS",10),bg="#023020",fg="white",command=lambda:button_click(9))
button0=Button(root,text="0",padx=40,pady=15,font=("Comic Sans MS",10),bg="#023020",fg="white",command=lambda:button_click(0))

buttonclr=Button(root,text="CLR",padx=33,pady=15,font=("Comic Sans MS",10),bg="#023020",fg="white",command=clear)
buttonequal=Button(root,text="=",padx=40,pady=15,font=("Comic Sans MS",10),bg="#023020",fg="white",command=equal)
buttonadd=Button(root,text="+",padx=40,pady=7,font=("Comic Sans MS",15),bg="#023020",fg="white",command=add)
buttonsub=Button(root,text="-",padx=41,pady=7,font=("Comic Sans MS",15),bg="#023020",fg="white" ,command=substract)
buttonmult=Button(root,text="X",padx=43,pady=15,font=("Comic Sans MS",10) ,bg="#023020",fg="white" ,command=mult)
buttondiv=Button(root,text="/",padx=44,pady=15,font=("Comic Sans MS",10),bg="#023020",fg="white",command=div)

buttonpow=Button(root,text="^",padx=38,pady=4,font=("Comic Sans MS",17),bg="#023020",fg="white",command=power)
buttonper=Button(root,text="%",padx=44,pady=15,font=("Comic Sans MS",10),bg="#023020",fg="white",command=percentage)


button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=1)
buttonclr.grid(row=4,column=0)
buttonequal.grid(row=4,column=2)
buttonadd.grid(row=2,column=4)
buttonsub.grid(row=1,column=4)
buttonmult.grid(row=3,column=4)
buttondiv.grid(row=4,column=4)
buttonpow.grid(row=1,column=5)
buttonper.grid(row=2,column=5)



root.mainloop()