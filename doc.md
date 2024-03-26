# Description technique du projet

## Affichage

L'affichage de l'application est réalisé à partir de Pygame. La bibliothèque Pygame propose des objets Rect qui permettent de dessiner des rectangles. En créant des fonctions, nous pouvons créer des rectangles avec un texte prédéfini par l'appel de la fonction. De plus, nous avons la possibilité d'entrer du texte dans une zone définie par un rectangle grâce au module Pygame 

## Base de données

Le principe des clés primaires et des clés étrangères est utilisé dans cette base de données pour assurer l'intégrité référentielle et identifier de manière unique chaque enregistrement.

Notre base de données utilise des clés primaires et des clés étrangères. L'identifiant de chaque table est défini comme clé primaire, tandis que dans la table "participe", les colonnes "id_course" et "id_eleves" servent de clé composite pour garantir l'unicité des relations. De plus, la clé étrangère "id_eleves" de la table "participe" fait référence à la clé primaire "id_eleves" de la table "eleves" et la clé étrangère "id_course" fait référence à la clé primaire "id_course" de la table "course".



Grace a la base de donnees nous pouvons inserer les noms des eleves mais aussi les recuperer grace aux fonctions nous permettant de realiser des requettes SQL en python. C'est ainsi que nous pouvons afficher la liste des eleves participant a une course ou encore le classement lorsqu'une course est terminee.

L'utilisation du module Tkinter nous permet de sélectionner le fichier CSV de notre choix. Lors de l'importation des élèves dans la BDD, nous devons également coder l'encodage en UTF-8 pour éviter la présence de caractères spéciaux dans les noms.

## Camera

Le module OpenCV-Python est une bibliothèque open-source largement utilisée pour le traitement d'images. Il fournit des fonctionnalités pour la manipulation d'images en temps réel, la détection d'objets, le suivi de mouvement, la reconnaissance faciale, la calibrage de la caméra et bien plus encore.

Pour notre cas, nous l'avons utilise dans le but de detecter les QR Code des eleves 

Nous pouvons choisir la camera pour laquelle vous voulez utiliser et nous avons utilise l'application Iriun (explication de ce qu'est l'application) qui nous permet si l'ordinateur qui fait tournee l'application et le telephone portable soit connecte sur un meme reseau wifi ait access a la camera du telephone portable pour avoir un semblant de "webcam" sans fil ou vous pouvez utiliser directement une webcam reliee a l'ordinateur.

