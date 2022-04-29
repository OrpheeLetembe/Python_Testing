 # Description
 Société qui a créé une plateforme numérique pour coordonner les compétitions de force en Amérique du Nord et en Australie, décide de mettre en place une version plus légère de la plateforme actuelle suite à des critiques sur les réseaux sociaux.

Cette version devra répondre aux exigences fonctionnelles suivants :

1- Le secrétaire d’un club doit pouvoir se connecte à l'application via son adresse email.
2-	Le secrétaire identifie une compétition à venir et clique sur celle-ci.
-  Il voit le nombre d'inscriptions disponibles et si d'autres peuvent être acceptées ou non.
- Le secrétaire peut alors utiliser les points accumulés par le club pour réserver des places pour la compétition.
- Si le club dispose d’assez de points et qu’il reste des places disponible le secrétaire y devrait voir un message de confirmation. 
- Les points utilisés sont alors déduits du compte du club.
- le secrétaire doit recevoir un message d'erreur si le club n'a pas assez de points, s'il essaie de réserver plus de 12 places ou si le concours est complet.

3-	Tous les utilisateurs peuvent consulter la liste des points des clubs.

# Technologies utilisées :
-	Python v3.x+
-	Flask


# Installation et exécution de l'application 

1	Cloner ce dépôt de code à l'aide de la commande ‘$ git clone clone https://github.com/OrpheeLetembe/Python_Testing.git 

2	 Rendez-vous depuis un terminal à la racine du répertoire du projet 

3	Créer un environnement virtuel pour le projet avec la commande :

- `$ python -m venv env` sous windows 
- `$ python3 -m venv env` sous macos ou linux.

4	Activez l'environnement virtuel avec la commande :

- `$ env\Scripts\activate` sous windows 
- `$ source env/bin/activate` sous macos ou linux.

5	Installez les dépendances du projet avec la commande :
- `$ pip install -r requirements.txt`

6	Démarrer l’application : Flask exige que vous définissiez une variable d'environnement pour le fichier python. Quelle que soit la façon dont vous le faites, vous devez définir le fichier comme étant server.py. Vérifiez [ici](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) pour plus de détails 

Les étapes 1 à 5 ne sont requises que pour l'installation initiale. Pour les lancements ultérieurs de l'application, il suffit d'exécuter l’étape 6 à partir du répertoire racine du projet.

Lorsque le serveur fonctionne, après l'étape 6 de la procédure, l’application peut être accessible via url http://127.0.0.1:5000. Ce dernier ouvrira un navigateur qui vous présentera la page d’accueil de l’application permettant la connexion de l’utilisateur et un lien vers la page de la liste des clubs.

# Configuration actuelle
L'application est alimentée par des fichiers JSON. C'est pour éviter d'avoir une base de données jusqu'à ce que nous en ayons réellement besoin. Les principaux fichiers sont :
-	competitions.json - liste des compétitions
-	clubs.json - liste des clubs avec des informations pertinentes. Vous pouvez regarder ici pour voir quelles adresses email l'application acceptera pour la connexion.

# Cadre de tests
-	[Pytest-flask](https://flask.palletsprojects.com/en/2.1.x/testing/): Pour l’exécution des tests unitaires et d’intégration.
-	[Selenium](https://www.selenium.dev/documentation/): Pour l’exécution des tests fonctionnels.
-	[Locust](https://docs.locust.io/en/stable/): Pour mesurer la performance.
-	[Coverage](https://coverage.readthedocs.io/en/6.3.2/) : Pour mesurer la couverture des tests.
