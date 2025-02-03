import pandas as pd 
import numpy as np

havaDurumu = {"Istanbul ": [20,20,np.nan],"Ankara":[20,np.nan,30],"Izmır":[30,50,40]}
havaDurumuData = pd.DataFrame(havaDurumu,index=[1,2,3])
print(havaDurumuData)

# eksik verileri silme 
dropnasatır = havaDurumuData.dropna() # na olan bütün satırları siler 
dropnastun = havaDurumuData.dropna(axis=1) # na olan bütün sütünları siler 
print(dropnastun)

yeniVeri = {"Istanbul ": [20,20,np.nan],"Ankara":[20,np.nan,30],"Izmır":[30,50,40],"Antalya":[40,np.nan,np.nan]}
havaDurumuData2 = pd.DataFrame(yeniVeri,index=[1,2,3])
dropna = havaDurumuData2.dropna(axis=1,thresh=2)
NaDeğerVer = havaDurumuData2.fillna(0)
print(dropna)
print(NaDeğerVer)


