import numpy as np
import pandas as pd 


ilk_indeks = ["Simpson","Simpson","Simpson",
              "South Park","South Park","South Park"]
ic_indeks = ["Homer","Bart","Marge","Cartmen","Kenny","Kyle"]

birlesmis_indeks = list(zip(ilk_indeks,ic_indeks))
birlesmis_indeks = pd.MultiIndex.from_tuples(birlesmis_indeks)
print(birlesmis_indeks)

cizgifilmlistesi = [[40,"A"],[30,"B"],[10,"C"],[11,"E"],[11,"F"],[12,"G"]]
cizgifilmnpdizisi = np.array(cizgifilmlistesi)

cizgifilmdataframe = pd.DataFrame(cizgifilmnpdizisi,
                                  index=birlesmis_indeks,
                                  columns=["Yaş","Meslek"])


print(cizgifilmdataframe.loc["Simpson"])
print(cizgifilmdataframe.loc["Simpson"].loc["Homer"]) # Homer'a ait bilgileri getirir

cizgifilmdataframe.index.names = ["Film adı","İsim"]  # indekslere isim atar
print(cizgifilmdataframe)
