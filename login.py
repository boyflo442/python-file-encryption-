from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import ast
window=Tk()

window.title("Login")  
window.minsize(950,500)  
window.configure(bg="#fff") 
window.resizable(False,False)

img=PhotoImage(file="img3.png")
Label(window,image=img,border=0,bg="white").place(x=20,y=30)
frame=Frame(window,width=320,height=390,bg="#fff")
frame.place(x=540,y=70)

heading=Label(frame,text="Log in", fg="#57a1f8",bg="white", font=("Microsoft Yahei UI Light",20,"bold"))
heading.place(x=120,y=5)
def signin():
    username=user.get()
    password=code.get()

    file=open("datasheet.txt","r")
    d=file.read()
    r=ast.literal_eval(d)
    file.close
    #print(r.keys())
    #print(r.values())
    
    if username in r.keys() and password==r[username]:
        messagebox.showinfo("Login Successful","YOU CAN NOW ACCESS OUR APP FOR ENCRYPTING YOUR FILES")
        window.destroy()
        import app
    else:
        messagebox.showerror("Invalid Login!","Please Signup to use our Application")
def Signup():
    window.destroy()
    import signup
        

#####-----------------------------------------------
def on_enter(e):
    user.delete(0, "end")
def on_leave(e):
    if user.get()== "":
        user.insert(0, "Username")
user=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",9,"bold"))
user.place(x=30,y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(frame,width=290,height=2,bg="black").place(x=25, y=107)


def on_enter(e):
    code.delete(0, "end")
def on_leave(e):
    if code.get()== "":
        code.insert(0, "Password")
code=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",9,"bold"),show="*")
code.place(x=30,y=150)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=290,height=2,bg="black").place(x=28, y=177)

#####--------------------------------------------------------
Button(frame,width=42,pady=7,text="Sign in",bg="#57a1f8", fg="white",border=0,command=signin).place(x=38,y=220)
label=Label(frame,text="Don't have an account?", fg="black", bg="white",font=("Microsoft Yahei UI Light",9))
label.place(x=80,y=270)

signup=Button(frame,width=6,text="Sign up", border=0,bg="white", cursor="hand2",fg="#57a1f8",command=Signup)
signup.place(x=230,y=271)


window.mainloop()
