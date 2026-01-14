import csv
donnees=[]
with open('intensité_carbone.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        donnees.append(row)

valeurs_carbone = []
dates = []
nb=0
for i in range(1, len(donnees)):
    types=donnees[i][2]
    if types== "Directes":
        date = donnees[i][0] 
        heure = donnees[i][1]
        if "2025" in date:
            jour = date[0:2]
            mois = date[3:5]
        
            if (mois == "05" and int(jour) >= 30) or (mois == "06")  :
                valeur= float(donnees[i][3].replace(",", "."))
                dates.append(date[:5])
                valeurs_carbone.append(valeur)

if len(dates) > 0 and "06" in dates[0]:
	dates.reverse()
	valeurs_carbone.reverse()


from matplotlib import pyplot as plt

plt.plot(dates, valeurs_carbone )
plt.title("Intensité Carbone du 30 Mai au 30 Juin 2025")
plt.ylabel("gCO₂/kWh")
plt.xlabel("Dates")

