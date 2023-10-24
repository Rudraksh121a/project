from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("Text to speech")
root.geometry("900x450+200+200")
root.resizable('False',False)
root.config(bg='#305065')
engine=pyttsx3.init()
def speaknow():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def setvoice():
        if (gender=='female'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if(speed=='Fast'):
            engine.setProperty('rate',250)
            setvoice()

        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()


def download():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def setvoice():
        if (gender=='female'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
    if(text):
        if(speed=='Fast'):
            engine.setProperty('rate',250)
            setvoice()

        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()






#icon
image_icon=PhotoImage(file='speak.png')
root.iconphoto(False,image_icon)


#Top Frame
Top_frame=Frame(root,width=900,height=100,bg='white')
Top_frame.place(x=0,y=0)

#logo
logo=PhotoImage(file='speaker logo.png')
Label(Top_frame,image=logo,bg='white').place(x=10,y=5)

Label(Top_frame,text='Text to speech',bg='white',font='arial 20 bold',fg="black").place(x=100,y=30)

###############

text_area=Text(root,font='Robote 20',bg='white',relief=GROOVE,width=10)
text_area.place(x=10,y=150,width=500,height=200)
Label(root,text='VOICE',bg='#305065',font='arial 20 bold',fg="white").place(x=570,y=160)
Label(root,text='SPEED',bg='#305065',font='arial 20 bold',fg="white").place(x=750,y=160)


gender_combobox=Combobox(root,values=['Female'],font='arial 14',state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Female')


speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font='arial 14',state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')


imageicon=PhotoImage(file='speak.png')
btn=Button(root,text='Speak',compound=LEFT,image=image_icon,width=130,font='arial 14 bold',command=speaknow)
btn.place(x=550,y=280)



imageicon2=PhotoImage(file='download.png')
save=Button(root,text='Speak',compound=LEFT,image=imageicon2,width=130,bg='#39c790',font='arial 14 bold',command=download)
save.place(x=730,y=280)










root.mainloop()