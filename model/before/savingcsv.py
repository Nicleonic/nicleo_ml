import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('nom_du_fichier.csv')

column_data = data['nom_de_la_colonne']
n_rows = 100  # Nombre de lignes à prendre
column_data = column_data[:n_rows]

plt.scatter(range(n_rows), column_data)
plt.xlabel('Index')
plt.ylabel('Valeur de la colonne')
plt.title('Scatter Plot')
plt.show()

new_data = pd.DataFrame({'nom_de_la_colonne': column_data})
new_data.to_csv('nouveau_fichier.csv', index=False)


"""
    Pour lire un fichier CSV, afficher un graphique scatter plot et enregistrer les données dans un nouveau fichier CSV en utilisant la bibliothèque pandas, vous pouvez suivre les étapes suivantes :

Importez les bibliothèques nécessaires :
python
Copier
import pandas as pd
import matplotlib.pyplot as plt
Chargez le fichier CSV à l'aide de la fonction read_csv de pandas :
python
Copier
data = pd.read_csv('nom_du_fichier.csv')
Assurez-vous de remplacer 'nom_du_fichier.csv' par le nom réel de votre fichier CSV.

Obtenez les données d'une colonne spécifique et le nombre de lignes souhaité :
python
Copier
column_data = data['nom_de_la_colonne']
n_rows = 100  # Nombre de lignes à prendre
column_data = column_data[:n_rows]
Remplacez 'nom_de_la_colonne' par le nom de la colonne réelle que vous souhaitez extraire et définissez n_rows selon le nombre de lignes que vous souhaitez prendre.

Créez un graphique scatter plot avec les données extraites :
python
Copier
plt.scatter(range(n_rows), column_data)
plt.xlabel('Index')
plt.ylabel('Valeur de la colonne')
plt.title('Scatter Plot')
plt.show()
Enregistrez les données extraites dans un nouveau fichier CSV :
python
Copier
new_data = pd.DataFrame({'nom_de_la_colonne': column_data})
new_data.to_csv('nouveau_fichier.csv', index=False)
Remplacez 'nom_de_la_colonne' par le nom de la colonne réelle, 'nouveau_fichier.csv' par le nom que vous souhaitez donner au nouveau fichier CSV.

Assurez-vous d'avoir les bibliothèques pandas et matplotlib installées sur votre système avant d'exécuter ce code.
    
    
    
"""