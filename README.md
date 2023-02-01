# olivier

## SmartGrid:

In deze case moeten voor elk district alle 150 huizen aan een van de 5 beschikbare batterijen worden gekoppeld door middel van het leggen van kabels. De capaciteit van de batterij mag niet overschreden worden door de output van de huizen die eraan verbonden zijn. Daarnaast is het de bedoeling de kosten zo laag mogelijk te houden. Elke batterij kost 5000 en elk kabelsegment kost 9.

## Algoritmes
### Connecties
Om de huizen aan de batterijen te verbinden zijn de volgende algoritmen geschreven:
1. Random:
Dit algoritme verbindt alle huizen aan een willekeurige batterij.

2. Greedy:
Dit algoritme verbindt de huizen aan de dichtst bijzijnde batterij.

3. Hill Climber:
Dit algoritme krijgt een gevulde smartgrid met alle huizen al verbonden aan een batterij, en wisselt willekeurig twee huizen om met als doel het verlagen van de kosten.

4. Simulated Annealing:
Dit algoritme maakt gebruik van de hill climber en wisselt ook telkens willekeurig twee huizen. Echter, dor gebruik te maken van temperatuur kan dit algoritme fouten toelaten, met als doel uiteindelijk een lagere kost te bereiken.
---

Om de kabels tussen de huizen en de batterijen te leggen zijn de volgende algoritmes geschreven:
1. 90 degrees:
Dit algoritme verbindt de huizen met hun batterijen door eerst de afstand over de x-as te overbruggen, en daarna de afstand over de y-as.

2. Random Try:
Dit algoritme zet 1 willekeurige stap en berekent de nieuwe afstand tot de batterij. Indien de stap de kabel dichter bij de batterij heeft gebracht wordt de stap opgeslagen in de kabel lijst. Zo niet, wordt er een volgende willekeurige stap geprobeerd.

3. Search Cables:
Dit algoritme loopt de 4 mogelijke richtingen af waar het naartoe kan en kent vervolgens aan deze richtingen aan score toe. Op basis van de scores die de stappen krijgen zal er een keuze worden gemaakt. Indien er meerdere hoge zijn zal hieruit een willekeurige keuze worden gemaakt.  

4. Further Cables:
Dit algoritme is gebaseerd op het score systeem van Search Cables. Hierbij wordt echter ook gekeken naar een eventuele vervolg kabel die er ligt. Deze wordt dan ook meegenomen in de score. Deze score bestaat hier uit een optelling van de individuele toegekende scores van elke stap. Hierna wordt ook weer een willekeurige keuze gemaakt tussen stappen met dezelfde score.

5. Closest to others:
Dit algoritme genereert voor de eerste 5 huizen 10 kabels en kiest voor die huizen de beste kabel op basis van de afstand tot andere huizen. Vervolgens worden de rest van de huizen met batterijen verbonden op basis van het search cables algoritme.



## Gebruik
Om de resultaten te reproduceren moet 
```
python main.py
```
worden gerund, met daar achteraan een 1, 2 of 3, afhankelijk van welk district je wil gebruiken.
Er zullen dan een aantal vragen worden gesteld:
1. Op basis van welk algoritme wil je de connecties tussen huizen en batterijen maken?
De opties hiervoor zijn: random, greedy, hillclimber, simulated annealing

2. Op basis van welk algoritme wil je de kabels leggen?
De opties hiervoor zijn: 90 degrees, random try, search cables,  further cables, closest to others

3. Wil je de kosten delen?
Het antwoord moet hierop 'yes' zijn.

4. Wil je loopen?
Vul hier 1 in als je alleen een visualisatie wil en 1000 indien je de distributie van kosten wil zien in een histogram.

## Vereisten
Deze code is geschreven in python versie 3.9.13. In onze code maken we gebruik van de volgende libraries:
In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```

Of via conda:

```
conda install --file requirements.txt
```
## Overzicht
Hierbij een overzicht van de belangrijke mappen en hun inhoud:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de drie benodigde classes voor deze case
  - **/code/visualisation**: bevat de code voor de visualisatie
- **/data**: bevat de verschillende databestanden die nodig zijn om de graaf te vullen en te visualiseren
- **main_run.py** staat los in de map Olivier, en moet gerund worden voor het uitvoeren van het experiment.

## Auteurs
- Frédérique Mulder
- Lisa Overbosch
- Sam Eijpex
