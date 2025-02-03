import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("kelime.csv")

pd.options.display.max_rows = 1000
print(pd.options.display.max_rows) 

print(data)
print(data.info())
print(data.duplicated())
data.drop_duplicates(inplace = True) # aynı olanları siler

print(data)

data = pd.read_excel("note.xlsx")


delodegerler = data.dropna() # null olanları siler
result = delodegerler.to_excel("note2.xlsx")
print(result)

## read_csv 
## to_csv

"""  
    birkaç uygulama 

"""
# Titanic veri setini okuma
titanic_data =  pd.read_csv("titanic.csv")


print(titanic_data.head())

# Genel bilgiler ve özet istatistikler
print(titanic_data.info())
print(titanic_data.describe())

# Eksik verileri kontrol etme
print(titanic_data.isnull().sum())

# Yaş sütunundaki eksik değerleri ortalama ile doldurma
titanic_data['Age'].fillna(titanic_data['Age'].mean(), inplace=True)

# Cinsiyet ve hayatta kalma oranlarını analiz etme
survival_by_gender = titanic_data.groupby('Sex')['Survived'].mean()
print(survival_by_gender)

# Yaş dağılımını görselleştirme
titanic_data['Age'].hist(bins=20)
plt.title("Yaş Dağılımı")
plt.xlabel("Yaş")
plt.ylabel("Frekans")
plt.show()