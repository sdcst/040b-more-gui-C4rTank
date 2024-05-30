import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("390x116")

p = tk.Entry(window,text="")
p.place(x=0,y=30,width=129,height=25)

p_text = tk.Label(window, text="Principal")
p_text.place(x=37,y=5)

ir = tk.Entry(window,text="")
ir.place(x=127,y=30,width=129,height=25)

ir_text = tk.Label(window, text="Interest Rate")
ir_text.place(x=155,y=5)

years = ttk.Combobox(window,values=["didn't say what to put here"])
years.place(x=255,y=30,width=135,height=25)

years_text = tk.Label(window, text="Years")
years_text.place(x=305,y=5)

amo = tk.Entry(window,text="")
amo.place(x=127,y=91,width=129,height=25)

amo_text = tk.Label(window, text="Amount")
amo_text.place(x=74,y=91)

line = tk.Label(window, text="-")
line.place(x=60,y=58)

window.mainloop()

#done
