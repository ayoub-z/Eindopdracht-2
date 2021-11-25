# Eindopdracht 2: Toepassingsopdracht DES

We hebben een vending machine gesimulieert waarbij een que mensen tegelijkertijd naartoe gaan in 1 dag. <br/>
Het aantal mensen is random tussen de 0 en 50 personen iedere dag.<br/>
Iedere persoon komt met een bepaald bedrag (tussen €2 en €10) en met een keuze van het aantal producten dat hij/zij wilt (tussen 1 en 3).<br/>

Aan het begin geef je een input mee van het aantal dagen dat gesimuleert wordt. 
De vending machine volgt dan deze stappen:
  - Stap 1: Er komt een deposit binnen en dit wordt bijgehouden.
  - Stap 2: Producten worden gekozen. Als de deposit voldoende is, worden de producten afgegeven.
  - Stap 3: De deposit verlaagt met het respectievelijk bedrag.
  - Stap 4: Returneer de change als deze er is.

De voorraad van ieder product is 50 en na iedere aankoop verlaagt de voorraad van dat product met 1.
Aan het eind van de gesimuleerde dag wordt de voorraad helemaal bijgevuld door een medewerker.


## **DES design**: 
![](https://github.com/ayoub-z/Eindopdracht-2/blob/main/DES_design.png).

## **Automaton**: 
![](https://github.com/ayoub-z/Eindopdracht-2/blob/main/Automaton.png).



