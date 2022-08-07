# PogodaTorun
Projekt zaliczeniowy Data Mining - 2022r.

## Cel
Projekt ten realizuje zagadnienie przewidywania i analizy pogody na podstawie danych meteorologicznych dla Torunia.
Ma przedstawić zmienność średniej minimalnej i maksymalnej temperatury danego roku w danym miesiącu, na podstawie której
można wyciągnąć wnioski odnoszące się np. do prawdziwości twierdzenia o tym czy postępuje globalne ocieplenie.

## Analiza średniej temperatury każdego miesiąca

```
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Zaimportowanie danych jako DataFrame
df = pd.read_csv("./meteo.csv")

#Tablica w ktorej beda dataFrame'y z kazdego miesiaca
dataFrames = []
#Tablica miesiecy do podpisania wykresow
months = ['Styczeń','Luty','Marzec','Kwiecień','Maj','Czerwiec','Lipiec','Sierpień','Wrzesień','Październik','Listopad','Grudzień']

for i in range(0,12):
    #Wyróżnienie tylko Toruńskiej stacji pogodowej w danym miesiącu
    dataFrames.append(df[(df["Nazwa stacji"]=="TORUŃ") & (df["Miesiąc"] == i+1)])
    #Wyznaczenie kolumny z datą jako głównego indeksu
    dataFrames[i] = dataFrames[i].set_index(dataFrames[i].date)
    #Wyciągniecie sredniej temp w kazdym roku
    dataFrames[i] = dataFrames[i].groupby(by=dataFrames[i]["Rok"]).mean()
    #Wyrysowanie wykresow
    dataFrames[i]["Maksymalna temperatura dobowa"]\
        .plot(xticks=dataFrames[i].index,fontsize=10,rot=90,title=months[i],xlabel="ROK",ylabel="TEMPERATURA",figsize=(10,7),label="Max")\
        .legend(loc='upper right')
    dataFrames[i]["Minimalna temperatura dobowa"]\
        .plot(xticks=dataFrames[i].index,fontsize=10,rot=90,title=months[i],xlabel="ROK",ylabel="TEMPERATURA",figsize=(10,7), label="Min")\
        .legend(loc='upper right')
    #Zapisanie figur w plikach png
    plt.savefig("Miesiac" + str(i+1) + ".png")
    #Wyczyszczenie po kazdym wyrysowaniu figury na dany miesiac zeby dane nie zbieraly sie tylko na 1 rysunku
    plt.clf()
 ```

| ![Miesiac1](https://user-images.githubusercontent.com/72518873/183078651-cf9d4887-314f-4c27-bddf-f2ef1fa45196.png) | ![Miesiac2](https://user-images.githubusercontent.com/72518873/183078658-451fa31e-9a08-4d98-b611-03ea41b0a55f.png) | 
| :---:          |     :---:      |    
| ![Miesiac3](https://user-images.githubusercontent.com/72518873/183078660-459b42ba-c170-4cec-bf64-6f54020115d6.png)   | ![Miesiac4](https://user-images.githubusercontent.com/72518873/183078662-f09a2f92-76bc-4871-a385-ef7f4fc2b433.png)     | 
| ![Miesiac5](https://user-images.githubusercontent.com/72518873/183078663-1f9ee6c2-94f2-409c-9a2b-82f42e25866d.png)     | ![Miesiac6](https://user-images.githubusercontent.com/72518873/183078665-72896d7b-eaaa-4ce7-906c-ad61a2fbdc92.png)      | 
| ![Miesiac7](https://user-images.githubusercontent.com/72518873/183078668-460b9702-b6b3-4c8c-8008-ec15b731346f.png) | ![Miesiac8](https://user-images.githubusercontent.com/72518873/183078669-cc2c4b25-2120-4f51-8043-d615ea65dab6.png)| 
| ![Miesiac9](https://user-images.githubusercontent.com/72518873/183078671-b5b87655-c1a4-49e6-9c55-9149687eab18.png)| ![Miesiac10](https://user-images.githubusercontent.com/72518873/183078672-01d64554-2eaf-48c0-b6ac-0e10b0b95392.png)     | 
| ![Miesiac11](https://user-images.githubusercontent.com/72518873/183078675-1d17d60f-85de-43d1-bbe8-233717faf291.png) | ![Miesiac12](https://user-images.githubusercontent.com/72518873/183078678-b7fee4d9-72ff-411b-9ab5-c3b13a8967cb.png)| 

## Prognoza na kolejne 5 lat przy użyciu Neural Prophet

Czym jest Neural Prophet?
Jest to framework , który łączy tradycyjne modele szeregów czasowych z metodami głębokiego uczenia.

Poniższy wykres prezentuje przykładowe dane z paru lat,na których został wytrenowany model.

![image](https://user-images.githubusercontent.com/72518873/183305780-23dd0608-b9c1-4d0c-8fd5-ae1f50916cc4.png)

Na pierwszy rzut oka widać,że temperatura ma tendencje rosnącą.

## Wyniki prognozy

![image](https://user-images.githubusercontent.com/72518873/183305949-e513d3d6-badf-4245-b7ac-01b696f0b076.png)
![image](https://user-images.githubusercontent.com/72518873/183305840-c807097e-9ab8-47ea-972a-7d57c486d2a5.png)

Można zauważyć po analizie systematyczny wzrost temperatury w przyszłych latach.

## Wnioski
















