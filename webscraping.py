import bs4
import urllib.request
import pandas as pd
from pymongo import MongoClient
#source =requests.get('https://www.jurisitetunisie.com/se/index.php?board=49.0').text
#soup =bs4.BeautifulSoup(source,'html.parser')
def connect_to_mongo():
    try :
        cluster0="mongodb+srv://biat:biat@cluster0.zn7fyk6.mongodb.net/firas?retryWrites=true&w=majority"
        client=MongoClient(cluster0)
        db = client.get_database('firas')
        collection=db.get_collection('DataFrame')
        return collection
    except :
        print("un problème est survenue lors du connexion au serveur")

def scraping(url) :
    try :
        request = urllib.request.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
        raw_response = urllib.request.urlopen(request).read()
        source = raw_response.decode("utf-8") 
        soup =bs4.BeautifulSoup(source,'html.parser')
        return soup
    except :
        print("un problème est survenue lors du <scraping>")

def parcourir_pages(nb , base) :
    try :
        str="https://www.jurisitetunisie.com/se/index.php/board,"
        L=[]
        for i in range(int(nb)) :
            L.append(str+f"{base+0.15*i}")
        return(L)
    except :
        print("un problème est survenue lors du generation des pages pour <scraping>")

def load(tag,nombrepage,base) :
    data=[]
    L=parcourir_pages(nombrepage,base)
    page=0
    nb=0
    #headers =["tag" ,"Question" , "Reponse" ] 
    #df=pd.DataFrame(columns=headers)
    #ancien_df=pd.read_csv('DataFrame.csv',index_col=[0])
    collection=connect_to_mongo()
    for i in L :
        soup=scraping(str(i))
        page+=1
        print(page)
        table=soup.find("table",{"class": "table_grid" ,"cellspacing":"0"})
        for element in table.find_all("tr")[1:] :
            td=element.find("td", {"class":"subject windowbg2"})
            if td==None :
                do=False
            else :
                do=True
            if do==True :
                div=td.find("div", {"style" : "padding-left: 36px; position: relative;"})
                for a in div.find_all("a")[1::2] :
                    soup1=scraping(a['href'])
                    for div in soup1.find_all("div" , {"class" : "inner"})[1:]:
                        data=[tag ,a.text ,div.text]
                        if (collection.find_one({"Response":div.text})==None) :
                            nb=nb+1
                            L=list(collection.find()) 
                            post={"_id" :len(L)+1 , "Tag" : tag ,"Question" : a.text ,"Reponse": div.text}
                            collection.insert_one(post)
    return (int(nb))
                    


            






