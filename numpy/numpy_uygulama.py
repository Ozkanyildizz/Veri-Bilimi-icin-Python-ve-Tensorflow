import numpy as np

# 1- (10,15,30,45,60) numpy dizisini oluştur
result = np.array([10,15,30,45,60])
# 2- (5-15) arasında numpy dizisini oluşturun
result = np.arange(5,15)
# 3- (50,100) arasında 5er artan dizi
result = np.arange(50,100,5)
# 4- 10 elemanlı sıfırdan oluşan dizi
result =  np.zeros(10)
# 5- 10 elemanlı birlerden oluşan diz
result = np.ones(10)
# 6- (0-100) arasında eşit aralıklı 5 sayı üretin
result = np.linspace(0,100,5)
# 7- (10-30) arasında rastgele 5 tane sayı üret
result  = np.random.randint(10,30,5)
# 8- (-1 ile 1) arasında 10 adet sayı üretin 
result = np.random.randn(5)
# 9- (3x5) boyutunda (10-50) arasında rastgele bir matris oluştur
sayı = np.random.randint(10,50,15)
matris = sayı.reshape(3,5)
# 10- üretilen matrislerin satır ve stun sayıları tolamı
result = matris.sum(axis=0)
result = matris.sum(axis=1)
# 11 - üretilen matriks en büyük en küçük ve ortalaması
result = matris.max()
result= matris.min()
result = matris.mean()
# 12- üretilen matriksin en büyüğünün ve küçüğünün indeksi
result = matris.argmax()
result = matris.argmin()
# 13- (10-20) arasındaki sayıları içeren dizinin ilk üç elemanını seçiniz
number = np.arange(10,20)
result = number[:3]
# 14- tersten yazdırın
result = number[::-1]
# 15- üretilen matrisin ilk satırını seçin
result = matris[0]
# 16- matrisin 2. satırı 3. stunundaki eleman
print(matris)
result = matris[1,2]
# 17- matrisin tüm satırındaki ilk eleman
result = matris[:,0]
# 18- matrisin her elemanın karesini alın
result = np.sqrt(matris)
# 19- matrisin elemanlarının hangisi pozitif çift sayıdır ?
numbers = np.arange(-50,50,15)
ciftler = numbers[numbers % 2 == 0]
result= ciftler[ciftler>0]
# 20 dizinin şeklini yazan metod
result = numbers.shape


print(result)