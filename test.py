import tkinter as tk 
from tkinter import messagebox as ms 
import pyttsx3
def appel():
    engine = pyttsx3.init()
    val1=text2.get()
    if "bonjour" in val1.lower() :
       text1.insert(1.0,"salut! comment puis je vous aider\n")
       engine.setProperty('rate', 110)
       engine.say("hello! how can i help you.")
    elif "nom" in val1.lower() :
       text1.insert(1.0,"je suis une pseudo evolution de john.3\n")
       engine.setProperty('rate', 110)
       engine.say("i am a evolution of john.3")
    elif "john" in val1.lower() :
       text1.insert(1.0,"maitre vous etes mon createur bienvenu dans votre monde\n")
       engine.setProperty('rate', 110)
       engine.say("master your are my creator welcome in your world")   
    engine.runAndWait()
root = tk.Tk()
root.title("test")
root.geometry("300x200")
label=tk.Label(root,text="John4.0")
label.pack(pady=50)
text1=tk.Text(root,height=15,width=120)
text1.pack()
text2=tk.Entry(root,width=120)
text2.pack()
boutton1=tk.Button(root,text="Envoyer",command=appel)
boutton1.pack()
root.mainloop()
