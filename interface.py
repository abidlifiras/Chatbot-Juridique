from operator import index
from time import sleep
from tkinter import *
from tkinter.ttk import Treeview
from last_update import *

#---------------------------------------------------------------------------
def auth(event=None) :
    rep=entry_field1.get()
    if rep.upper()!="ROOT" :
        view.title("MOT PASSE INVALIDE !!!")
        sleep(2)
        view.destroy()
        interface()
        return None
    else :
        view.title("CONNEXION ...")
        sleep(2)
        view.destroy()
        serveur()

def interface() :
    global view , entry_field1
    view=Tk()
    view.title("Authentification")
    view.geometry("300x150")
    ch=Label(view,text="**** TAPEZ MOT DE PASSE SERVEUR ****")
    ch.pack()
    entry_field1=Entry(view, show="*" ,text="")
    entry_field1.bind("<Return>", auth)
    entry_field1.pack()
    send_button =Button(view, text="repondre")
    send_button.bind("<ButtonRelease-1>", auth)
    send_button.pack()
    view.mainloop()

def serveur() :
    global scene 
    scene=Tk()
    scene.geometry("400x300")
    scene.title("Web scraping")
    mainmenu=Menu(scene)
    firstmenu=Menu(mainmenu)
    firstmenu.add_command(label="Voir liste des Tags",command=voir_tag)
    firstmenu.add_command(label="Ajouter Tag",command=Ajouter_Tag)
#    firstmenu.add_command(label="Faire une mise à jour ",command=faire_maj)
    firstmenu.add_separator()
    firstmenu.add_command(label="Quitter",command=quitter)

    mainmenu.add_cascade(label="Cliquez ici",menu=firstmenu)
    scene.config(menu=mainmenu)
    scene.mainloop()
  
#-------------------------------------------------------------------------------------------------
def voir_tag(event=None):
    view=Tk()
    view.title("consulter les tags")
    tableview=Treeview(view,columns=(1),height=10, show ="headings")
    tableview.heading(1,text="Tag")
    df=pd.read_excel('last_update.xlsx')
    for i in df.index :
        L=list(str(df['Tag'][i]))
        ch=''
        for j in L :
            ch=ch+j
        tableview.insert('',END,values=ch)



    tableview.pack()
    view.mainloop()

def Ajouter_Tag(event=None):
    global entry_field2
    ch=Label(scene,text=" Tapez Tag")
    ch.pack()
    entry_field2=Entry(scene ,text="")
    entry_field2.bind("<Return>", ajouter)
    entry_field2.pack()
    global entry_field3
    ch=Label(scene,text=" Tapez le site")
    ch.pack()
    entry_field3=Entry(scene ,text="")
    entry_field3.bind("<Return>", ajouter)
    entry_field3.pack()
    send_button =Button(scene, text="repondre")
    send_button.bind("<ButtonRelease-1>", ajouter)
    send_button.pack()
    scene.update()
def ajouter():
    b=1


def quitter():
    scene.destroy()



interface()

