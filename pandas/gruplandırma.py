import pandas as pd 
import numpy as np

maasDic = {"Departmanlar": ["Yazılım","Yazılım","Pazarlama","Pazarlama","Hukuk","Hukuk"],
           "Çalışan isim": ["Ahmet","Mehmet","Özkan","Yaren","zeynep","Ali"],
           "Maas": [1000,5000,6000,4000,700,9000]}

maasDataFrame = pd.DataFrame(maasDic)
grupObjesi = maasDataFrame.groupby("Departmanlar")
print(grupObjesi.count()) #kaç kişi olduğunu gösterir
print(grupObjesi.min()) # min maaş 
print(grupObjesi.max()) # max maaş 
#print(grupObjesi.mean()) # ortalama maaş
print(grupObjesi.describe())

