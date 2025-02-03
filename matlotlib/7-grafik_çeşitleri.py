import numpy as nm
import matplotlib.pyplot as plt

numpyDizisi = nm.linspace(0,10,20) # 0 ile 10 arasında 20 tane sayı oluşturur
numpyDizisi2 = numpyDizisi ** 2

## Line Plot
x = nm.linspace(0, 10, 20)
y = x ** 2
plt.plot(x,y)
plt.title("Line Plot")

## Scatter Plot
plt.scatter(numpyDizisi,numpyDizisi2)
plt.title("Scatter Plot")

## Histogram Plot
yeniDizi = nm.random.randint(0, 100, 50) # 50 tane normal dağılım oluşturur
yenidizi2 = yeniDizi ** 2

plt.hist(yeniDizi, bins=10)
plt.title("Histogram Plot")

## Box Plot 
plt.boxplot(yeniDizi*7)
plt.title("Box Plot")

# Barplot 
plt.bar(numpyDizisi, numpyDizisi2)





plt.show()

