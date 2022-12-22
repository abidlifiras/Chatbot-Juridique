import pymongo
import pandas 

cluster0="mongodb+srv://biat:biat@cluster0.zn7fyk6.mongodb.net/firas?retryWrites=true&w=majority"
client=pymongo.MongoClient(cluster0)
db = client.get_database('firas')
collection=db.get_collection('DataFrame')
#collection.insert_one({"_id" : 0 , "Tag" : "this is a tag" ,"Question" : "this this question " ,"Reponse": "this is a reponse"})
L=list(collection.find())
print(len(L))
#try :
   # for i in df.index :
     #   post={"_id" : i , "Tag" : df['tag'][i] ,"Question" : df['Question'][i] ,"Reponse": df['Reponse'][i]}
     #   collection.insert_one(post)
  #  print("terminier avec succes")
#except :
   # print("un erreur est survenue")