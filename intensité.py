import csv
donnees=[]
with open('intensité_carbone.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        donnees.append(row)

annees=[]
moyenne=[]
somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][-4:]=="2017":
        somme+=float(donnees[i][1])
        nb+=1
        moyenne_2017=somme/nb
print("Moyenne 2017 =", moyenne_2017)
annees.append(2017)
moyenne.append(moyenne_2017)

somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][-4:]=="2018":
        somme+=float(donnees[i][1])
        nb+=1
        moyenne_2018=somme/nb
print("Moyenne 2018 =", moyenne_2018)
annees.append(2018)
moyenne.append(moyenne_2018)


somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][-4:]=="2019":
        somme+=float(donnees[i][1])
        nb+=1
        moyenne_2019=somme/nb
print("Moyenne 2019 =", moyenne_2019)
annees.append(2019)
moyenne.append(moyenne_2019)


somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][-4:]=="2020":
        somme+=float(donnees[i][1])
        nb+=1
        moyenne_2020=somme/nb
print("Moyenne 2020 =", moyenne_2020)
annees.append(2020)
moyenne.append(moyenne_2020)


somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][-4:]=="2021":
        somme+=float(donnees[i][1])
        nb+=1
        moyenne_2021=somme/nb
print("Moyenne 2021 =", moyenne_2021)
annees.append(2021)
moyenne.append(moyenne_2021)


somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][-4:]=="2022":
        somme+=float(donnees[i][1])
        nb+=1
        moyenne_2022=somme/nb
print("Moyenne 2022 =", moyenne_2022)
annees.append(2022)
moyenne.append(moyenne_2022)


somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][-4:]=="2023":
        somme+=float(donnees[i][1])
        nb+=1
        moyenne_2023=somme/nb
print("Moyenne 2023 =", moyenne_2023)
annees.append(2023)
moyenne.append(moyenne_2023)


somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][-4:]=="2024":
        somme+=float(donnees[i][1])
        nb+=1
        moyenne_2024=somme/nb
print("Moyenne 2024 =", moyenne_2024)
annees.append(2024)
moyenne.append(moyenne_2024)


somme=0
nb=0

for i in range(1,len(donnees)):
    if donnees[i][0][-4:]=="2025":
        somme+=float(donnees[i][1])
        nb+=1
        moyenne_2025=somme/nb
print("Moyenne 2025 =", moyenne_2025)
annees.append(2025)
moyenne.append(moyenne_2025)

from matplotlib import pyplot as plt
plt.plot(annees, moyenne, marker="o")
plt.ylabel("Heure")
plt.xlabel("Année")
plt.title("Chronique horaire de l'intensité carbone au périmètre de la consommation")
plt.xticks(annees)
plt.show()
