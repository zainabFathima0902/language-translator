from tkinter import *
from tkinter import ttk
from  googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1

def data():
    s=comb_sor.get()
    d=comb_des.get()
    masg=sor_txt.get(1.0,END)
    textget=change(text=masg,src=s,dest=d)
    des_txt.delete(1.0,END)
    des_txt.insert(END,textget)

container= Tk()
container.title("Translator")
container.geometry("500x700")
container.config(bg="Red")

lab_txt=Label(container,text="Translator",font=("Time New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

frame=Frame(container).pack(side=BOTTOM)

lab_txt=Label(container,text="Source Text",font=("Time New Roman",20,"bold"),bg="red")
lab_txt.place(x=100,y=100,height=20,width=300)

sor_txt=Text(frame,font=("Times New Roman",30,"bold"))
sor_txt.place(x=10,y=130,height=150,width=480)

list_text=list(LANGUAGES.values())
comb_sor= ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("english")

button_change=Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

comb_des= ttk.Combobox(frame,value=list_text)
comb_des.place(x=330,y=300,height=40,width=150)
comb_des.set("english")

lab_txt=Label(container,text="Destination Text",font=("Time New Roman",20,"bold"),bg="red")
lab_txt.place(x=100,y=360,height=20,width=300)

des_txt=Text(frame,font=("Times New Roman",20,"bold"),wrap=WORD)
des_txt.place(x=10,y=400,height=150,width=480)


container.mainloop()
