import pandas as pd
import numpy as np

mmasSozluk = {"isim": ["Ali", "Veli", "Ayşe", "Fatma", "Mehmet"],
            "Depertmant": ["Yazılım", "Satıs", "Pazarlama", "Pazarlama", "Yazılım"],
              "maas": [1000, 2000, 3000, 4000, 5000]}
maasDataFrame = pd.DataFrame(mmasSozluk)
# print(maasDataFrame)

result = maasDataFrame["Depertmant"].unique() 
result = maasDataFrame["Depertmant"].nunique() # kaç farklı değer var
result = maasDataFrame["Depertmant"].value_counts() # kaç tane hangi değerden var

def bruttenNete(maas):
    return maas * 0.66 
result = maasDataFrame["maas"].apply(bruttenNete) # apply fonksiyonu ile her bir elemana fonksiyon uygulayabiliriz

result = maasDataFrame.isnull() # null değer var mı
result = maasDataFrame["maas"].dropna() # null değerleri siler

yeniVeri = {"karakter": ["Süperman", "Süperman", "Wonderwoman", "Wonderwoman","Süperman"],
            "kaeakter ismi": ["Clark Kent", "Bruce Wayne", "Peter Parker", "Diana Prince","Diana Prince"],
            "karakter yas": [9, 10, 50, 20,10]}
karakterDF = pd.DataFrame(yeniVeri)
# print(karakterDF)

result = karakterDF.pivot_table(values="karakter yas", index=["karakter", "kaeakter ismi"], aggfunc=np.sum)


print(result)