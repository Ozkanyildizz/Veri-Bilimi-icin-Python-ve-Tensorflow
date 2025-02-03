import numpy as nm
import matplotlib.pyplot as plt

numpyDizisi = nm.linspace(0,10,20) # 0 ile 10 arasında 20 tane sayı oluşturur
numpyDizisi2 = numpyDizisi ** 2
numpyDizisi3 = numpyDizisi ** 3
 
# dpi=150 çözünürlük ayarı sonradan da eklenebilir
yenifigur = plt.figure(figsize=(8,5) ) # figsize=(8,5) 10x5 boyutunda bir figür oluşturur
yeniEksen = yenifigur.add_axes([0.1,0.1,0.9,0.9])

yeniEksen.plot(numpyDizisi,numpyDizisi2,label ="numpayDizisi ** 2")
yeniEksen.plot(numpyDizisi,numpyDizisi3 ,label ="numpayDizisi ** 3")

yeniEksen.legend(loc=(1,0)) # label gösterir sağ üst köşede x ve y eksenine göre
yeniEksen.legend(loc=2) # label gösterir sol alt köşede
yeniEksen.legend(loc=3) # label gösterir sol alt köşede
yeniEksen.legend(loc=4) # label gösterir sağ alt köşede
yeniEksen.legend(loc=(0.5,0)) 

yeniEksen.set_xlabel("X Ekseni")
yeniEksen.set_ylabel("Y Ekseni")
yeniEksen.set_title("Grafik Başlığı")

yenifigur.savefig("benimfigur.png",dpi=200) # Çizimi kaydeder dpi çözünürlüğü ayarlar
plt.show() # Çizimi gösterir
