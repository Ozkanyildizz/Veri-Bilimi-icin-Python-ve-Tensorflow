import numpy as nm
import matplotlib.pyplot as plt

numpyDizisi = nm.linspace(0,10,20) # 0 ile 10 arasında 20 tane sayı oluşturur
numpyDizisi2 = numpyDizisi ** 3

#plt.plot(numpyDizisi,numpyDizisi2,"g--") # g-- kesik çizgi 
#plt.plot(numpyDizisi,numpyDizisi2,"g*-") # g*- yıldızlı çizgi

# plt.xlabel("X Ekseni") 
# plt.ylabel("Y Ekseni")
# plt.title("Grafik Başlığı")

## 2 grafik yan yana
# plt.subplot(1,2,1) # 1 sıra 2 kolon olacak 1. grafik
# plt.plot(numpyDizisi,numpyDizisi2,"r*-")
# plt.subplot(1,2,2) # 1 sıra 2 kolon olacak 2. grafik
# plt.plot(numpyDizisi2,numpyDizisi,"g--")

## kendimize ait bir figure oluşturmak
benimFigure = plt.figure() # boş bir figure oluşturur
figureAxes = benimFigure.add_axes([0.15,0.1,0.4,0.4]) # x,y,genişlik,yükseklik
figureAxes.plot(numpyDizisi,numpyDizisi2,"g")
figureAxes.set_xlabel("X Ekseni")
figureAxes.set_ylabel("Y Ekseni")
figureAxes.set_title("Grafik Başlığı")

plt.show()
