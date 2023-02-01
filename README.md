# olivier

# SmartGrid:

In deze case moeten voor elk district alle 150 huizen aan een van de 5 beschikbare batterijen worden gekoppeld door middel van het leggen van kabels. De capaciteit van de batterij mag niet overschreden worden door de output van de huizen die eraan verbonden zijn. Daarnaast is het de bedoeling de kosten zo laag mogelijk te houden. Elke batterij kost 5000 en elk kabelsegment kost 9.

# Gebruik
<<<<<<< HEAD
Om de resultaten te reproduceren moet python main_opgeschoond.py worden gerund,
met daar achteraan een 1, 2 of 3, afhankelijk van welk district je wil gebruiken.
Er zullen dan een aantal vragen worden gesteld:
1, op basis van welk algoritme wil je de connecties tussen huizen en batterijen maken?
hier kun je invullen: random,


#Main_run.py
=======
Om de resultaten te reproduceren moet python main_run.py worden gerund, met daar achteraan een 1, 2 of 3, afhankelijk van welk district je wil gebruiken.
Er zullen dan een aantal vragen worden gesteld:
1. Op basis van welk algoritme wil je de connecties tussen huizen en batterijen maken?
De opties hiervoor zijn: random, greedy, hillclimber, simulated annealing

2. Op basis van welk algoritme wil je de kabels leggen?
De opties hiervoor zijn: 90 degrees, random try, search cables,  further cables, breadth first

3. Wil je de kosten delen?
Het antwoord moet hierop 'yes' zijn.

4. Wil je loopen?
Vul hier 1 in als je alleen een visualisatie wil en 1000 indien je de distributie van kosten wil zien in een histogram.

# Vereisten
Deze code is geschreven in python versie 3.9.13. In onze code maken we gebruik van de volgende libraries:
matplotlib.pyplot 3.5.3
seaborn 0.12.0
json5 0.9.10

# Overzicht
Hierbij een overzicht van de belangrijke mappen en hun inhoud:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de drie benodigde classes voor deze case
  - **/code/visualisation**: bevat de code voor de visualisatie
- **/data**: bevat de verschillende databestanden die nodig zijn om de graaf te vullen en te visualiseren
- **main_run.py** staat los in de map Olivier, en moet gerund worden voor het uitvoeren van het experiment.

# Auteurs
- Frédérique Mulder
- Lisa Overbosch
- Sam Eijpex
>>>>>>> 397d4330c14f27178798b6bc696015ce5930ac1c
