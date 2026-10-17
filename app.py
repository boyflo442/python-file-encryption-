#********************* Import Required Modules ************************************************************
from tkinter import *     
from tkinter import Tk  
import os                  
import pyAesCrypt
import time
import signup
#***********************************************************************************************************
start = time.time()
tk=Tk()                                 
tk.config(bg="white")                    
tk.geometry("1350x600")                  
tk.title("Cryptography Using AES")    
mylab=Label(tk,text="<----:::::Developed by HaweyTech::::---->",bg="cyan") 
mylab1=Label(tk,text="Please provide Complete path || Path of Folder and path of single file both are allowed",bg="cyan",fg="blue")  
mylab.grid(row=0,column=0)    
mylab1.grid(row=0,column=5)   
img=PhotoImage(file="img1.png")
Label(tk,image=img,border=0,bg="white").place(x=300,y=180)
def logout():
    tk.destroy()
    import signup


def login():
    tk.destroy()
    import app
    

i1=IntVar()          #Declare Intiger variable as i1,here we use for RadioButton
path=StringVar()     #Declare String variable as path,here we use for set Path
pas=StringVar()      #Declare String variable as pas,here we use for set Password

def subm():          #Define Method that called by Button
    gi1=i1.get()     #fetch value of i1
    if gi1==1:       #Check value of fetched variable with 1,1 is for Encryption purpose Selection
        lbl1=Label(tk,text="Provide path for encryption",width=30,fg="purple")    #Set label for entryBox for path
        lbl1.grid(row=3,column=0)                            #set position of Label
        
        epe=Entry(tk,textvariable=path,width=30,border=4)                      #Set Entry Box for get Path from user
        epe.grid(row=3,column=1)                             #set position of EntryBox
        
        lbl1=Label(tk,text="Provide password for encryption",width=25,fg="purple")  #Set label for entryBox, for password
        lbl1.grid(row=3,column=3)                              #set position of Label
        
        epe=Entry(tk,textvariable=pas,width=15,border=4,show="*")                         #Set Entry Box, for get Password from user
        epe.grid(row=3,column=4)                               #set position of EntryBox
        
        btsub1=Button(tk,text="EncryptMe: -->",command=enc,fg="white",bg="magenta",font=('Helvetica', 15, 'bold'))     #Set Button, if that pressed then call required function
        btsub1.grid(row=3,column=5)                             #set position of Button

    else:                                                       #if case is False, then else is call 

        lbl1=Label(tk,text="Provide path for decryption",width=30,fg="purple")       #Set label for entryBox for path
        lbl1.grid(row=4,column=0)                               #set position of Label
        
        epe=Entry(tk,textvariable=path,width=30,border=4)                         #Set Entry Box for get Path from user    
        epe.grid(row=4,column=1)                                #set position of EntryBox
        
        lbl1=Label(tk,text="Provide password for decrypting the file",width=30,fg="purple")    #Set label for entryBox, for password
        lbl1.grid(row=4,column=3)                                           #set position of Label
        
        epe=Entry(tk,textvariable=pas,width=15,border=4,show="*")                                       #Set Entry Box, for get Password from user
        epe.grid(row=4,column=4)                                             #set position of EntryBox
    
        btsub2=Button(tk,text="DecryptMe: -->",command=dec,fg="white",bg="magenta",font=('Helvetica', 15, 'bold'))                  #Set Button, if that pressed then call required function
        btsub2.grid(row=4,column=5)                                          #set position of Button

def enc():                                              #Enryption function call by button 
    chsz=64*1024                                        #set chunk size
    pat=path.get()                                      #get path ,in Entry box by .get()
    pat=pat.replace("\\","/")                           #make path window readable
    ps=pas.get()                                        #get pass ,in Entry box by .get()
    if os.path.exists(pat):                             #check given path is exist or not
            if os.path.isfile(pat):                     #check if file 
                lnts=len(pat)                           #count lenth of path
                if (pat[lnts-4]=="." and pat[lnts-3]=="a" and pat[lnts-2]=="e" and pat[lnts-1]=="s"):     #check file encrypted or not 
                    lblaes=Label(tk,text="This File are Already Encrypted",bg="green")                    #set lable as file is already encrypt ,dont perform encryption
                    lblaes.grid(row=7,column=4)         #set position to lable
                    
                else:                                   #if check file already encrypted or not is false then else execute for encrypt th file
                    pat1=os.path.dirname(pat)           #get parent folder name
                    pat2=str(pat.split(pat1)[1]).replace("/","").replace("\\","")     #get file name
                    pat3=pat2+".aes"                                                  #give encryption stander name ,tail at origianl name
                    os.chdir(pat1)                                 #change directory from main program execution path to given operational file path
                    pyAesCrypt.encryptFile(pat2,pat3,ps,chsz)      #Encrypt the file and save as ".aes" format                 
                    os.remove(pat2)                                #remove originle readable file
                
            elif os.path.isdir(pat):                  #when path contain end node is folder 
                os.chdir(pat)                         #change directory from main program execution path to given operational file path
                cvt=os.listdir()                      #list file contain in the folder
                for k in range(0,len(cvt)):           #for use for operation in each of one by one
                    pat=cvt[k]                        #capy name file in other variable
                    lnts=len(pat)                     #count lenth of path,number of character found
                    if (pat[lnts-4]=="." and pat[lnts-3]=="a" and pat[lnts-2]=="e" and pat[lnts-1]=="s"):      #check if is already encrypted or not
                        end = time.time()
                        print(end - start)
                        lblnaes=Label(tk,text=end-start,bg="Cyan",width=35)  #set label for for Alert user,"file,files are non_Encrypt format"
                        lblnaes=Label(tk,text=('Total execution time for Encryption',end-start),bg="Cyan")           
                        lblnaes.grid(row=7,column=4)    #set position of label
                    else:
                        patt=str(cvt[k])                     #conert string format and save in other variable
                        patte=patt+".aes"                   #give encryption stander name ,tail at origianl name
                        pyAesCrypt.encryptFile(patt,patte,ps,chsz)  #convert to encrypt file,and save as .aes format
                        os.remove(patt)                        #remove original/readable file
                
            

def dec():                         #decrypt fuction call
    chsz=64*1024                   #set chunk size 
    pat=path.get()                 #get path ,that Enterd in Entry box and fetch by .get() method
    pat=pat.replace("\\","/")      #make a path windows capable ,cause some time "\" give error 
    ps=pas.get()                   #get password ,that Enterd in Entry box and fetch by .get() method
    if os.path.exists(pat):        #check user entered path Present or not if present then if Execute
        if os.path.isfile(pat):    #check path folder or end file,if file then if Execute
            lnts=len(pat)          #get lenth of path string,number of character
            if (pat[lnts-4]=="." and pat[lnts-3]=="a" and pat[lnts-2]=="e" and pat[lnts-1]=="s"):  #check for file is encrypted format
                pat1=os.path.dirname(pat)                 #get parent directory of file
                pat2=str(pat.split(pat1)[1]).replace("/","").replace("\\","")   #get name of file
                pat3=pat2.split(".aes")[0]                        #for rename the file ,at reable/openable format
                os.chdir(pat1)                                    #change directory from main program execution path to given operational file path
                pyAesCrypt.decryptFile(pat2,pat3,ps,chsz)         #decrypt the file and create readable/openable format
                os.remove(pat2)                                   #removve encrypted file

            else:                                                 # if If condition false means file alredy reable 
                lblnaes=Label(tk,text="This Files are Already in  Decrypted format",bg="green")  #Alert user to not need of decryption 
                lblnaes.grid(row=8,column=4)                                                     #set position to Label
                
        elif os.path.isdir(pat):                           # if end node of path is folder ,and that folder contain operationals files
            os.chdir(pat)                                  #change path of program from main program path to operational file_folder
            cvt=os.listdir()                               #list the directory in that perticular folder 
            for k in range(0,len(cvt)):                    #for loop use for operation each file in that folder 
                patt=str(cvt[k])                           #convert file name to string format 
                pat=cvt[k]                                 #store value on other  variable
                patte=patt.split(".aes")[0]                #get original file name by remove aes(Encryption foramt name)
                lnts=len(pat)                              #copy lenth of path
                if (pat[lnts-4]=="." and pat[lnts-3]=="a" and pat[lnts-2]=="e" and pat[lnts-1]=="s"): #check file is encrypted or not
                    pyAesCrypt.decryptFile(patt,patte,ps,chsz)  #decryption method ,create reable format file
                    os.remove(patt)                             #Remove encrypted file
                else:                                          #if If Condition goes false then else will execute
                    end = time.time()
                    print(end - start)
                    lblnaes=Label(tk,text=end-start,bg="Cyan",width=35)  #set label for for Alert user,"file,files are non_Encrypt format"
                    lblnaes=Label(tk,text=('Total execution time for Decryption',end-start),bg="Cyan")
                    lblnaes.grid(row=8,column=4)             #set position of Label
                    

lr1=Label(tk,text="Encryption")             #set label for RadioButton with value1, for Encryption
lr1.grid(row=1,column=1)                    #set position of Label
rb1=Radiobutton(tk,variable=i1,value=1)     #set RadioButton with value 1
rb1.grid(row=1,column=2)                    #set position of Button 

lr2=Label(tk,text="Decryption")               #set label for RadioButton with value2, for Decryption
lr2.grid(row=1,column=3)                      #set position of Label  
rb2=Radiobutton(tk,variable=i1,value=2)       #set RadioButton with value 2
rb2.grid(row=1,column=4)                      #set position of Button                 

bt1=Button(tk,text="Next: -->",command=subm)  #Define Button ,is press then Control goes to subm function
bt1.grid(row=2,column=3)
Button(tk,width=42,pady=7,text="Log Out",bg="#57a1f8", fg="white",border=0,command=logout,font=("Times",8,"bold")).place(x=900,y=350)
Button(tk,width=42,pady=7,text="Start Over",bg="#57a1f8", fg="white",border=0,command=login,font=("Times",8,"bold")).place(x=900,y=400)
tk.mainloop()                                 

