import csv
donnees = []
with open('effet_de_serre.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        donnees.append(row)


valeurs2014=[]
valeurs2024=[]

for i in range(1, len(donnees)):
    types=donnees[i][1]
    dates = donnees[i][0]
    if types== "Emission de gaz à effet de serre":
        valeur= float(donnees[i][2].replace(",", "."))
        
        if "2014" in dates:
            valeurs2014.append(valeur)
            print(valeur)
        elif "2024" in dates:
            valeurs2024.append(valeur)
            print(valeur)
            
 
from matplotlib import pyplot as plt
import numpy as np
noms_mois = ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Août", "Sep", "Oct", "Nov", "Dec"]
x = np.arange(len(noms_mois)) 
largeur = 0.35 

plt.bar(x - largeur/2, valeurs2014, largeur, label='2014')
plt.bar(x + largeur/2, valeurs2024, largeur, label='2024')

plt.title("Comparaison de l'intensité carbone : 2014 vs 2024")
plt.ylabel("gCO₂/kWh")
plt.xlabel("Mois")
plt.xticks(x, noms_mois)
plt.legend() 
plt.show()


Charbon14=[]
Déchets14=[]
Fioul14=[]
Gaz14=[]

Charbon24=[]
Déchets24=[]
Fioul24=[]
Gaz24=[]
for i in range(1, len(donnees)):
    dates = donnees[i][0]
    types=donnees[i][1]
    valeur= float(donnees[i][2].replace(",", "."))
    
    if "2014" in dates:
        if "Gaz" in types:
            Gaz14.append(valeur)
        elif "Charbon" in types:
            Charbon14.append(valeur)
        elif "Fioul" in types:
            Fioul14.append(valeur)
        elif "Déchets" in types:
            Déchets14.append(valeur)
            
    if "2024" in dates:
        if "Gaz" in types:
            Gaz24.append(valeur)
        elif "Charbon" in types:
            Charbon24.append(valeur)
        elif "Fioul" in types:
            Fioul24.append(valeur)
        elif "Déchets" in types:
            Déchets24.append(valeur)
            
from matplotlib import pyplot as plt
import numpy as np

x= np.arange(len(Gaz14))
largeur= 0.35
plt.bar(x - largeur/2, Gaz14, largeur, label='Gaz')
plt.bar(x - largeur/2, Fioul14, largeur,bottom=Gaz14 ,label='Fioul')
plt.bar(x - largeur/2, Charbon14, largeur,bottom=Fioul14 ,label='Charbon')
plt.bar(x - largeur/2, Déchets14, largeur,bottom=Charbon14 ,label='Déchets')


plt.bar(x + largeur/2, Gaz24, largeur, label='Gaz')
plt.bar(x + largeur/2, Fioul24, largeur,bottom=Gaz24, label='Fioul')
plt.bar(x + largeur/2, Charbon24, largeur,bottom=Fioul24, label='Charbon')
plt.bar(x + largeur/2, Déchets24, largeur,bottom=Charbon24 ,label='Déchets')

noms_mois = ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Août", "Sep", "Oct", "Nov", "Dec"]
plt.title("Comparaison de l'intensité carbone : 2014 vs 2024")
plt.ylabel("gCO₂/kWh")
plt.xlabel("Mois")
plt.xticks(x, noms_mois)
plt.legend() 
plt.show()





