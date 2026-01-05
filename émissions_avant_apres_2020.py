import csv
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
plt.bar( annee, valeurs)
plt.title("Comparaison des émissions moyennes annuelles: avant et après 2020")
plt.ylabel('Moyenne des émissions (Mt)')
plt.xlabel('Années')

plt.show()






