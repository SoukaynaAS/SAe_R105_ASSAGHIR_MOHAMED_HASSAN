import csv

donnees=[]
with open('donnees_global.csv',newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter=';')
	for row in reader:
		donnees.append(row)
#print(donnees)

mt=[]
for i in range(1,len(donnees)):
	mt.append(donnees[i][2])
#print(mt)

annees=[]
moyennes=[]
somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2014" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2014 = (somme/nb)*12
annees.append(2014)
moyennes.append(moyenne_2014)
print("Moyenne 2014 =", moyenne_2014)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2015" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2015=(somme/nb)*12
annees.append(2015)
moyennes.append(moyenne_2015)
#print("Moyenne 2015 =", moyenne_2015)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2016" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2016=(somme/nb)*12
annees.append(2016)
moyennes.append(moyenne_2016)
#print("Moyenne 2016 =", moyenne_2016)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2017" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2017=(somme/nb)*12
annees.append(2017)
moyennes.append(moyenne_2017)
#print("Moyenne 2017 =", moyenne_2017)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2018" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2018=(somme/nb)*12
annees.append(2018)
moyennes.append(moyenne_2018)
#print("Moyenne 2018 =", moyenne_2018)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2019" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2019=(somme/nb)*12
annees.append(2019)
moyennes.append(moyenne_2019)
#print("Moyenne 2019 =", moyenne_2019)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2020" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2020=(somme/nb)*12
annees.append(2020)
moyennes.append(moyenne_2020)
#print("Moyenne 2020 =", moyenne_2020)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2021" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2021=(somme/nb)*12
annees.append(2021)
moyennes.append(moyenne_2021)
#print("Moyenne 2021 =", moyenne_2021)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2022" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2022=(somme/nb)*12
annees.append(2022)
moyennes.append(moyenne_2022)
#print("Moyenne 2022 =", moyenne_2022)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2023" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2023=(somme/nb)*12
annees.append(2023)
moyennes.append(moyenne_2023)
#print("Moyenne 2023 =", moyenne_2023)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2024" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2024=(somme/nb)*12
annees.append(2024)
moyennes.append(moyenne_2024)
#print("Moyenne 2024 =", moyenne_2024)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2025" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2025=(somme/nb)*12
annees.append(2025)
moyennes.append(moyenne_2025)
#print("Moyenne 2025 =", moyenne_2025)

from matplotlib import pyplot as plt

plt.plot(annees, moyennes, marker="o")
plt.ylabel("Million de tonnes (Mt)")
plt.xlabel("Année")
plt.title("Évolution des émissions des gaz à effet de serre liées à la production d'électricité")
plt.xticks(annees)
plt.show()
		
donnees=[]
with open('donnees_global.csv',newline='', encoding="utf-8") as csvfile:
	reader=csv.reader(csvfile,delimiter=';')
	for row in reader:
		donnees.append(row)
#print(donnees)

annees1=[]
charbon=[]
dechets=[]
fioul=[]
gaz=[]

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2014" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2014=(somme/nb)*12
annees1.append(2014)
charbon.append(charbon_2014)
#print("Production 2014 GSE charbon  =", charbon_2014)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2014" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2014=(somme/nb)*12
dechets.append(dechets_2014)
#print("Production 2014 GSE déchets  =", dechets_2014)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2014" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2014=(somme/nb)*12
fioul.append(fioul_2014)
#print("Production 2014 GSE fioul  =", fioul_2014)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2014" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2014=(somme/nb)*12
gaz.append(gaz_2014)
#print("Production 2014 GSE gaz  =", gaz_2014)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2015" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2015=(somme/nb)*12
annees1.append(2015)
charbon.append(charbon_2015)
#print("Production 2015 GSE charbon  =", charbon_2015)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2015" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2015=(somme/nb)*12
dechets.append(dechets_2015)
#print("Production 2015 GSE déchets  =", dechets_2015)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2015" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2015=(somme/nb)*12
fioul.append(fioul_2015)
#print("Production 2015 GSE fioul  =", fioul_2015)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2015" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2015=(somme/nb)*12
gaz.append(gaz_2015)
#print("Production 2015 GSE gaz  =", gaz_2015)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2016" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2016=(somme/nb)*12
annees1.append(2016)
charbon.append(charbon_2016)
#print("Production 2016 GSE charbon  =", charbon_2016)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2016" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2016=(somme/nb)*12
dechets.append(dechets_2016)
#print("Production 2016 GSE déchets  =", dechets_2016)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2016" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2016=(somme/nb)*12
fioul.append(fioul_2016)
#print("Production 2016 GSE fioul  =", fioul_2016)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2016" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2016=(somme/nb)*12
gaz.append(gaz_2016)
#print("Production 2016 GSE gaz  =", gaz_2016)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2017" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2017=(somme/nb)*12
annees1.append(2017)
charbon.append(charbon_2017)
#print("Production 2017 GSE charbon  =", charbon_2017)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2017" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2017=(somme/nb)*12
dechets.append(dechets_2017)
#print("Production 2017 GSE déchets  =", dechets_2017)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2017" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2017=(somme/nb)*12
fioul.append(fioul_2017)
#print("Production 2017 GSE fioul  =", fioul_2017)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2017" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2017=(somme/nb)*12
gaz.append(gaz_2017)
#print("Production 2017 GSE gaz  =", gaz_2017)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2018" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2018=(somme/nb)*12
annees1.append(2018)
charbon.append(charbon_2018)
#print("Production 2018 GSE charbon  =", charbon_2018)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2018" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2018=(somme/nb)*12
dechets.append(dechets_2018)
#print("Production 2018 GSE déchets  =", dechets_2018)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2018" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2018=(somme/nb)*12
fioul.append(fioul_2018)
#print("Production 2018 GSE fioul  =", fioul_2018)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2018" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2018=(somme/nb)*12
gaz.append(gaz_2018)
#print("Production 2018 GSE gaz  =", gaz_2018)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2019" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2019=(somme/nb)*12
annees1.append(2019)
charbon.append(charbon_2019)
#print("Production 2019 GSE charbon  =", charbon_2019)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2019" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2019=(somme/nb)*12
dechets.append(dechets_2019)
#print("Production 2019 GSE déchets  =", dechets_2019)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2019" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2019=(somme/nb)*12
fioul.append(fioul_2019)
#print("Production 2019 GSE fioul  =", fioul_2019)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2019" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2019=(somme/nb)*12
gaz.append(gaz_2019)
#print("Production 2019 GSE gaz  =", gaz_2019)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2020" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2020=(somme/nb)*12
annees1.append(2020)
charbon.append(charbon_2020)
#print("Production 2020 GSE charbon  =", charbon_2020)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2020" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2020=(somme/nb)*12
dechets.append(dechets_2020)
#print("Production 2020 GSE déchets  =", dechets_2020)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2020" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2020=(somme/nb)*12
fioul.append(fioul_2020)
#print("Production 2020 GSE fioul  =", fioul_2020)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2020" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2020=(somme/nb)*12
gaz.append(gaz_2020)
#print("Production 2020 GSE gaz  =", gaz_2020)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2021" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2021=(somme/nb)*12
annees1.append(2021)
charbon.append(charbon_2021)
#print("Production 2021 GSE charbon  =", charbon_2021)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2021" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2021=(somme/nb)*12
dechets.append(dechets_2021)
#print("Production 2021 GSE déchets  =", dechets_2021)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2021" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2021=(somme/nb)*12
fioul.append(fioul_2021)
#print("Production 2021 GSE fioul  =", fioul_2021)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2021" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2021=(somme/nb)*12
gaz.append(gaz_2021)
#print("Production 2021 GSE gaz  =", gaz_2021)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2022" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2022=(somme/nb)*12
annees1.append(2022)
charbon.append(charbon_2022)
#print("Production 2022 GSE charbon  =", charbon_2022)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2022" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2022=(somme/nb)*12
dechets.append(dechets_2022)
#print("Production 2022 GSE déchets  =", dechets_2022)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2022" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2022=(somme/nb)*12
fioul.append(fioul_2022)
#print("Production 2022 GSE fioul  =", fioul_2022)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2022" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2022=(somme/nb)*12
gaz.append(gaz_2022)
#print("Production 2022 GSE gaz  =", gaz_2022)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2023" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2023=(somme/nb)*12
annees1.append(2023)
charbon.append(charbon_2023)
#print("Production 2023 GSE charbon  =", charbon_2023)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2023" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2023=(somme/nb)*12
dechets.append(dechets_2023)
#print("Production 2023 GSE déchets  =", dechets_2023)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2023" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2023=(somme/nb)*12
fioul.append(fioul_2023)
#print("Production 2023 GSE fioul  =", fioul_2023)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2023" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2023=(somme/nb)*12
gaz.append(gaz_2023)
#print("Production 2023 GSE gaz  =", gaz_2023)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2024" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2024=(somme/nb)*12
annees1.append(2024)
charbon.append(charbon_2024)
#print("Production 2024 GSE charbon  =", charbon_2024)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2024" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2024=(somme/nb)*12
dechets.append(dechets_2024)
#print("Production 2024 GSE déchets  =", dechets_2024)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2024" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2024=(somme/nb)*12
fioul.append(fioul_2024)
#print("Production 2024 GSE fioul  =", fioul_2024)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2024" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2024=(somme/nb)*12
gaz.append(gaz_2024)
#print("Production 2024 GSE gaz  =", gaz_2024)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2025" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2025=(somme/nb)*12
annees1.append(2025)
charbon.append(charbon_2025)
#print("Production 2025 GSE charbon  =", charbon_2025)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2025" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2025=(somme/nb)*12
dechets.append(dechets_2025)
#print("Production 2025 GSE déchets  =", dechets_2025)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2025" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2025=(somme/nb)*12
fioul.append(fioul_2025)
#print("Production 2025 GSE fioul  =", fioul_2025)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2025" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2025=(somme/nb)*12
gaz.append(gaz_2025)
#print("Production 2025 GSE gaz  =", gaz_2025)

from matplotlib import pyplot as plt

plt.plot(annees, gaz, marker="o", label="Gaz")
plt.plot(annees, fioul, marker="o", label="Fioul")
plt.plot(annees, dechets, marker="o", label="Déchets")
plt.plot(annees, charbon, marker="o", label="Charbon")

plt.ylabel("MtCO2e (Mt)")
plt.xlabel("Année")
plt.title("Émissions de GES liées à la production d’électricité")
plt.legend()
plt.xticks(annees)
plt.show()


donnees2=[]
with open('donnees_global_2.csv',newline='', encoding="utf-8") as csvfile:
	reader=csv.reader(csvfile,delimiter=';')
	for row in reader:
		donnees2.append(row)
#print(donnees2)

mt2=[]
for i in range(1,len(donnees2)):
	mt2.append(donnees2[i][2])
#print(mt2)

annees=[]
moyennes=[]
somme=0
nb=0

for i in range(1,len(donnees2)):
    if donnees2[i][0][:4]=="2017" and "Emission" in donnees[i][1]:
        valeur=donnees2[i][2]
        if valeur!= "":
            somme+=float(valeur.replace(",", "."))
            nb+=1
            moyenne_2017=(somme/nb)*12
annees.append(2017)
moyennes.append(moyenne_2017)
#print("Moyenne 2017 =", moyenne_2017)

somme=0
nb=0

for i in range(1,len(donnees2)):
    if donnees2[i][0][:4]=="2018" and "Emission" in donnees[i][1]:
        valeur=donnees2[i][2]
        if valeur!= "":
            somme+=float(valeur.replace(",", "."))
            nb+=1
            moyenne_2018=(somme/nb)*12
annees.append(2018)
moyennes.append(moyenne_2018)
#print("Moyenne 2018 =", moyenne_2018)

somme=0
nb=0

for i in range(1,len(donnees2)):
    if donnees2[i][0][:4]=="2019" and "Emission" in donnees[i][1]:
        valeur=donnees2[i][2]
        if valeur!= "":
            somme+=float(valeur.replace(",", "."))
            nb+=1
            moyenne_2019=(somme/nb)*12
annees.append(2019)
moyennes.append(moyenne_2019)
#print("Moyenne 2019 =", moyenne_2019)

somme=0
nb=0

for i in range(1,len(donnees2)):
    if donnees2[i][0][:4]=="2020" and "Emission" in donnees[i][1]:
        valeur=donnees2[i][2]
        if valeur!= "":
            somme+=float(valeur.replace(",", "."))
            nb+=1
            moyenne_2020=(somme/nb)*12
annees.append(2020)
moyennes.append(moyenne_2020)
#print("Moyenne 2020 =", moyenne_2020)

somme=0
nb=0

for i in range(1,len(donnees2)):
    if donnees2[i][0][:4]=="2021" and "Emission" in donnees[i][1]:
        valeur=donnees2[i][2]
        if valeur!= "":
            somme+=float(valeur.replace(",", "."))
            nb+=1
            moyenne_2021=(somme/nb)*12
annees.append(2021)
moyennes.append(moyenne_2021)
#print("Moyenne 2021 =", moyenne_2021)

somme=0
nb=0

for i in range(1,len(donnees2)):
    if donnees2[i][0][:4]=="2022" and "Emission" in donnees[i][1]:
        valeur=donnees2[i][2]
        if valeur!= "":
            somme+=float(valeur.replace(",", "."))
            nb+=1
            moyenne_2022=(somme/nb)*12
annees.append(2022)
moyennes.append(moyenne_2022)
#print("Moyenne 2022 =", moyenne_2022)

somme=0
nb=0

for i in range(1,len(donnees2)):
    if donnees2[i][0][:4]=="2023" and "Emission" in donnees[i][1]:
        valeur=donnees2[i][2]
        if valeur!= "":
            somme+=float(valeur.replace(",", "."))
            nb+=1
            moyenne_2023=(somme/nb)*12
annees.append(2023)
moyennes.append(moyenne_2023)
#print("Moyenne 2023 =", moyenne_2023)

somme=0
nb=0

for i in range(1,len(donnees2)):
    if donnees2[i][0][:4]=="2024" and "Emission" in donnees[i][1]:
        valeur=donnees2[i][2]
        if valeur!= "":
            somme+=float(valeur.replace(",", "."))
            nb+=1
            moyenne_2024=(somme/nb)*12
annees.append(2024)
moyennes.append(moyenne_2024)
#print("Moyenne 2024 =", moyenne_2024)

somme=0
nb=0

for i in range(1,len(donnees2)):
    if donnees2[i][0][:4]=="2025" and "Emission" in donnees[i][1]:
        valeur=donnees2[i][2]
        if valeur!= "":
            somme+=float(valeur.replace(",", "."))
            nb+=1
            moyenne_2025=(somme/nb)*12
#print("Moyenne 2025 =", moyenne_2025)
annees.append(2025)
moyennes.append(moyenne_2025)

from matplotlib import pyplot as plt

plt.plot(annees, moyennes, marker="o")
plt.ylabel("Millions de tonnes (Mt)")
plt.xlabel("Année")
plt.title("Évolution des émissions des gaz à effet de serre liées à la consommation d'électricité")
plt.xticks(annees)
plt.show()


import csv

donnees=[]
with open('donnees_global.csv',newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter=';')
	for row in reader:
		donnees.append(row)
#print(donnees)

annees=[]
moyennes=[]
somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2014" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2014 = (somme/nb)*12
annees.append(2014)
moyennes.append(moyenne_2014)
#print("Moyenne 2014 =", moyenne_2014)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2015" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2015=(somme/nb)*12
annees.append(2015)
moyennes.append(moyenne_2015)
#print("Moyenne 2015 =", moyenne_2015)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2016" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2016=(somme/nb)*12
annees.append(2016)
moyennes.append(moyenne_2016)
#print("Moyenne 2016 =", moyenne_2016)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2017" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2017=(somme/nb)*12
annees.append(2017)
moyennes.append(moyenne_2017)
#print("Moyenne 2017 =", moyenne_2017)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2018" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2018=(somme/nb)*12
annees.append(2018)
moyennes.append(moyenne_2018)
#print("Moyenne 2018 =", moyenne_2018)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2019" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2019=(somme/nb)*12
annees.append(2019)
moyennes.append(moyenne_2019)
#print("Moyenne 2019 =", moyenne_2019)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2020" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2020=(somme/nb)*12
annees.append(2020)
moyennes.append(moyenne_2020)
#print("Moyenne 2020 =", moyenne_2020)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2021" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2021=(somme/nb)*12
annees.append(2021)
moyennes.append(moyenne_2021)
#print("Moyenne 2021 =", moyenne_2021)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2022" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2022=(somme/nb)*12
annees.append(2022)
moyennes.append(moyenne_2022)
#print("Moyenne 2022 =", moyenne_2022)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2023" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2023=(somme/nb)*12
annees.append(2023)
moyennes.append(moyenne_2023)
#print("Moyenne 2023 =", moyenne_2023)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2024" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2024=(somme/nb)*12
annees.append(2024)
moyennes.append(moyenne_2024)
#print("Moyenne 2024 =", moyenne_2024)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][:4]=="2025" and "Emission" in donnees[i][1]:
        somme+=float(donnees[i][2].replace(",", "."))
        nb+=1
moyenne_2025=(somme/nb)*12
annees.append(2025)
moyennes.append(moyenne_2025)
#print("Moyenne 2025 =", moyenne_2025)

from matplotlib import pyplot as plt

plt.bar(annees, moyennes)
plt.ylabel("Millions de tonnes (Mt)")
plt.xlabel("Année")
plt.title("Évolution des émissions des gaz à effet de serre liées à la production d'électricité")
plt.xticks(annees)
plt.show()


donnees=[]
with open('donnees_global.csv',newline='', encoding="utf-8") as csvfile:
	reader=csv.reader(csvfile,delimiter=';')
	for row in reader:
		donnees.append(row)
#print(donnees)

annees1=[]
charbon=[]
dechets=[]
fioul=[]
gaz=[]

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2014" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2014=(somme/nb)*12
annees1.append(2014)
charbon.append(charbon_2014)
print("Production 2014 GSE charbon  =", charbon_2014)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2014" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2014=(somme/nb)*12
dechets.append(dechets_2014)
print("Production 2014 GSE déchets  =", dechets_2014)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2014" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2014=(somme/nb)*12
fioul.append(fioul_2014)
print("Production 2014 GSE fioul  =", fioul_2014)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2014" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2014=(somme/nb)*12
gaz.append(gaz_2014)
print("Production 2014 GSE gaz  =", gaz_2014)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2015" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2015=(somme/nb)*12
annees1.append(2015)
charbon.append(charbon_2015)
print("Production 2015 GSE charbon  =", charbon_2015)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2015" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2015=(somme/nb)*12
dechets.append(dechets_2015)
print("Production 2015 GSE déchets  =", dechets_2015)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2015" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2015=(somme/nb)*12
fioul.append(fioul_2015)
print("Production 2015 GSE fioul  =", fioul_2015)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2015" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2015=(somme/nb)*12
gaz.append(gaz_2015)
print("Production 2015 GSE gaz  =", gaz_2015)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2016" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2016=(somme/nb)*12
annees1.append(2016)
charbon.append(charbon_2016)
print("Production 2016 GSE charbon  =", charbon_2016)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2016" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2016=(somme/nb)*12
dechets.append(dechets_2016)
print("Production 2016 GSE déchets  =", dechets_2016)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2016" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2016=(somme/nb)*12
fioul.append(fioul_2016)
print("Production 2016 GSE fioul  =", fioul_2016)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2016" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2016=(somme/nb)*12
gaz.append(gaz_2016)
print("Production 2016 GSE gaz  =", gaz_2016)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2017" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2017=(somme/nb)*12
annees1.append(2017)
charbon.append(charbon_2017)
print("Production 2017 GSE charbon  =", charbon_2017)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2017" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2017=(somme/nb)*12
dechets.append(dechets_2017)
print("Production 2017 GSE déchets  =", dechets_2017)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2017" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2017=(somme/nb)*12
fioul.append(fioul_2017)
print("Production 2017 GSE fioul  =", fioul_2017)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2017" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2017=(somme/nb)*12
gaz.append(gaz_2017)
print("Production 2017 GSE gaz  =", gaz_2017)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2018" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2018=(somme/nb)*12
annees1.append(2018)
charbon.append(charbon_2018)
print("Production 2018 GSE charbon  =", charbon_2018)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2018" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2018=(somme/nb)*12
dechets.append(dechets_2018)
print("Production 2018 GSE déchets  =", dechets_2018)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2018" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2018=(somme/nb)*12
fioul.append(fioul_2018)
print("Production 2018 GSE fioul  =", fioul_2018)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2018" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2018=(somme/nb)*12
gaz.append(gaz_2018)
print("Production 2018 GSE gaz  =", gaz_2018)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2019" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2019=(somme/nb)*12
annees1.append(2019)
charbon.append(charbon_2019)
print("Production 2019 GSE charbon  =", charbon_2019)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2019" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2019=(somme/nb)*12
dechets.append(dechets_2019)
print("Production 2019 GSE déchets  =", dechets_2019)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2019" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2019=(somme/nb)*12
fioul.append(fioul_2019)
print("Production 2019 GSE fioul  =", fioul_2019)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2019" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2019=(somme/nb)*12
gaz.append(gaz_2019)
print("Production 2019 GSE gaz  =", gaz_2019)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2020" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2020=(somme/nb)*12
annees1.append(2020)
charbon.append(charbon_2020)
print("Production 2020 GSE charbon  =", charbon_2020)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2020" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2020=(somme/nb)*12
dechets.append(dechets_2020)
print("Production 2020 GSE déchets  =", dechets_2020)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2020" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2020=(somme/nb)*12
fioul.append(fioul_2020)
print("Production 2020 GSE fioul  =", fioul_2020)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2020" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2020=(somme/nb)*12
gaz.append(gaz_2020)
print("Production 2020 GSE gaz  =", gaz_2020)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2021" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2021=(somme/nb)*12
annees1.append(2021)
charbon.append(charbon_2021)
print("Production 2021 GSE charbon  =", charbon_2021)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2021" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2021=(somme/nb)*12
dechets.append(dechets_2021)
print("Production 2021 GSE déchets  =", dechets_2021)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2021" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2021=(somme/nb)*12
fioul.append(fioul_2021)
print("Production 2021 GSE fioul  =", fioul_2021)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2021" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2021=(somme/nb)*12
gaz.append(gaz_2021)
print("Production 2021 GSE gaz  =", gaz_2021)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2022" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2022=(somme/nb)*12
annees1.append(2022)
charbon.append(charbon_2022)
print("Production 2022 GSE charbon  =", charbon_2022)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2022" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2022=(somme/nb)*12
dechets.append(dechets_2022)
print("Production 2022 GSE déchets  =", dechets_2022)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2022" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2022=(somme/nb)*12
fioul.append(fioul_2022)
print("Production 2022 GSE fioul  =", fioul_2022)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2022" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2022=(somme/nb)*12
gaz.append(gaz_2022)
print("Production 2022 GSE gaz  =", gaz_2022)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2023" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2023=(somme/nb)*12
annees1.append(2023)
charbon.append(charbon_2023)
print("Production 2023 GSE charbon  =", charbon_2023)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2023" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2023=(somme/nb)*12
dechets.append(dechets_2023)
print("Production 2023 GSE déchets  =", dechets_2023)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2023" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2023=(somme/nb)*12
fioul.append(fioul_2023)
print("Production 2023 GSE fioul  =", fioul_2023)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2023" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2023=(somme/nb)*12
gaz.append(gaz_2023)
print("Production 2023 GSE gaz  =", gaz_2023)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2024" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2024=(somme/nb)*12
annees1.append(2024)
charbon.append(charbon_2024)
print("Production 2024 GSE charbon  =", charbon_2024)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2024" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2024=(somme/nb)*12
dechets.append(dechets_2024)
print("Production 2024 GSE déchets  =", dechets_2024)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2024" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2024=(somme/nb)*12
fioul.append(fioul_2024)
print("Production 2024 GSE fioul  =", fioul_2024)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2024" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2024=(somme/nb)*12
gaz.append(gaz_2024)
print("Production 2024 GSE gaz  =", gaz_2024)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2025" and "Charbon" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
charbon_2025=(somme/nb)*12
annees1.append(2025)
charbon.append(charbon_2025)
print("Production 2025 GSE charbon  =", charbon_2025)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2025" and "Déchets" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
dechets_2025=(somme/nb)*12
dechets.append(dechets_2025)
print("Production 2025 GSE déchets  =", dechets_2025)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2025" and "Fioul" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
fioul_2025=(somme/nb)*12
fioul.append(fioul_2025)
print("Production 2025 GSE fioul  =", fioul_2025)

somme=0
nb=0

for i in range(1, len(donnees)):
    if donnees[i][0][:4]=="2025" and "Gaz" in donnees[i][1]:
        valeur=donnees[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
gaz_2025=(somme/nb)*12
gaz.append(gaz_2025)
print("Production 2025 GSE gaz  =", gaz_2025)

from matplotlib import pyplot as plt


plt.bar(annees1, gaz, color="red", label="Gaz")
plt.bar(annees1, fioul, bottom=gaz, color="purple", label="Fioul")
bottom=[gaz[i]+fioul[i] for i in range(len(annees1))]
plt.bar(annees1, dechets, bottom=bottom, color="blue", label="Déchets")
bottom=[bottom[i]+dechets[i] for i in range(len(annees1))]
plt.bar(annees1, charbon, bottom=bottom, color="green", label="Charbon")
plt.ylabel("MtCO2e (Mt)")
plt.xlabel("Année")
plt.title("Émissions de GES liées à la production d’électricité")
plt.legend(["Gaz", "Fioul", "Déchets ménagers", "Charbon"])
plt.xticks(annees1)
plt.show()



donnees2=[]
with open('donnees_global_2.csv',newline='', encoding="utf-8") as csvfile:
	reader=csv.reader(csvfile,delimiter=';')
	for row in reader:
		donnees2.append(row)
#print(donnees2)

annees2=[]
production=[]
importations=[]

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4] == "2017" and "production" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur = donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production_2017=(somme/nb)*12
annees2.append(2017)
production.append(production_2017)
print("Production 2017 émission cycle de vie =", production_2017)


somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2017" and "importations" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations_2017=(somme/nb)*12
importations.append(importations_2017)
print("Importation 2017 émission cycle de vie =", importations_2017)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2018" and "production" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production_2018=(somme/nb)*12
annees2.append(2018)
production.append(production_2018)
print("Production 2018 émission =", production_2018)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2018" and "importations" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations_2018=(somme/nb)*12
importations.append(importations_2018)
print("Importation 2018 émission cycle de vie =", importations_2018)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2019" and "production" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production_2019=(somme/nb)*12
annees2.append(2019)
production.append(production_2019)
print("Production 2019 émission cycle de vie =", production_2019)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2019" and "importations" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations_2019=(somme/nb)*12
importations.append(importations_2019)
print("Importation 2019 émission cycle de vie =", importations_2019)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2020" and "production" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production_2020=(somme/nb)*12
annees2.append(2020)
production.append(production_2020)
print("Production 2020 émission cycle de vie =", production_2020)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2020" and "importations" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations_2020=(somme/nb)*12
importations.append(importations_2020)
print("Importation 2020 émission cycle de vie =", importations_2020)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2021" and "production" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production_2021=(somme/nb)*12
annees2.append(2021)
production.append(production_2021)
print("Production 2021 émission cycle de vie =", production_2021)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2021" and "importations" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations_2021=(somme/nb)*12
importations.append(importations_2021)
print("Importation 2021 émission cycle de vie =", importations_2021)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2022" and "production" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production_2022=(somme/nb)*12
annees2.append(2022)
production.append(production_2022)
print("Production 2022 émission cycle de vie =", production_2022)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2022" and "importations" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations_2022=(somme/nb)*12
importations.append(importations_2022)
print("Importation 2022 émission cycle de vie =", importations_2022)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2023" and "production" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production_2023=(somme/nb)*12
annees2.append(2023)
production.append(production_2023)
print("Production 2023 émission cycle de vie =", production_2023)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2023" and "importations" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations_2023=(somme/nb)*12
importations.append(importations_2023)
print("Importation 2023 émission cycle de vie =", importations_2023)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2024" and "production" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production_2024=(somme/nb)*12
annees2.append(2024)
production.append(production_2024)
print("Production 2024 émission cycle de vie =", production_2024)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2024" and "importations" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations_2024=(somme/nb)*12
importations.append(importations_2024)
print("Importation 2024 émission cycle de vie =", importations_2024)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2025" and "production" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production_2025=(somme/nb)*12
annees2.append(2025)
production.append(production_2025)
print("Production 2025 émission cycle de vie =", production_2025)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2025" and "importations" in donnees2[i][1] and "cycle" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations_2025=(somme/nb)*12
importations.append(importations_2025)
print("Importation 2025 émission cycle de vie =", importations_2025)

from matplotlib import pyplot as plt

plt.bar(annees2, importations, label="Importations")
plt.bar(annees2, production, bottom=importations, label="Production en France")

plt.ylabel("MtCO2e (Mt)")
plt.xlabel("Année")
plt.title("Émissions de GES liées à la consommation d'électricité (cycle de vie)")
plt.xticks(annees2)
plt.legend()
plt.show()






donnees2=[]
with open('donnees_global_2.csv',newline='', encoding="utf-8") as csvfile:
	reader=csv.reader(csvfile,delimiter=';')
	for row in reader:
		donnees2.append(row)
#print(donnees2)

annees3=[]
production2=[]
importations2=[]

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4] == "2017" and "production" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur = donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production2_2017=(somme/nb)*12
annees3.append(2017)
production2.append(production2_2017)
print("Production 2017 émission direct  =", production2_2017)


somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2017" and "importations" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations2_2017=(somme/nb)*12
importations2.append(importations2_2017)
print("Importation 2017 émission direct =", importations2_2017)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2018" and "production" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production2_2018=(somme/nb)*12
annees3.append(2018)
production2.append(production2_2018)
print("Production 2018 émission direct =", production2_2018)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2018" and "importations" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations2_2018=(somme/nb)*12
importations2.append(importations2_2018)
print("Importation 2018 émission direct =", importations2_2018)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2019" and "production" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production2_2019=(somme/nb)*12
annees3.append(2019)
production2.append(production2_2019)
print("Production 2019 émission direct =", production2_2019)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2019" and "importations" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations2_2019=(somme/nb)*12
importations2.append(importations2_2019)
print("Importation 2019 émission direct =", importations2_2019)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2020" and "production" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production2_2020=(somme/nb)*12
annees3.append(2020)
production2.append(production2_2020)
print("Production 2020 direct =", production2_2020)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2020" and "importations" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations2_2020=(somme/nb)*12
importations2.append(importations2_2020)
print("Importation 2020 émission direct =", importations2_2020)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2021" and "production" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production2_2021=(somme/nb)*12
annees3.append(2021)
production2.append(production2_2021)
print("Production 2021 émission direct =", production2_2021)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2021" and "importations" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations2_2021=(somme/nb)*12
importations2.append(importations2_2021)
print("Importation 2021 émission direct =", importations2_2021)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2022" and "production" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production2_2022=(somme/nb)*12
annees3.append(2022)
production2.append(production2_2022)
print("Production 2022 émission direct =", production2_2022)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2022" and "importations" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations2_2022=(somme/nb)*12
importations2.append(importations2_2022)
print("Importation 2022 émission direct =", importations2_2022)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2023" and "production" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production2_2023=(somme/nb)*12
annees3.append(2023)
production2.append(production2_2023)
print("Production 2023 émission direct =", production2_2023)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2023" and "importations" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations2_2023=(somme/nb)*12
importations2.append(importations2_2023)
print("Importation 2023 émission direct =", importations2_2023)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2024" and "production" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production2_2024=(somme/nb)*12
annees3.append(2024)
production2.append(production2_2024)
print("Production 2024 émission direct =", production2_2024)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2024" and "importations" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations2_2024=(somme/nb)*12
importations2.append(importations2_2024)
print("Importation 2024 émission direct =", importations2_2024)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2025" and "production" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
production2_2025=(somme/nb)*12
annees3.append(2025)
production2.append(production2_2025)
print("Production 2025 émission direct =", production2_2025)

somme=0
nb=0

for i in range(1, len(donnees2)):
    if donnees2[i][0][:4]=="2025" and "importations" in donnees2[i][1] and "directes" in donnees2[i][3]:
        valeur=donnees2[i][2]
        if valeur!="":
            somme+=float(valeur.replace(",", "."))
            nb+=1
importations2_2025=(somme/nb)*12
importations2.append(importations2_2025)
print("Importation 2025 émission direct =", importations2_2025)

from matplotlib import pyplot as plt

plt.bar(annees3, importations2, label="Importations")
plt.bar(annees3, production2, bottom=importations2, label="Production en France")

plt.ylabel("MtCO2e (Mt)")
plt.xlabel("Année")
plt.title("Émissions de GES liées à la consommation d'électricité (émissions directes)")
plt.xticks(annees3)
plt.legend()
plt.show()



donnees=[]
with open('effet_de_serre.csv',newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter=';')
	for row in reader:
		donnees.append(row)
#print(donnees)
somme=0
nb=0
for i in range(1, len(donnees)):
	if donnees[i][0][:4]=="2014":
		somme += float(donnees[i][2].replace ("," , "."))
		nb+=1
#print("Moyennes 2014=" , somme/nb)
		
for i in range(1, len(donnees)):
	if donnees[i][0][:4]=="2015":
		somme += float(donnees[i][2].replace ("," , "."))
		nb+=1
#print("Moyennes 2015=" , somme/nb)

for i in range(1, len(donnees)):
	if donnees[i][0][:4]=="2016":
		somme += float(donnees[i][2].replace ("," , "."))
		nb+=1
#print("Moyennes 2016=" , somme/nb)
		
for i in range(1, len(donnees)):
	if donnees[i][0][:4]=="2017":
		somme += float(donnees[i][2].replace ("," , "."))
		nb+=1
#print("Moyennes 2017=" , somme/nb)

for i in range(1, len(donnees)):
	if donnees[i][0][:4]=="2018":
		somme += float(donnees[i][2].replace ("," , "."))
		nb+=1
#print("Moyennes 2018=" , somme/nb)

for i in range(1, len(donnees)):
	if donnees[i][0][:4]=="2019":
		somme += float(donnees[i][2].replace ("," , "."))
		nb+=1
#print("Moyennes 2019=" , somme/nb)


for i in range(1, len(donnees)):
	if donnees[i][0][:4]=="2020":
		somme += float(donnees[i][2].replace ("," , "."))
		nb+=1
#print("Moyennes 2020=" , somme/nb)
		
for i in range(1, len(donnees)):
	if donnees[i][0][:4]=="2021":
		somme += float(donnees[i][2].replace ("," , "."))
		nb+=1
#print("Moyennes 2021=" , somme/nb)

for i in range(1, len(donnees)):
	if donnees[i][0][:4]=="2022":
		somme += float(donnees[i][2].replace ("," , "."))
		nb+=1
#print("Moyennes 2022=" , somme/nb)
		
for i in range(1, len(donnees)):
	if donnees[i][0][:4]=="2023":
		somme += float(donnees[i][2].replace ("," , "."))
		nb+=1
#print("Moyennes 2023=" , somme/nb)

for i in range(1, len(donnees)):
	if donnees[i][0][:4]=="2024":
		somme += float(donnees[i][2].replace ("," , "."))
		nb+=1
#print("Moyennes 2024=" , somme/nb)

for i in range(1, len(donnees)):
	if donnees[i][0][:4]=="2025":
		somme += float(donnees[i][2].replace ("," , "."))
		nb+=1
#print("Moyennes 2025=" , somme/nb)

from matplotlib import pyplot as plt
annee= ["2014", "2015" , "2016" , "2017", "2018 ", "2019" ,"2020" , "2021" , "2022" , "2023" , "2024" , "2025"]
valeurs= [0.5397464547375784,0.5976113121852324, 0.6608869892742477, 0.7237215195094543, 0.7109198481586964, 0.6965514183970019, 0.6780913867722648, 0.6716681314392169,0.6788086218322862, 0.6599794504749192,0.6324351607918517, 0.6082923956612957]
couleurs = ['skyblue' if int(a) < 2020 else 'orange' for a in annee]
plt.bar( annee, valeurs,color=couleurs)
plt.title("Comparaison des émissions moyennes annuelles: avant et après 2020")
plt.ylabel('Moyenne des émissions (Mt)')
plt.xlabel('Années')

plt.show()



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
noms_complets = [f"{m}\n2014 | 2024" for m in noms_mois]
plt.xticks(x, noms_complets)
plt.legend(loc='upper left')
plt.figure(figsize=(15, 8))
plt.tight_layout()
plt.show()
