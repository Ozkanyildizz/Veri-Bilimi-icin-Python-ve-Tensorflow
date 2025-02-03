import numpy as np 



numbers = np.array([0,46,64,64,64,6,4,3,7,4])
result = numbers[5]
result = numbers[-1]
result = numbers[0:6:2] # sıfır ile altı arası ikişerli yaz
result = numbers[::-1] # ters çevir 

# Matrix

numbers2 = np.array([[0,46,64],[64,64,6],[4,3,7,]]) # [satır başlangıcı:  satır sonu, seçilen satırın başlangıcı : sonu]
result = numbers2[0]
result = numbers2[0,2]  # sıfırıncı satır ikinci eleman
result = numbers2[:,2] # bütün satırları seç ve her satırdan ikinci elemanı getir
result = numbers2[:,0] # bütün satırları seç ve her satırdan sıfırıncı elemanı getir
result = numbers2[:,0:2]  # bütün satırları seç ve her satırdan sıfır ile ikinci indeks arasını getir
result = numbers2[-1,:] # -1. elemanı al hepsini yazdır
result = numbers2[-1,0:1] # -1. elemanı al 0-1 . indeksini yazdır
result = numbers2[:2,:2] 

#print(result)

arr1 = np.arange(0,10)
# arr2 = arr1 # referans herhangi bir değişimde ikisinde de değişim olur
arr2 = arr1.copy() # değişiklikte sadece arr2 değişir

arr2[0] = 20 

print(arr1)                   
print(arr2)                   
