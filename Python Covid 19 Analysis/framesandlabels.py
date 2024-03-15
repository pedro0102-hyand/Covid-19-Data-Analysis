frame_Total = Frame(frame_quadros, width=178, height=70,
                    bg=co1, relief="flat",)
frame_Total.place(x=0, y=0)
app_pr = Label(frame_Total, text="", width=1, height=10,
               pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=cor_letra)
app_pr.place(x=0, y=0)
app_nome_rev = Label(frame_Total, text="Total de casos", height=1, pady=0,
                     padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=cor_letra)
app_nome_rev.place(x=10, y=5)
app_nome_va = Label(frame_Total, text="1234567", height=1, pady=0, padx=0,
                    relief="flat", anchor=CENTER, font=('Roboto 16 '), bg=co1, fg="#202124")
app_nome_va.place(x=10, y=35)

frame_recuperados = Frame(frame_quadros, width=178, height=70,
                          bg=co1, relief="flat",)
frame_recuperados.place(x=188, y=0)
app_pr = Label(frame_recuperados, text="", width=1, height=10,
               pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co3, fg=cor_letra)
app_pr.place(x=0, y=0)
app_nome_rev = Label(frame_recuperados, text="Total Recuperado", height=1,
                     pady=0, padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=cor_letra)
app_nome_rev.place(x=10, y=5)
app_nome_va = Label(frame_recuperados, text="1234567", height=1, pady=0,
                    padx=0, relief="flat", anchor=CENTER, font=('Roboto 16 '), bg=co1, fg="#202124")
app_nome_va.place(x=10, y=35)


frame_mortes = Frame(frame_quadros, width=178, height=70,
                     bg=co1, relief="flat",)
frame_mortes.place(x=375, y=0)
app_pr = Label(frame_mortes, text="", width=1, height=10,
               pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co4, fg=cor_letra)
app_pr.place(x=0, y=0)
app_nome_rev = Label(frame_mortes, text="Morte Total", height=1,
                     pady=0, padx=0, relief="flat", anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=cor_letra)
app_nome_rev.place(x=10, y=5)
app_nome_va = Label(frame_mortes, text="1234567", height=1, pady=0,
                    padx=0, relief="flat", anchor=CENTER, font=('Roboto 16 '), bg=co1, fg="#202124")
app_nome_va.place(x=10, y=35)