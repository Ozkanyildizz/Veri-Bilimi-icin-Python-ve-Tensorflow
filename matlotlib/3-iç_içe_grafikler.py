import numpy as nm
import matplotlib.pyplot as plt

numpyDizisi = nm.linspace(0,10,20) # 0 ile 10 arasında 20 tane sayı oluşturur
numpyDizisi2 = numpyDizisi ** 3

figure = plt.figure()
eksen1 = figure.add_axes([0.1,0.1,0.7,0.7])
eksen2 = figure.add_axes([0.22,0.35,0.3,0.3])

eksen1.plot(numpyDizisi,numpyDizisi2,"g")
eksen1.set_xlabel("X Ekseni")
eksen1.set_ylabel("Y Ekseni")
eksen1.set_title("Ana Grafik Başlık")

eksen2.plot(numpyDizisi2,numpyDizisi,"b")
eksen2.set_xlabel("X Ekseni küçük")
eksen2.set_ylabel("Y Ekseni küçük")
eksen2.set_title("Küçük Grafik Başlık")



plt.show()
