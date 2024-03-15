import tkinter
from tkinter import Frame
from tkinter import ttk
from tkinter import *
cor="#feffff"
cor_fundo="#3a3a4d"
janela=Tk()
frame_app_nome=Frame(janela,wdith=1365,height=45,pady=0,padx=0,bg=cor,relief="flat")
frame_app_nome.grid(row=0,column=0)
ttk.Separator(janela,orient=HORIZONTAL).grid(row=1,columnspan=1,ipadx=680)
frame_quadros=Frame(janela,width=1365,height=500,bg=cor_fundo,pady=0,padx=0,relief="flat")
frame_quadros.grid(row=3,column=0,sticky=NW)



