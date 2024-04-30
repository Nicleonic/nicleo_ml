import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Charger le dataset
dataset = pd.read_csv('model/mydataset.csv')

# Recuperation des variables dependantes et variables independantes 
X = dataset.iloc[:, 1].values  # superficie
y = dataset.iloc[:, 0].values  # prix

# Division de l'ensemble de données en ensemble d'entraînement et ensemble de test.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Ajustement de la régression linéaire simple à l'ensemble d'entraînement.
regressor = LinearRegression()

# Entrainement 
regressor.fit(X_train.reshape(-1, 1), y_train.reshape(-1, 1))

# Prédiction des résultats de l'ensemble de test.
y_pred = regressor.predict(X_test.reshape(-1, 1))

# Enregistrement du modèle en utilisant la bibliothèque "pickle".
# pickle.dump(regressor, open('model/mymodel.pkl', 'wb'))  #XXXXXXXXXXXXXXXXXXS

# Chargement du modèle pour comparer les résultats.
model = pickle.load(open('model/mymodel.pkl', 'rb'))
print(" 3320.0 de superficie : " ,model.predict([[3320.0]]))
print(" 50020.0 de superficie : " ,model.predict([[50020.0]]))
print('This is my test....')

print(dataset.head(20))

