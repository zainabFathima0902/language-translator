from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    trans=Translator()
    try:
        trans1=trans.translate(text,src=src, dest=dest)
        return trans1.text
    except Exception as e:
        return f"Error: {str(e)}"

def data():
    s =comb_sor.get()
    d = comb_des.get()
    masg=sor_txt.get(1.0, END)
    textget=change(text=masg,src=s, dest=d)
    des_txt.delete(1.0, END)
    des_txt.insert(END, textget)

def validate_translation():
    if not sor_txt.get(1.0, END).strip():
        messagebox.showerror("Input Error", "Source text cannot be empty")
        return False
    if comb_sor.get() not in LANGUAGES.values():
        messagebox.showerror("Input Error", "Invalid source language selected")
        return False
    if comb_des.get() not in LANGUAGES.values():
        messagebox.showerror("Input Error", "Invalid destination language selected")
        return False
    return True

def handle_translate():
    if validate_translation():
        data()

container=Tk()
container.title("Translator")
container.geometry("500x700")
container.config(bg="Red")

lab_txt=Label(container, text="Translator", font=("Times New Roman", 40, "bold"))
lab_txt.place(x=100, y=40, height=50, width=300)

lab_src_txt=Label(container, text="Source Text", font=("Times New Roman", 20, "bold"), bg="red")
lab_src_txt.place(x=100, y=100, height=20, width=300)

sor_txt=Text(container,font=("Times New Roman", 20, "bold"), wrap=WORD)
sor_txt.place(x=10, y=130, height=150, width=480)

list_text=list(LANGUAGES.values())
comb_sor= ttk.Combobox(container, value=list_text)
comb_sor.place(x=10, y=300, height=40,width=150)
comb_sor.set("english")

button_change= Button(container,text="Translate", relief=RAISED, command=handle_translate)
button_change.place(x=170, y=300, height=40, width=150)

comb_des=ttk.Combobox(container,value=list_text)
comb_des.place(x=330, y=300, height=40, width=150)
comb_des.set("english")

lab_des_txt=Label(container,text="Destination Text", font=("Times New Roman", 20, "bold"), bg="red")
lab_des_txt.place(x=100, y=360, height=20, width=300)

des_txt=Text(container, font=("Times New Roman", 20, "bold"), wrap=WORD)
des_txt.place(x=10, y=400, height=150, width=480)

container.mainloop()



