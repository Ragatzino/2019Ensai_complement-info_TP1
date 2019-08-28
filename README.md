# Complément informatique, 2A, TP1

## Base de données et DAO

### Objectif du TP

Créer une première application qui communique avec la base de données.
Pour cela vous aller utiliser la bibliothèque python **psycopg2** et
mettre en place une couche DAO vu en cours.

Dans ce TP vous aller également découvrir un nouvel IDE et réaliser
quelques commande Git (on les expliquera plus en détail dans le TP4)

Notion principale abordée :
- DAO

Notions secondaires :
- Classe abstraite
- Git



### Récupérer le code du TP

Pour récupéer le code du TP vous allez utiliser Git. Git est un logiciel
de versionnage et de partage de code source. Pour récupérer le TP créez
sur votre session un dossier "TP1-DAO", puis dans le dossier faites
clic droit /> Git Bash here. Cela va ouvrir un invite de commande git.

Dans git bash saississez

```git
git clone https://github.com/HealerMikado/2019Ensai_complement-info_TP1.git squelette-TP1

cd squelette-TP1
```

Cela va vous créer un dossier squelette-TP1 avec le code de base du TP
et déplacer le curseur de git bash dans le dossier créer. Ne fermez pas
git bash.
 
> On reviendra plus en détail sur git lors du TP 4

### Nouvel IDE

En fonction de votre tuteur vous allez soit utiliser visual studio code,
soit PyCharm. Dans les deux cas, ces deux (environnement de développement
intégré) sont très différents de Spyder. Spyder est fait pour utiliser
python comme un outil de data science, pas pour développer une application.
Ce qui est le cas de VScode et PyCharm.

#### PyCharm

PyCharm est un IDE spécifique à python. Il n'y a presque rien à 
configurer tout est déjà fait.

Si vous utilisez PyCharm, après avoir récupérer le TP, faites

```
File > Open > squelette-TP1 > Ok > This windows
```

Dans le paneau de gauche l'arboréscence du dossier ainsi que son 
contenu devrait apparaitre.

#### VScode

VScode est un IDE léger, mais vide par défaut. Il faut lui télécharger
des extensions pour prendre en charge différent langage.

Allez dans Fichier > Préférences > Paramètres : dans la fenêtre d’édition de droite, ajoutez entre
les accolades :
"telemetry.enableTelemetry": false
Ouvrez le répertoire obtenu (Fichier > Ouvrir le dossier …)
Dans le menu vertical à gauche, allez dans les extensions (icone carrée), recherchez Python (avec
le moteur de recherche en haut) et installez la première extension de la liste (qui se nomme
python)
Installez autopep8 et pylint : dans le menu en haut allez dans « Afficher » > « terminal intégré »
Tapez la ligne de commande suivante :
pip install autopep8 pylint --user --proxy http://pxcache-02.ensai.fr:3128
Pour pouvoir lancer un script python facilement, allez dans Fichier > Préférences > Raccourcis
Clavier
Dans la fenêtre qui s’ouvre, cliquez sur keybindings.json
Dans la fenêtre de droite mettez le contenu suivant :
// Place your key bindings in this file to overwrite the defaults
[
 {"key

### Ecriture de données

#### Utiliser AvengerDAO

Dans le squelette vous avez un exemple de DAO (avenger_dao.py) qui
permet d’enregistrer en base des avengers (méthode create) et de lister
les avengers enregistrés. Cette classe hérite d'une classe abstraite
(abstract_dao) ce qui permet de générer facilement les déclarations des
méthodes attendues, et de créer pour toutes les DAO une seule connection
à la base de données.

Le fichier fichier connection.py contient la configuration de la 
connexion à la base de données et la méthode get_connection() la réalise.

Le fichier main.py contient un petit programme qui crée un avengers et
 récupère liste les avengers créés. Modifiez le fichier connection.py pour remplacer la valeur MY_ID par votre
identifiant ENSAI. Dans le repertoire sql vous avez un fichier
create_avengers.sql. Sur l’ENT, allez dans mes applications > postgresql

Connectez vous avec votre identifiant (le mot de passe est aussi votre
identifiant), et dans votre base (qui a pour nom votre identifiant),
exécutez le contenu du fichier create_avengers.sql Maintenant que vous
avez créé votre table book vous pouvez y insérer des avengers.

> Note: l’id d’un avengers et de type serial. Le type serial intègre une
> séquence. L’identifiant est donc généré automatiquement lors de
> l’insertion.

Installez psycopg2 pour pouvoir se connecter et consulter votre base de
donnée. Vous pouvez retrouver la documentation de psycopg2 ici :
http://initd.org/psycopg

```bash
pip install psycopg2 --user --proxy http://pxcache-02.ensai.fr:3128
```

Lancez le programme main.py Dans la console, vous devez voir qu’un
avenger a été créé. Depuis phpPgAdmin, consultez votre table avengers et
vérifiez que le avenger «Spider Man» est bien présent.


#### Création d'agents du shield

En se basant sur l’exemple donné avec les avengers, nous allons créé des
agents du shield. Dans le répertoire business_object, créez un fichier
agent.py et définissez une classe Agent. Un Agent aura un identifiant,
un nom et un niveau de sécurité (de 1 à 10, puis 33, niveau accessible
uniquement par Nick Fury).

Dans le repertoire sql, créez un fichier create_agents.sql dans lequel
vous écrivez la création de la table Agents qui vous permettra
d’enregistrer vos agents. Exécutez le sur votre base. Dans le
répertoire dao, créez un fichier dao_agent.py Dans ce fichier, de façon
similaire à dao_avenger, créez une méthode create et une méthode
fin_all qui vous permettent de créer des agents du shield et de
lister les agents créés.

Pour pouvoir communiquer avec le base de données, nous récupérons des
cursors qui nous permettent d’exécuter des requêtes sql dans une
transaction. Lorsque l’on fait un commit, on valide la transaction. Si
un problème survient on peut faire un rollback, on fait alors un retour 
arrière sur l’état au début de la transaction, ce qui permet d’avoir un
état cohérent en base de données.

Avec psycopg2 voilà comment gérer cela. :

```python
with connection.cursor() as cur:
  # instructions
  
  connection.commit()
```

Explicitement on commit la transaction. Mais implicitement, close() est
exécutée (à la fin du block) et rollback si un exception est levée. 
Créer un fichier main_agents.py dans lequel vous créez 3 agents, par
exemple "Phil Coulson", "Maria Hill" et "Nick Fury" et listez les agents
créés avec la méthode get_all_agents.

Via git vous allez sauvegarder votre travail. Sauvegardez tous vos fichiers
d'ouvert et dans git bash tapez

```git
git add .
git commit -m "initialisation DAO agent"
```

#### Suppression et mise à jour

Vous allez ajouter 2 méthodes dans notre dao agents.

- update qui prend en paramètre un agent (modifié) et qui met à jour le
  nom et le niveau de notre agent en base. Pour
  tester votre méthode, après avoir créer Phil Coulson, modifiez le en
  changeant son nom par "Clint Barton" et son niveau de sécurité par 9 et
  appelez la méthode update de votre dao. Vérifiez que pour les 3
  derniers agents, vous Clint Barton à la place de Phil Coulson
- delete qui prend en paramètre un agents et qui le supprime de la base
  Pour tester votre méthode, supprimez un des agents après l’avoir
  créé et vérifiez qu’il n’apparait pas dans votre liste
  
Comme au dessus, via git vous allez sauvegarder votre travail. Sauvegardez tous vos fichiers
d'ouvert et dans git bash tapez

```git
git add .
git commit -m "ajoute methode update, delete"
```
  
#### Lien entre agents et avengers

Un peu sur le même principe que l'exemple donné dans le cours, vous
aller faire le lien entre la table agents et avengers. Chaque agent va
gérer un certain nombre d'avengers.

Chaque agent du shield a une liste de d'avengers. Pour chaque avenger
qu'il encadre, un score d'affinité va être donné (exprimé en entier).
Vous allez donc créer une nouvelle tables Agent_Avenger pour
enregistrer les agents et lui associer des avengers.
 
Vous aller devoir modifier la classe Agent et Agent_dao pour refléter
cette modification.

Une fois le TP terminé dans git bash tapez

```git
git add .
git commit -m "fin du TP"
```
