import tkinter as tk 
from tkinter import *
from tkinter import ttk
from typing import Sized

window = tk.Tk()
window.title("POKEMON ADVENTURE")
window.geometry("649x597")

title = tk.Label(window, text="POKEMON ADVENTURE")
title.place(x=255,y=7)

main = PhotoImage(file="main.png")
screen = tk.Label(window, image=main)
screen.place(x=10,y=40)

title = tk.Label(window, text="MINI MAP")
title.place(x=540,y=60)

mini_main = PhotoImage(file="minimap.png")
mini_screen = tk.Label(window, image=mini_main)
mini_screen.place(x=521,y=90)

Map = tk.Button(window,text="MAP",borderwidth=2,)
Map.place(x=523,y=190,width=100,height=40)

inventory = tk.Button(window,text="INVENTORY",borderwidth=2,)
inventory.place(x=523,y=231,width=100,height=40)

pokedex = tk.Button(window,text="POKEDEX",borderwidth=2,)
pokedex.place(x=523,y=272,width=100,height=40)

roster = tk.Button(window,text="ROSTER",borderwidth=2,)
roster.place(x=523,y=313,width=100,height=40)

journal = tk.Button(window,text="JOURNAL",borderwidth=2,)
journal.place(x=523,y=354,width=100,height=40)

help = tk.Button(window,text="HELP",borderwidth=2,)
help.place(x=523,y=395,width=100,height=40)

shop = tk.Button(window,text="SHOP",borderwidth=2,)
shop.place(x=523,y=436,width=100,height=40)

nw = tk.Button(window,text="NW",borderwidth=2,)
nw.place(x=10,y=490,width=30,height=30)

n = tk.Button(window,text="N",borderwidth=2,)
n.place(x=40,y=490,width=30,height=30)

ne = tk.Button(window,text="NE",borderwidth=2,)
ne.place(x=70,y=490,width=30,height=30)

w = tk.Button(window,text="W",borderwidth=2,)
w.place(x=10,y=520,width=30,height=30)

sw = tk.Button(window,text="SW",borderwidth=2,)
sw.place(x=10,y=550,width=30,height=30)

s = tk.Button(window,text="S",borderwidth=2,)
s.place(x=40,y=550,width=30,height=30)

se = tk.Button(window,text="SE",borderwidth=2,)
se.place(x=70,y=550,width=30,height=30)

e = tk.Button(window,text="E",borderwidth=2,)
e.place(x=70,y=520,width=30,height=30)

logo = PhotoImage(file="logo.png")
nintendo = tk.Label(window, image=logo)
nintendo.place(x=270,y=500)

#done









window.mainloop()

#done
