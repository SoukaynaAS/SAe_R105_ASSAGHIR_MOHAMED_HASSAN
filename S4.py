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


Gaz14 = np.array(Gaz14); Fioul14 = np.array(Fioul14)
Déchets14 = np.array(Déchets14); Charbon14 = np.array(Charbon14)

Gaz24 = np.array(Gaz24); Fioul24 = np.array(Fioul24)
Déchets24 = np.array(Déchets24); Charbon24 = np.array(Charbon24)

x = np.arange(len(Gaz14))
largeur = 0.35 


c_gaz = '#FF0000'      
c_fioul = '#705090'    
c_déchets = '#60C0E0'  
c_charbon = '#8B7355' 



plt.bar(x - largeur/1.8, Gaz14, largeur, color=c_gaz, label='Gaz')
plt.bar(x - largeur/1.8, Fioul14, largeur, bottom=Gaz14, color=c_fioul, label='Fioul')
plt.bar(x - largeur/1.8, Déchets14, largeur, bottom=Gaz14+Fioul14, color=c_déchets, label='Déchets ménagers')
plt.bar(x - largeur/1.8, Charbon14, largeur, bottom=Gaz14+Fioul14+Déchets14, color=c_charbon, label='Charbon')


plt.bar(x + largeur/1.8, Gaz24, largeur, color=c_gaz)
plt.bar(x + largeur/1.8, Fioul24, largeur, bottom=Gaz24, color=c_fioul)
plt.bar(x + largeur/1.8, Déchets24, largeur, bottom=Gaz24+Fioul24, color=c_déchets)
plt.bar(x + largeur/1.8, Charbon24, largeur, bottom=Gaz24+Fioul24+Déchets24, color=c_charbon)



noms_mois = ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Août", "Sep", "Oct", "Nov", "Déc"]

plt.title("Émissions de gaz à effet de serre liées à la production d'électricité")
plt.ylabel("Millions de tonnes (Mt)")
plt.xlabel("Mois")
plt.xticks(x, noms_mois)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()





