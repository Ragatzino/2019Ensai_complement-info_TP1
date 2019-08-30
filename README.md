# Complément informatique, 2A, TP1

*2019, Pépin Rémi*

## Base de données et DAO

### Objectif du TP

Créer une première application qui communique avec une base de données.
Pour cela vous allez utiliser la bibliothèque python **psycopg2** et
mettre en place une **couche DAO** vu en cours.

Dans ce TP vous aller également découvrir un nouvel **IDE** et réaliser
quelques commande **Git** (on les expliquera plus en détail dans le TP4)

Notion principale abordée :
- DAO

Notions secondaires :
- Classe abstraite
- Git



### Récupérer le code du TP

Pour récupére le code du TP vous allez utiliser Git. Git est un logiciel
de versionnage et de partage de code source. Créez sur votre session un dossier "TP1-DAO", puis dans le dossier faites clic droit > Git Bash here. Cela va ouvrir un invite de commande git.

** Une petite configuration préalable de git est à prévoir : 
Proposition : Créez un dossier sur votre bureau appelé git_repositories
              Utilisez bash : Démarrer -> Informatique -> Git -> Git Bash
Ensuite : 
Dans git bash saississez

```git
cd /C/Users/*votreId*/Desktop/git_repositories

git config --global http.proxy http://pxcache-02.ensai.fr:3128
```
Vous venez de configurer votre git pour le proxy et vous allez êtes maintenant dans le dépot git repositories
```git
git clone https://github.com/HealerMikado/2019Ensai_complement-info_TP1.git squelette-TP1

cd squelette-TP1
```

Cela va vous créer un dossier squelette-TP1 avec le code de base du TP
et déplacer le curseur de git bash dans le dossier créé. Ne fermez pas
git bash.
 
> On reviendra plus en détail sur git lors du TP 4

#### PyCharm

PyCharm est un IDE spécifique à python. Il n'y a presque rien à 
configurer tout est déjà fait.

Si vous utilisez PyCharm, après avoir récupérer le TP, faites

```
File > Open > squelette-TP1 > Ok > This windows
```

Dans le paneau de gauche l'arboréscence du dossier ainsi que son 
contenu devraient apparaitre.


### Ecriture de données

#### Utiliser AvengerDAO

Dans le squelette vous avez un exemple de DAO (avenger_dao.py) qui
permet d’enregistrer en base des avengers (*méthode create()*) et de lister
les avengers enregistrés (*find_all()*). Cette classe hérite d'une classe abstraite (*abstract_dao*) ce qui permet de générer facilement les déclarations des méthodes attendues, et de créer pour toutes les DAO une seule connection
à la base de données.


![Diagramme de class](http://www.plantuml.com/plantuml/png/TSynpi8m30NWFQVms0wzmAz_Q0Ntg1pReA3WeDX5Gi3T2HAW3h0zlszv7isn-dBC0QDvHNAONc6B1Qu1O5DKXJmL1Vh4rk-IyXmlS-8kSV_tRZ3dhc_7Sc9qwU9YISLiBl4Wv4-XAZ-49SitkOT06SrWEelkfRPf8Qnt_j-6OOsZABUd7W00)


Le fichier connection.py contient la configuration de la 
connexion à la base de données et la méthode *get_connection()* la réalise.
 Modifiez le fichier connection.py pour remplacer les valeurs de MY_ID et MY_PASSWORD par votre identifiant ENSAI.
 
Le fichier main.py contient un petit programme qui crée un avengers et
 récupère liste les avengers créés.
 
Dans le repertoire sql vous avez un fichier create_avengers.sql. Sur l’ENT, allez dans mes applications > postgresql. Connectez vous avec votre identifiant (le mot de passe est aussi votre identifiant), et dans votre base (qui a pour nom votre identifiant), exécutez le contenu du fichier create_avengers.sql. Maintenant que vous avez créé votre table avengers vous pouvez y insérer des avengers.

> Note: l’id d’un avengers et de type serial. Le type serial intègre une
> séquence. L’identifiant est donc généré automatiquement lors de
> l’insertion.


Lancez le programme main.py dans la console. Vous devez voir qu’un
avenger a été créé. Depuis phpPgAdmin, consultez votre table avengers et
vérifiez que le avenger «Iron Man» est bien présent.


#### Création d'agents du shield

En se basant sur l’exemple donné avec les avengers, vous allez créer des
agents du shield. Dans le répertoire business_object, créez un fichier
shield_agent.py et définissez une classe *ShieldAgent*. Un ShieldAgent aura un identifiant, un nom et un niveau de sécurité reprénsenté par un integer.

Dans le repertoire sql, créez un fichier create_agents.sql dans lequel
vous écrivez la création de la table Agents qui vous permettra
d’enregistrer vos ShieldAgent. Exécutez la requêe sur votre base. Dans le
répertoire dao, créez un fichier dao_shield_agent.py. Dans ce fichier, générez toutes les méthodes de la classes abstraite (Ctrl+I), puis remplissez le corps des méthodes create() et find_all().


Pour pouvoir communiquer avec le base de données, vous récupérez des
*cursors* qui vous permettent d’exécuter des requêtes sql dans une
transaction. Lorsque l’on fait un commit, on valide la transaction. Si
un problème survient on peut faire un rollback = un retour 
arrière sur l’état au début de la transaction, ce qui permet d’avoir un
état cohérent en base de données.

Avec psycopg2 voilà comment gérer cela. :

```python
cur = self.connection.cursor()
try:
    cur.execute(requête SQL)
    # la transaction est enregistrée en base
    self.connection.commit()
except:
    # la transaction est annulée
    self.connection.rollback()
    raise
finally:
    cur.close()
```

 
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

Vous allez coder le corps de deux autres méthodes dans notre dao agents.

- update() qui prend en paramètre un ShieldAgent (modifié) et qui met à jour le nom et le niveau de notre agent en base. Pour tester votre méthode, après avoir créer Phil Coulson, modifiez-le en changeant son nom par "Clint Barton" et son niveau de sécurité par 9 et appelez la méthode update de votre dao. Vérifiez que que le changement s'est bien produit en base.
- delete() qui prend en paramètre un agents et qui le supprime de la base   Pour tester votre méthode, supprimez un des agents après l’avoir créé et vérifiez qu’il n’apparait pas dans votre liste.
  
Comme au dessus, via git vous allez sauvegarder votre travail. Sauvegardez tous vos fichiers d'ouvert et dans git bash tapez

```git
git add .
git commit -m "ajoute methode update, delete"
```
  
#### Lien entre agents et avengers

Maintenant nous allons lier nos agents et nos avengers. Chaque agent du shield encadre une liste de d'avengers. Pour chaque avenger qu'il encadre, l'agent dispose d'un code unique d'identification pour l'avenger, représenté sous forme d'un string. Vous allez donc créer une nouvelle table 
 pour enregistrer les liens qui existent entre les agents et les avengers.
 
- Modèle physique de donnèes
 ![diagramme de model physique](https://i.imgur.com/zsVUinZ.png)
 
- Diagramme de classes

  ![diagramme de classe](http://www.plantuml.com/plantuml/png/POv12i9034NtEKKku0MwaFOCFO24cKyTI5F9f1KHx-uiH0TS_f3tU6CDyTXNfQHIAy_N0itJ0Wj-aiaA7dWEBxPGHTgznEEYEA3jNYpeHHzoEc0B_8yIBL9_yxRTuTrEM-wUcwqlE7sj0yEIP0UVYMY4vTRy1W00)


Vous aller devoir modifier la classe Agent et Agent_dao pour refléter
cette modification.

Une fois le TP terminé dans git bash tapez

```git
git add .
git commit -m "fin du TP"
```

#### Bonus

Implémenter toues les fonctions dont hérite les DAO.
