# Cr0ss iT

Read this document in [english](README_en.md)

**Une application pour simplifier l'organisation des événements sportifs scolaires faites avec pygame !**

![image](https://github.com/RB-2804/Cross-iT/assets/130835974/43d66d9a-7c62-4eed-8b38-a505f582ad9c)

## Table des matières
- [Démo](#démo)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#Installation)
- [Utilisation](#comment-l'utiliser-?)

## Démo 

## Fonctionnalités

### Gestion des événements sportifs

  - Inscription des élèves aux différentes épreuves
    
  - Importation de données via un fichier CSV pour une gestion plus efficace
    
  - Création et suivi des différentes courses
    
  - Système de départ avec QR Code pour un chronométrage précis et un classement efficace à l'arrivée

## Installation

### Windows 

Apres avoir installé Python3 (version 3.7 ou plus), lancez la commande suivante :

![image](https://github.com/RB-2804/Cross-iT/assets/130835974/6962260a-cf2f-48dc-9272-37c0a6294404)

Ainsi que les modules csv et cv2 pour un bon fonctionnement :

- pip install csv opencv-python-headless

### Ubuntu

Apres avoir installé le paquet SOL2 ( IIbsd12-dev pour Ubuntu), Python3 (version 3.7 Ou plus), et lancez la commande suivante :

- sudo pip3 install pygame opencv-python-headless

## Comment l'utiliser ?

Quand vous lancez l'application, une fenetre s'ouvrira avec plusieurs onglets :

### Onglets
- Accueil

  - Ce premier onglet affiche un bouton "Réinitialiser" pour réinitialiser la base de données et un bouton "Quitter" pour fermer l'application.
  
- Inscription

  - Cet onglet permet d'enregistrer manuellement un élève à l'aide d'un formulaire.
  - Il propose également un bouton "Créer QR Code" pour générer des QR codes uniques associés à chaque élève.
  - Un bouton "Importer un fichier" permet d'importer un fichier CSV pour enregistrer automatiquement les élèves dans la base de données.

- Départ

  - Dans cet onglet, vous pouvez sélectionner une course parmi celles disponibles.
  - Il affiche la liste des élèves participant à la course sélectionnée.
  - Vous pouvez également saisir dans une zone de texte le numéro de la caméra à utiliser.
  - Un bouton "Démarrer" lancera la caméra et démarrera un chronomètre interne au code.

- Course
  
  - Cet onglet propose un formulaire pour créer une nouvelle course.
  - Vous pouvez sélectionner la classe, le genre et la distance de la course, qui seront enregistrés dans la base de données.
  
- Classement

  - Une fois la course terminée, cet onglet permet de sélectionner le classement de la course, affichant les 3 premiers temps.

## License de la photo 

© 2024 Lycée La Bourdonnais. All rights reserved.
