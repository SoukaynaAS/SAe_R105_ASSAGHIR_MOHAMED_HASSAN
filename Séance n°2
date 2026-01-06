import csv
donnees=[]
with open('effet_de_serre.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        donnees.append(row)


moyenne=[]
somme=0
nb=0
for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2017":
        valeur=donnees[i][1]
        if valeur== "Gaz":
           somme+=float(donnees[i][2].replace(",", "."))
           nb+=1
           moyenne_gaz=somme/nb        
print("Moyenne_gaz =", moyenne_gaz)
moyenne.append(moyenne_gaz)


somme=0
nb=0
for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2017":
        valeur=donnees[i][1]
        if valeur== "Fioul":
           somme+=float(donnees[i][2].replace(",", "."))
           nb+=1
           moyenne_fioul=somme/nb         
print("Moyenne_fioul =", moyenne_fioul)
moyenne.append(moyenne_fioul)


somme=0
nb=0
for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2017":
        valeur=donnees[i][1]
        if valeur== "Charbon":
           somme+=float(donnees[i][2].replace(",", "."))
           nb+=1
           moyenne_charbon=somme/nb        
print("Moyenne_charbon =", moyenne_charbon)
moyenne.append(moyenne_charbon)


somme=0
nb=0
for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2017":
        valeur=donnees[i][1]
        if valeur== "Déchets ménagers":
           somme+=float(donnees[i][2].replace(",", "."))
           nb+=1
           moyenne_déchets=somme/nb          
print("Moyenne_déchets =", moyenne_déchets)
moyenne.append(moyenne_déchets)


moyenne2=[]
somme=0
nb=0
for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2025":
        valeur=donnees[i][1]
        if valeur== "Gaz":
           somme+=float(donnees[i][2].replace(",", "."))
           nb+=1
           moyenne_gaz=somme/nb        
print("Moyenne_gaz =", moyenne_gaz)
moyenne2.append(moyenne_gaz)


somme=0
nb=0
for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2025":
        valeur=donnees[i][1]
        if valeur== "Fioul":
           somme+=float(donnees[i][2].replace(",", "."))
           nb+=1
           moyenne_fioul=somme/nb         
print("Moyenne_fioul =", moyenne_fioul)
moyenne2.append(moyenne_fioul)


somme=0
nb=0
for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2025":
        valeur=donnees[i][1]
        if valeur== "Charbon":
           somme+=float(donnees[i][2].replace(",", "."))
           nb+=1
           moyenne_charbon=somme/nb        
print("Moyenne_charbon =", moyenne_charbon)
moyenne2.append(moyenne_charbon)


somme=0
nb=0
for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2025":
        valeur=donnees[i][1]
        if valeur== "Déchets ménagers":
           somme+=float(donnees[i][2].replace(",", "."))
           nb+=1
           moyenne_déchets=somme/nb          
print("Moyenne_déchets =", moyenne_déchets)
moyenne2.append(moyenne_déchets)

from matplotlib import pyplot as plt
import numpy as np

categories = ["Gaz", "Fioul", "Charbon", "Déchets ménagers"]
x = np.arange(len(categories))  
largeur = 0.35                 

plt.bar(x - largeur/2, moyenne, largeur, label='2017')
plt.bar(x + largeur/2, moyenne2, largeur, label='2025')

plt.title("Évolution des émissions de GES par source d’énergie (2017 vs 2025)")
plt.xlabel("Source d'énergies")
plt.ylabel("Émissions de GES (MtCO₂)")
plt.xticks(x, categories) 
plt.legend()             
plt.show()
