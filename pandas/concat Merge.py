import numpy as np
import pandas as pd

sozluk1 = {"Isımler": ["Ahmet","Mehmet","Zeynep","Atıl"],
           "Spor": ["koşu","yüzme","koşu","basketbol"],
           "Kalori" : [100,200,300,300]} 
dataF1 = pd.DataFrame(sozluk1,index=[1,2,3,4])

sozluk2 = {"Isımler": ["Atlas","Ali","Veli","Atıl"],
           "Spor": ["koşu","yüzme","koşu","basketbol"],
           "Kalori" : [100,200,300,300]} 
dataF2 = pd.DataFrame(sozluk2,index=[5,6,7,8])

sozluk3 = {"Isımler": ["Veli","Merve","Furkan","Atıl"],
           "Spor": ["koşu","yüzme","futbol","tenis"],
           "Kalori" : [100,200,300,300]} 
dataF3 = pd.DataFrame(sozluk3,index=[8,9,10,11])

# concatenation birleştirme
concat = pd.concat([dataF1,dataF2,dataF3])
print(concat)

# merge 

mergesozluk1 = {"Isımler": ["Ahmet","Mehmet","Zeynep","Atıl"],
           "Spor": ["koşu","yüzme","koşu","basketbol"]} 
merge1 = pd.DataFrame(mergesozluk1)

mergesozluk2 = {"Isımler": ["Ahmet","Mehmet","Zeynep","Atıl"],
           "kalori": [100,200,300,300]} 
merge2 = pd.DataFrame(mergesozluk2)

merge = pd.merge(merge1,merge2,on="Isımler")
print(merge)