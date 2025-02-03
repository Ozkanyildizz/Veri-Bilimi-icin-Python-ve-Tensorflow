import numpy as nm
import matplotlib.pyplot as plt

numpyDizisi = nm.linspace(0,10,20) # 0 ile 10 arasında 20 tane sayı oluşturur
numpyDizisi2 = numpyDizisi ** 3

(benimfigure,benimEksenler )=plt.subplots(nrows=1,ncols=2)
# benimEksenler.plot(numpyDizisi,numpyDizisi2,"g") dizi olduğu için hata verir
print(type(benimEksenler))

for eksen in benimEksenler:
    eksen.plot(numpyDizisi,numpyDizisi2,"g")
    eksen.set_xlabel("X Ekseni")

plt.tight_layout() # grafikler arasındaki boşlukları ayarlar
plt.show()