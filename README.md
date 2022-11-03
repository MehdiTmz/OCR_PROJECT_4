# OCR_PROJECT_4
# Développez un programme logiciel en Python

Le but de ce projet est de pouvoir créer gérer la création d'un tournoi et de pourvoir générer plusieurs rapports.

## Installation:
Commencez tout d'abord par installer Python. Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:

```git clone https://github.com/MehdiTmz/OCR_PROJECT_4```

Placez vous dans le dossier OC_P4_ChessTournament, puis créez un nouvel environnement virtuel:

```python -m venv env```

Ensuite, activez-le. Windows:

```env\scripts\activate.bat```

Il ne reste plus qu'à installer les packages requis:

```pip install -r requirements.txt```

Vous pouvez enfin lancer le script:

```python main.py```

## Les menus
On peut décomposer le programme en plusieurs menu.

Le menu principale qui permet de :
  1. Créer un nouveau tournoi
  2. Ajouter un nouveau joueur
  3. Changer le rang d'un joueur
  4. Afficher le menu des rapports
  5. Quitter l'application

Dans un tournoi, un sous-menu est disponible entre chaque round et permet de :
  1. Passez au round suivant
  2. Afficher la liste des joueurs d'un tournoi
  3. Changer le rangs d'un joueur

Dans le menu des rapports, on peut :
  1. Afficher la liste de tout les joueurs
  2. Afficher la liste de tout les joueurs d'un tournoi
  3. Afficher la liste de tout les tournois
  4. Afficher la liste de tout les rounds d'un tournoi
  5. Afficher la liste de tout les matchs d'un tournoi
