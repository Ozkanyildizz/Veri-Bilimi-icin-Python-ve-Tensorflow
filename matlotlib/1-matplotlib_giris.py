import numpy as nm
import matplotlib.pyplot as plt 

yasListesi = [10,20,30,40,50,60,70,80,90,100]
kiloListesi = [20,75,70,80,60,70,80,90,100,95]

numpyYasListesi = nm.array(yasListesi)
numpyKiloListesi = nm.array(kiloListesi)

# print(numpyYasListesi)
# print(numpyKiloListesi)

# plt.plot(numpyKiloListesi,numpyYasListesi,"g") # g: green genelde r g b kullanılır 
plt.plot(numpyYasListesi,numpyKiloListesi,"r") 
plt.xlabel("Yas") 
plt.ylabel("Kilo") 
plt.title("Kilonun Yaşa Göre Değişimi")
plt.show()



