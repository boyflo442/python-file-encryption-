from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import ast
import pymysql
window=Tk()

window.title("Signup")  
window.minsize(950,500)  
window.configure(bg="#fff") 
window.resizable(False,False)

def connect_database():
    username=user.get()
    password=code.get()
    confirm_password=confirm_code.get()
    if password==confirm_password:
        try:
            file=open("datasheet.txt","r+")
            d=file.read()
            r=ast.literal_eval(d)

            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()
            
            file=open ("datasheet.txt","w")
            w=file.write(str(r))
            messagebox.showinfo("Signup","Successfully signed up")
        except:
            file=open("datasheet.txt","w")
            pp=str({"Username":"password"})
            file.write(pp)
            file.close()
    elif username == "" or password =="" or confirm_password == "":
        messagebox.showerror("Invalid input!", "All Entry are Required")    
    else:
        messagebox.showerror("Invalid input!", "Both password should match")
def sign():
    window.destroy()
    import login
 
img=PhotoImage(file="img1.png")
Label(window,image=img,border=0,bg="white").place(x=20,y=30)
frame=Frame(window,width=320,height=390,bg="#fff")
frame.place(x=580,y=70)

heading=Label(frame,text="sign up", fg="#57a1f8",bg="white", font=("Microsoft Yahei UI Light",20,"bold"))
heading.place(x=120,y=5)




#####-----------------------------------------------
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
#####-----------------------------------------------
def on_enter(e):
    confirm_code.delete(0, "end")
def on_leave(e):
    if confirm_code.get()== "":
        confirm_code.insert(0, "Confirm Password")
    

confirm_code=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",9,"bold"),show="*")
confirm_code.place(x=30,y=220)
confirm_code.insert(0, "Confirm Password")
confirm_code.bind("<FocusIn>", on_enter)
confirm_code.bind("<FocusOut>", on_leave)

Frame(frame,width=290,height=2,bg="black").place(x=28, y=247)
######---------------------------------------------------------
Button(frame,width=42,pady=7,text="Sign up",bg="#57a1f8", fg="white",border=0,command=connect_database).place(x=38,y=280)
label=Label(frame,text="I have an account", fg="black", bg="white",font=("Microsoft Yahei UI Light",9))
label.place(x=90,y=340)

signin=Button(frame,width=6,text="Sign in", border=0,bg="white", cursor="hand2",fg="#57a1f8",command=sign)
signin.place(x=200,y=340)

window.mainloop()
