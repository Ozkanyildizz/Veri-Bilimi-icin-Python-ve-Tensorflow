import numpy as np 

result = np.array([1,2,3,5,56,7])
result = np.arange(1,10)  # bir ile 10 arasında liste yapar
result = np.arange(10,100,3) # üçerli artar
result = np.zeros(10) # on tane sıfır 
result = np.ones(10)# on tane bir
result = np.linspace(0,100,5) # eşit beş aralığa böler
result = np.linspace(0,5,5)
result = np.random.randint(0,10) # random bir sayı getirir maks 9
result = np.random.randint(20) 
result = np.random.randint(1,10,3)
result = np.random.rand(5) # sıfır ile 1 arasında 5 tane sayı getirir
result = np.random.randn(5) # negatifte alır

np_array = np.arange(50)
np_multi = np_array.reshape(5,10)
print(np_multi.sum(axis=1))  # satırların toplamını verir
print(np_multi.sum(axis=0)) # stunların toplamını verir

rnd_numbers = np.random.randint(1,100,10)
result = rnd_numbers.max()
result = rnd_numbers.min()
result = rnd_numbers.mean() # ortalamasını veriri
result = rnd_numbers.argmax() # maxın indeksini verir
result = rnd_numbers.argmin() # minin indeksini verir

print(rnd_numbers)
print(result)