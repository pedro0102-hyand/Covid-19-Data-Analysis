import pandas as pd 
import numpy as np 

frame_categoria=Frame(frame_quadros,wdith=200,height=200,bg=co1,relief="flat",)
frame_categoria.place(x=562,y=220)
lista_continentes_valor=[3568870,27195616,19517392,22281680,1794942,19269056]
lista_continentes_nome=['Africa','Asia','Europe','Oceania','South-America']
figura=plt.Figure(figsize=(8.65,3.9),dpi=60)
ax=figura.add_subplot(111)

colors = ['#5588bb', '#66bbbb', '#aa6644',
          '#99bb55', '#ee9944', '#444466', '#bb5555']


wedges,texts=ax.pie(lista_continentes_valor,wedgepros=dict(wdith=0.2),colors=colors,shadow=True,startangle=-90)
bbox_props=dict(boxstyle="square,pad=0.3",fc="w",ec="k",lw=0.72)
kw=dict(arrowprops=dict(arrowstyle="-"),bbox=bbox_props,zorder=0,va="center")


for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(lista_continentes_nome[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

app_categoria = Label(frame_categoria, text="Continente mais afetado", height=1,
                      pady=5, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
app_categoria.grid(row=0, column=0, pady=0,
                   padx=20, columnspan=2, sticky=NSEW)
canva_cont = FigureCanvasTkAgg(figura, frame_categoria)
canva_cont.get_tk_widget().grid(row=1, column=0, sticky=NSEW)
