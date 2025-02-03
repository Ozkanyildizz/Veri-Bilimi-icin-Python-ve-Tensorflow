import numpy as np 

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1+numbers2
result = numbers1+10 # her değere ekler
result = numbers1-numbers2
result = numbers1-10
result = numbers2*numbers1  # bölme çarpma hepsi olur her değere uygular

result = np.sin(numbers1)
result = np.cos(numbers1)
result = np.sqrt(numbers1) # karekökünü alır
result = np.log(numbers1)  # logaritmasını alır

multi_numbers = numbers1.reshape(2,3)
multi_numbers2 = numbers2.reshape(2,3)

#print(multi_numbers)
#print(multi_numbers2)

result = np.vstack((multi_numbers,multi_numbers2)) # alt alta birleştirme işlemi yapar vertical
result = np.hstack((multi_numbers,multi_numbers2)) # yan yana birleştirme işlemi yapar horizental

result = numbers1 >= 50 # her değer için kontrol eder true false çıktı verir
result = numbers1 % 2 == 0 # çiftse true gönderir
print(numbers1[result])
print(result)

numbers = np.arange(-50,50,15)
ciftler = numbers[numbers % 2 == 0] #çift sayıları getirir
print(ciftler)
