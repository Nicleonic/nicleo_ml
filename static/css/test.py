# Données fournies
data = [
    {"Annee": 2007, "Prix": 271868, "Surface": 80},
    {"Annee": 2007, "Prix": 273208, "Surface": 80},
    # ... autres données ...
]

# Création d'une liste distincte pour les années
annees = list(set(d["Annee"] for d in data))

# Calcul du prix moyen par mètre carré pour chaque année
prix_moyen_par_annee = {}
for annee in annees:
    somme_prix = 0
    somme_surface = 0
    for d in data:
        if d["Annee"] == annee:
            somme_prix += d["Prix"]
            somme_surface += d["Surface"]
    prix_moyen = somme_prix / somme_surface
    prix_moyen_par_annee[annee] = prix_moyen

# Affichage des résultats
for annee, prix_moyen in prix_moyen_par_annee.items():
    print(f"Année {annee}: Prix moyen par mètre carré = {prix_moyen}")
    
# ******************************************************
import os

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
os.environ["QT_SCALE_FACTOR"] = "1"
import pandas as pd
import matplotlib.pyplot as plt

donnees = pd.read_csv('model/price_surface.csv', sep=';')

x = donnees['Annee']
y = donnees['Prix']

# Ajouter la surface comme variable y2
y2 = donnees['Surface']

# Afficher le graphique
plt.scatter(x, y, label='Prix', color='orange')
plt.scatter(x, y2, label='Surface')
plt.xlabel('Année')
plt.ylabel('Prix / Surface')
plt.legend()
plt.show()


a = donnees[["Annee", "Surface"]]
b = donnees["Prix"]
plt.plot(a, b)
plt.show()
