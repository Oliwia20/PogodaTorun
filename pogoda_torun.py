# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 18:21:55 2022

@author: Oliwia
"""

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

