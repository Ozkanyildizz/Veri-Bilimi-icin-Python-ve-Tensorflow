import numpy as nm
import matplotlib.pyplot as plt

numpyDizisi = nm.linspace(0,10,20) # 0 ile 10 arasında 20 tane sayı oluşturur
numpyDizisi2 = numpyDizisi ** 2
numpyDizisi3 = numpyDizisi ** 3

yeniFigur , yeniEksen = plt.subplots()
yeniEksen.plot(numpyDizisi,numpyDizisi ,color = "red",alpha = 0.5) # alpha saydamlık
yeniEksen.plot(numpyDizisi ,numpyDizisi + 2,linewidth = 5.0,linestyle="--") # linewidth çizgi kalınlığı
yeniEksen.plot(numpyDizisi ,numpyDizisi + 4,linewidth = 5.0,linestyle="-.") # linestyle çizgi stili
yeniEksen.plot(numpyDizisi ,numpyDizisi + 6,linewidth = 5.0,linestyle=":") # linestyle çizgi stili

yeniEksen.plot(numpyDizisi ,numpyDizisi + 8,color = "000000",
               linewidth = 5.0, # linewidth çizgi genişliği
               linestyle="--", # linestyle çizgi stili 
               marker = "o", # değerleri 0 ile işaretle
               markersize = 8, # işaretleyici boyutu
               markerfacecolor="red" # işaretleyici rengi
               ) 

plt.show() 