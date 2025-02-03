import numpy as np
import pandas as pd 

data = np.random.randn(4,3)
print(data)
dataFrame = pd.DataFrame(data)
print(dataFrame[0])

#pd.options.display.max_rows = 1000 termşnalde en fazla gösterimi 1000e çıkarır
data2 = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data2)
print(df)

yenDdataFrame = pd.DataFrame(data=data,
                             index=["Özkan","Yaren","Zeynep","ahmet"],
                             columns=["maaş","yaş","çalışma saati"])

print(yenDdataFrame["yaş"]) # yaşı getirir
print(yenDdataFrame.loc["Özkan"]) # özkanın bütün değerlerini getirir
print(yenDdataFrame.loc["Özkan"]["yaş"]) # özkanın yaş değerini getirir
print(yenDdataFrame.loc["Özkan","yaş"]) # özkanın yaş değerini getirir
print(yenDdataFrame["yaş"]["Özkan"]) # özkanın yaşını getirir
print(yenDdataFrame.iloc[1]) # 1. indelsteki değerleri getirir

# data frame'e veri ekleme
yenDdataFrame["emeklilik yaşı"] = yenDdataFrame["yaş"] + yenDdataFrame["yaş"]
print(yenDdataFrame)

# data frame veri silme  orjinal data frame'de değişiklik yapmaz
print(yenDdataFrame.drop("emeklilik yaşı",axis=1))
print(yenDdataFrame.drop("Zeynep",axis=0))
# data framde de değişiklik yapar siler
yenDdataFrame.drop("emeklilik yaşı",axis=1, inplace=True) # bunun için inplace kullanılır
print(yenDdataFrame)
print(yenDdataFrame<0) # true false dödürür
print(yenDdataFrame[yenDdataFrame<0]) # sıfırdan küçük değerleri dödürür
print(yenDdataFrame[yenDdataFrame["yaş"]<0]) # yaşı sıfırdan küçük kişileri dödürür

print(yenDdataFrame.reset_index()) # ineksleri 0,1,2.. ile değiştirir
yenDdataFrame["Yeni indeks"]= ["Öz","yar","Zey","aho"]
print(yenDdataFrame.set_index("Yeni indeks",inplace=True)) # yendeksleri yenileri ile değiştirir

 
