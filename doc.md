# Description technique du projet

## Affichage

L'affichage de l'application est réalisé à partir de Pygame. La bibliothèque Pygame propose des objets Rect qui permettent de dessiner des rectangles. En créant des fonctions, nous pouvons créer des rectangles avec un texte prédéfini par l'appel de la fonction. De plus, nous avons la possibilité d'entrer du texte dans une zone définie par un rectangle grâce au module Pygame.

## Base de données

Dans ce projet, l'utilisation d'une base de données est primordiale pour structurer les données des élèves, des courses et des participations aux courses. Elle assure l'intégrité des données, facilite leur manipulation et garantit la pérennité de l'application. Grâce à elle, les opérations telles que l'affichage des listes d'élèves ou le calcul des classements sont efficaces et sécurisées. En somme, notre BDD offre une solution solide et flexible pour gérer les informations de manière efficace.

Le principe des clés primaires et des clés étrangères est utilisé dans notre base de données pour assurer le bon fonctionnement et identifier de manière unique chaque enregistrement.

Notre base de données utilise des clés primaires et des clés étrangères. L'identifiant de chaque table est défini comme clé primaire. Dans la table "participe", les colonnes "id_course" et "id_eleve" servent de clé composite pour garantir l'unicité des relations. De plus, la clé étrangère "id_eleve" de la table "participe" fait référence à la clé primaire "id_eleve" de la table "eleves" et la clé étrangère "id_course" fait référence à la clé primaire "id_course" de la table "course".

Grâce à la base de données, nous pouvons insérer les noms des élèves mais aussi les récupérer grâce aux fonctions nous permettant de réaliser des requêtes SQL en Python. C'est ainsi que nous pouvons afficher la liste des élèves participant à une course ou encore le classement lorsqu'une course est terminée.

L'utilisation du module Tkinter nous permet de sélectionner le fichier CSV de notre choix. Lors de l'importation des élèves dans la BDD, nous devons également spécifier l'encodage en UTF-8 pour éviter la présence de caractères spéciaux dans les noms.

## Caméra

Le module OpenCV-Python est une bibliothèque open-source largement utilisée pour le traitement d'images. Il fournit des fonctionnalités pour la manipulation d'images en temps réel, la détection d'objets, le suivi de mouvement, la reconnaissance faciale, le calibrage de la caméra, et bien plus encore.

Dans notre cas, nous l'avons utilisé dans le but de détecter les QR Codes des élèves.

Nous pouvons choisir la caméra que vous voulez utiliser et nous avons utilisé l'application Iriun, qui permet, si l'ordinateur qui fait tourner l'application et le téléphone portable sont connectés sur le même réseau Wi-Fi, d'accéder à la caméra du téléphone portable pour obtenir un semblant de "webcam" sans fil. Vous pouvez également utiliser directement une webcam reliée à l'ordinateur.

## App Design

### Les onglets

L'application est composée de plusieurs onglets tels que l'onglet d'accueil, l'onglet de départ, l'onglet de la course et l'onglet classement. Pour changer d'onglet, il suffit simplement de cliquer sur le nom de l'onglet.

(requirements.txt : pip freeze > requirements.txt)
