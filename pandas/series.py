import pandas as pd
seri1 = pd.Series(["Özkan","Yaren","Zeynep"],[1,2,3])  # ilk değer isimler olur ikincisi indeks
seri2 = pd.Series([10,20,30],["Özkan","Yaren","Zeynep"])
seri3 = pd.Series([100,200,300,300],["Özkan","Yaren","Zeynep","ahmet"])

result= seri2["Özkan"]

result = seri2+seri3 # farklı değerler varsa NAN döndürür




print(result)




