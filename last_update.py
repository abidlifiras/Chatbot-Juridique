import re
import pandas as pd
from webscraping import *


def update() :
    df=pd.read_excel('last_update.xlsx')
    for i in df.index :
        L=[]
        soup=scraping(df['Site'][i])
        div=soup.find("div", {"class":"pagelinks floatleft"})
        a=div.find_all("a", {"class":"navPages"})
        L=list(a)
        lien=L[len(L)-1]
        soup1=scraping(lien['href'])
        table=soup1.find("table",{"class": "table_grid" ,"cellspacing":"0"})
        elements=table.find_all("tr")[1:] 
        L2=list(elements)
        element=L2[len(L2)-1]
        td=element.find("td", {"class":"subject windowbg2"})
        if td==None :
            do=False
        else :
            do=True
        if do==True :
                div=td.find("div", {"style" : "padding-left: 36px; position: relative;"})
                a1 = div.find_all("a")
                L1=list(a1)
                if len(L1)==1 :
                    ch=L1[len(L1)-1]['href']
                else :
                    ch=L1[len(L1)-2]['href']    
                nb=re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?",ch)[0]
                if nb == str(float(df['Dernier_question'][i] )):
                    print(f"Pas de maj pour {df['Tag'][i]}")
                    print("--------------------------------------------------------")

                else :
                    try :
                        print(f"En train de faire une maj sur {df['Tag'][i]}")
                        base=re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?",df["Site"][i])[0]
                        nb=load(df["Tag"][i],lien.text,int(float(base)))
                        df['Dernier_question'] = df['Dernier_question'].replace([df['Dernier_question'][i]],nb)                    
                        df.to_excel('last_update.xlsx',index=False)
                        print(f"màj terminé sur {df['Tag']} : {nb} ligne(s) a été ajoutée(s) !")
                    except :
                        print(f"un problème est survenue lors du màj sur {df['Tag']}")

                    print("--------------------------------------------------------")
update()
