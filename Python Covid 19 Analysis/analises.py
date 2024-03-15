from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
frame_top = Frame(frame_quadros, width=200, height=500, bg=co1, relief="flat",)
frame_top.place(x=560, y=0)
lista_pais = ['Angola', "Portugal", 'Brazil', 'India']
lista_valores = [10002, 27265, 3826, 27125]
figura = plt.Figure(figsize=(8.7, 3), dpi=60)
ax = figura.add_subplot(111)

ax.barh(lista_pais, lista_valores,
        align='center', color=cores)
ax.set_alpha(0.3)
c = 0
for i in ax.patches:
    ax.text(i.get_width()+.3, i.get_y()+.50,
            str(lista_valores[c]), fontsize=12, verticalalignment='center', fontstyle='italic', weight='bold', color='dimgrey'
            )
    c += 1
ax.patch.set_facecolor('#FFFFFF')
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['left'].set_linewidth(1)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(False)
ax.xaxis.grid(False)
app_nome_rev = Label(frame_top, text="Top 5 países mais afetados", height=1,
                     pady=5, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
app_nome_rev.grid(row=0, column=0, padx=20, pady=0, sticky=NSEW)
canva = FigureCanvasTkAgg(figura, frame_top)
canva.get_tk_widget().grid(row=1, column=0, sticky=NSEW, columnspan=2)