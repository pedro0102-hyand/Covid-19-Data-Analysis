frame_paises=Frame(frame_quadros,wdith=700,height=500,bg=co1,relief="flat",)
frame_paises.place(x=0,y=80)

style = ttk.Style()
style.element_create("Custom.Treeheading.border", "from", "default")
style.layout("Custom.Treeview.Heading", [
    ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
    ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
        ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
            ("Custom.Treeheading.image", {'side': 'right', 'sticky': ''}),
            ("Custom.Treeheading.text", {'sticky': 'we'})
        ]})
    ]}),
])
style.configure("Custom.Treeview.Heading",
                background="#494d4a", foreground="white", relief="raised")
style.map("Custom.Treeview.Heading",
          relief=[('active', 'groove'), ('pressed', 'sunken')])

lista_head=['País','Total Confirmado','Total Recuperado','Total mortes','Data']
free=ttk.Treeview(frame_paises,selectmode="extends",style="Custom.Treeview",height=18,columns=lista_head,show="headings")
vsb=ttk.Scrollbar(frame_paises,orient="vertical",command=tree.yview)
hsb=ttk.Scrollbar(frame_paises,orient="horizontal",comand=tree.xview)
tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
tree.grid(column=0,row=1,sticky='nsew')
vsb.grid(column=1,row=1,sticky='ns')
hsb.grid(column=0,row=2,sticky='ew')
frame_paises.grid_rowconfigure(0,weight=2)

hd=["nw","center","center","center","center","center","center"]
h=[140,100,100,100,91]
n=0



for col in lista_head:
    tree.heading(col,text=col.title(),anchor=CENTER)
    tree.column(col,wdith=h[n],anchor=hd[n])
    n=n+1
