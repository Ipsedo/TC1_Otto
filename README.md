# Projet de TC1

Samuel Berrien, David Biard

Challenge [Otto](https://www.kaggle.com/c/otto-group-product-classification-challenge)

* `courbes.ipynb` : création de différentes courbes avec `pyplot`
* `exploration_donnes.ipynb` : affichage d'informations utiles sur les données
* `sklearn_grid_search.ipynb` : recherche d'hyper-paramètres pour différents modèles avec `GridSearchCV`
* `soumission_kaggle.ipynb` : Entraînement de modèles pour la soumission Kaggle
* `data.data.py` : Chargement des données
* `data.data_info.py` : Fonction pour récupérer différentes informations sur les données
* `utils.kaggle_submit.py` : Fonction pour la création de soumission Kaggle
* `utils.model_utils.py` : Fonction pour l'évaluation de modèles `sklearn`

Il faut créer un dossier `res` et y placer les fichier `train.csv` et `test.csv` comme suivant :
```
TC1_Otto
 |-- ...
 |-- res
      |-- train.csv
      |-- test.csv
      |-- ...
```
