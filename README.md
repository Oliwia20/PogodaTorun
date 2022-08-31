# PogodaTorun
Projekt zaliczeniowy Data Mining - 2022r.

## Cel
Projekt ten realizuje zagadnienie przewidywania i analizy pogody na podstawie danych meteorologicznych dla Torunia.
Ma przedstawić zmienność średniej temperatury danego roku, na podstawie której
można wyciągnąć wnioski odnoszące się np. do prawdziwości twierdzenia o postępowaniu globalnego ocieplenia

## Analiza średniej temperatury każdego miesiąca

| ![Miesiac1](https://user-images.githubusercontent.com/72518873/187720449-e6393c7a-b361-4340-92aa-5d08afe75896.png) | ![Miesiac2](https://user-images.githubusercontent.com/72518873/187720452-bedd4c6c-4f02-45dc-840d-a0dc77db9fe5.png) | 
| :---:          |     :---:      |    
| ![Miesiac3](https://user-images.githubusercontent.com/72518873/187720454-221a25a7-830d-47fd-a730-96c7015f13aa.png)   | ![Miesiac4](https://user-images.githubusercontent.com/72518873/187720459-12c74d38-3f88-415b-8524-53acf7951d3d.png)     | 
| ![Miesiac5](https://user-images.githubusercontent.com/72518873/187720460-9739cc73-e6c8-42b8-aa06-6bf54deba0a8.png)     | ![Miesiac6](https://user-images.githubusercontent.com/72518873/187720462-678e1345-6d15-4e4c-b09c-f7459db265de.png)      | 
| ![Miesiac7](https://user-images.githubusercontent.com/72518873/187720464-5dca3890-f34d-4408-bcc9-61105090d565.png) | ![Miesiac8](https://user-images.githubusercontent.com/72518873/187720466-59852668-54c9-474c-955b-ce7dd200f8fb.png)| 
| ![Miesiac9](https://user-images.githubusercontent.com/72518873/187720468-51360d41-176f-4c16-a418-fcf5c12b2ff8.png)| ![Miesiac10](https://user-images.githubusercontent.com/72518873/187720443-a1f1d324-6011-4f93-8e86-466be1f703cf.png)     | 
| ![Miesiac11](https://user-images.githubusercontent.com/72518873/187720447-609f8c35-9f4d-4c65-a813-c13cba1b97cf.png) | ![Miesiac12](https://user-images.githubusercontent.com/72518873/187720448-a78e91bc-f71c-4c04-8bec-579ef8faa065.png)| 


## Prognoza na kolejne 5 lat przy użyciu regresji liniowej

| ![MiesiacV2_reg1](https://user-images.githubusercontent.com/72518873/187721208-60ce287a-5474-4a0b-9372-8d0b329989ce.png) | ![MiesiacV2_reg2](https://user-images.githubusercontent.com/72518873/187721210-637d511b-30e1-4835-890d-c129886d9128.png) | 
| :---:          |     :---:      |    
| ![MiesiacV2_reg3](https://user-images.githubusercontent.com/72518873/187721212-3038477e-ecb9-49b9-8de3-8243c68b2be1.png)   | ![MiesiacV2_reg4](https://user-images.githubusercontent.com/72518873/187721216-3b73ccb6-16dc-482b-8e85-0c5d6e552f06.png)     | 
| ![MiesiacV2_reg5](https://user-images.githubusercontent.com/72518873/187721218-9636f42f-b1b8-4673-b38e-b9e6b9a08979.png)     | ![MiesiacV2_reg6](https://user-images.githubusercontent.com/72518873/187721221-c3cdb780-bb30-4428-93cb-36ecca2e3234.png)      | 
| ![MiesiacV2_reg7](https://user-images.githubusercontent.com/72518873/187721225-1120cbac-c325-42d9-8b2a-8b274f534489.png) | ![MiesiacV2_reg8](https://user-images.githubusercontent.com/72518873/187721228-cc953a64-e808-4039-9f21-f08334d9fcf1.png)| 
| ![MiesiacV2_reg9](https://user-images.githubusercontent.com/72518873/187721232-bdca4c2c-5d9c-43e9-9448-9848ef9455cf.png)| ![MiesiacV2_reg10](https://user-images.githubusercontent.com/72518873/187721236-c6563845-7c6c-4964-9362-e292c55d0b15.png)     | 
| ![MiesiacV2_reg11](https://user-images.githubusercontent.com/72518873/187721237-3e81f69a-ab51-4079-990e-0c801268f598.png) | ![MiesiacV2_reg12](https://user-images.githubusercontent.com/72518873/187721240-c607da83-e13c-4bc9-b827-6209a1174d92.png)| 

Według osiągnietych wyników w czerwcu i listopadzie będziemy mogli zauważyć najbardziej drastyczny skok temperatur.

Z drugiej strony spodziewalibyśmy się wzrostu temperatury w najcieplejszych miesiącach roku,
natomiast funkcja na wykresie wyraźnie zdaje się temu zaprzeczać.
By przeanalizować jeszcze raz zebrane dane ze stacji meteorologicznych
posłużyłam się frameworkiem NeuralProphet.

## Prognoza na kolejne 5 lat przy użyciu Neural Prophet

Czym jest Neural Prophet?
Jest to framework , który łączy tradycyjne modele szeregów czasowych z metodami głębokiego uczenia.

Poniższy wykres prezentuje przykładowe dane z paru lat,na których został wytrenowany model.

![image](https://user-images.githubusercontent.com/72518873/183305780-23dd0608-b9c1-4d0c-8fd5-ae1f50916cc4.png)

Na pierwszy rzut oka widać,że temperatura z roku na rok rośnie.

## Wyniki prognozy

![image](https://user-images.githubusercontent.com/72518873/183305949-e513d3d6-badf-4245-b7ac-01b696f0b076.png)
![image](https://user-images.githubusercontent.com/72518873/183305840-c807097e-9ab8-47ea-972a-7d57c486d2a5.png)

Można zauważyć po analizie systematyczny wzrost temperatury w przyszłych latach.
