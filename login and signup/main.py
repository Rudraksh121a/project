from tkinter import *
from tkinter import messagebox
import ast


root=Tk()
root.title("SignIn")
root.geometry("925x500+300+200")
root.resizable('False',False)
root.config(bg='#fff')



#------------------
def signin():
    username=user.get()
    password=code.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()


    if username in r.keys() and password==r[username]:
            screen=Toplevel(root)
            screen.geometry("925x500+300+200")
            screen.config(bg='white')

            Label(screen,text='ERROR 404',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)

            screen.mainloop()

    else:
        messagebox.showerror("Invalid",'invalid username or Password ')



#-----------------

def signup_command():
    window=Toplevel(root)

  
    window.title("SignUp")
    window.geometry("925x500+300+200")
    window.resizable('False',False)
    window.config(bg='#fff')

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



    def sign():
        username=user.get()
        password=code.get()
        confirm_password=conform_code.get()

        if password == confirm_password:
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
            
                messagebox.showinfo('Signup','sucessfully sign up')
                window.destroy()

            except:
                file=open('datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror("Invalid",'Both Password should match')

    im=PhotoImage(file='log.png')
    Label(window,image=im,border=0,bg='white').place(x=50,y=90)


    frame=Frame(window,width=350,height=390,bg='#fff')
    frame.place(x=450,y=50)


    heading=Label(frame,text='Sign Up',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=5)



    ####----------------------------------------------
    def on_enter(e):
        code.delete(0,'end')
    
    def on_leave(e):
        if code.get()=='':
            user.insert(0,'Password')
    code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11,))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)




    
    ####----------------------------------------------
    def on_enter(e):
        user.delete(0,'end')
    
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Username')

    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11,))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)



    ####----------------------------------------------

    def on_enter(e):
        conform_code.delete(0,'end')
    
    def on_leave(e):
        if conform_code.get()=='':
            conform_code.insert(0,'Conform Password')

    conform_code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11,))
    conform_code.place(x=30,y=220)
    conform_code.insert(0,'Conform Password')
    conform_code.bind('<FocusIn>',on_enter)
    conform_code.bind('<FocusOut>',on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    #---------------------------------------------------

    Button(frame,text='Sign up',width=39,pady=7,bg='#57a1f8',fg='white',border=0,command=sign).place(x=35,y=288)
    a=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
    a.place(x=90,y=340)


    signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
    signin.place(x=200,y=340)
    window.mainloop()
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$





img=PhotoImage(file='login.png')
Label(root,image=img,border=0,bg='white').place(x=50,y=90)


frame=Frame(root,width=350,height=390,bg='#fff')
frame.place(x=480,y=70)

heading=Label(frame,text='Sign Up',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)


#------------------------

def on_enter(e):
   user.delete(0,'end')
    
def on_leave(e):
    if user.get()=='':
       user.insert(0,'Username')



user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11,))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#-------------------------------
def on_enter(e):
    code.delete(0,'end')
    
def on_leave(e):
    if code.get()=='':
        user.insert(0,'Password')




code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11,))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#===================================

Button(frame,text='Sign in',width=39,pady=7,bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text='Dont have an account?',fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
label.place(x=80,y=270)


sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=210,y=270)




root.mainloop()

