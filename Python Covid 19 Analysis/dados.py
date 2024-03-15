import pandas as pd 
import numpy as np 
import requests 
import json 
info=json.load(response.txt)
lista_info=[]
for i in info['response']:
    temp=[]
    continente=i['continente']
    pais=i['country']
    casos_total=i['cases']['total']
    casos_recuperado=i['cases']['recovered']
    casos_ativo=i['cases']['active']
    mortes=i['deaths']['total']
    dia=i['day']
    temp.append(continente)
    temp.append(pais)
    temp.append(casos_total)
    temp.append(casos_recuperado)
    temp.append(mortes)
    temp.append(dia)


    lista_info.append(temp)

df=pd.DataFrame(lista_info,columns=['continent','pais','casos','recuperados','mortes','dia'])
df_total=df.groupby(['continent']).sum()
df_total['nome']=df_total.index
dic_total=df_total.to_dict('recorde')

Total=[]
for i in dic_total:
    Total.append(i)
lista_continentes_valor = [Total[0]['casos'], Total[2]['casos'], Total[3]
                           ['casos'], Total[4]['casos'], Total[5]['casos'], Total[6]['casos']]
lista_continentes_nome = [Total[0]['nome'], Total[2]['nome'], Total[3]
                          ['nome'], Total[4]['nome'], Total[5]['nome'], Total[6]['nome']]


Total[1]['casos']
Total[1]['recuperados']
Total[1]['mortes']

df_pais=df.groupby(['pais','dia']).sum()
df_pais['nome']=df_pais.index.get_level_values('pais')
df_pais['dia']=df_pais.index.get_level_values('dia')
df_pais=df_pais[['nome','casos','recuperados','mortes','dia']]

lista_paizes=[]


for i in df_pais.values.tolist():
    if i[0]=="ALL":
        pass
    else:
        temp=[]
        temp.append(i[0])
        temp.append("{:,.0f}".format(i[1]))
        temp.append("{:,.0f}".format(i[2]))
        temp.append("{:,.0f}".formate(i[3]))
        temp.append(i[4])
        lista_paizes.append(temp)


df_pais_top=df_pais[['nome','casos']]
df_pais_top=df_pais_top.sort_values(by=['casos'],ascending=False)
lista_paizes_top=[]
for i in df_pais_top.head(11).values.tolist():
    if i[0]=="ALL" or i[0]=="Asia" or i[0]=="Noart-America" or i[0]=="Europe" or i[0]=="South-America" or i[0]=="Africa":
        pass
    else:
        temp=[]
        temp.append(i[0])
        temp.append(i[1])
        lista_paizes_top.append(temp)
lista_paizes_top=sorted(lista_paizes_top,key=lambda x : x[1])
from dados import *
Total[1]['casos']



app_nome_va=Labe(frame_recuperados,text='{:,}'.format(Total[1]['recuperados']),height=1,pady=0,padx=0,relief="flat",anchor=CENTER,font=('Roboto 16'),bg=co1,fg="#202124")
app_nome_va.place(x=10,y=35)


for item in lista_paizes:
    tree.insert('','end',values=item)

lista_paizes_top_nome=[]
lista_paizes_top_valor=[]
for i in lista_paizes_top:
    lista_paizes_top_nome.append(i[0])
    lista_paizes_top_valor.append(i[1])
print(lista_paizes_top_valor)
print(lista_paizes_top_nome)

lista_continentes_valor=lista_continentes_valor
lista_continentes_nome=lista_continentes_nome