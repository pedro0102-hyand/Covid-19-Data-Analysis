from tkinter import Label
from tkinter import Frame
from tkinter import ttk
from tkinter import *
janela=Tk()
cor="#feffff"
cor_fundo="#3a3a4d"
frame_app_nome=Frame(janela,wdith=1365,height=45,pady=0,padx=0,bg=cor,relief="flat")
app_nome=Label(frame_app_nome,text="COVID-19 ANALYSIS",width=32,height=2,pady=5,padx=0,relief="flat",anchor="nw",font=('Ivy 17 bold'),bg=cor,fg=cor_letra)
app_nome.place(x=0,y=0)
