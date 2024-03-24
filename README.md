# Cr0ss_iT

Read this document in [english](README_en.md)

**Une application pour simplifier l'organisation des événements sportifs scolaires faites avec pygame !**

## Description

Cr0ss_iT est une application développée avec Pygame, conçue pour simplifier l'organisation des événements sportifs scolaires. Elle offre des fonctionnalités telles que la gestion des événements sportifs, l'inscription des élèves via un formulaire ou l'importation de données CSV, la création et le suivi des courses, un système de départ avec QR Code pour un chronométrage précis, une organisation de base de données efficace et l'affichage du classement. Cr0ss_iT représente une solution complète et conviviale pour les écoles souhaitant optimiser la gestion de leurs événements sportifs.

![image](https://github.com/RB-2804/Cr0ss-iT/assets/130835974/c8376baf-5168-407c-b3a1-b00164f57ca7)

## Table des matières
- [Démo](#démo)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#Installation)
- [Utilisation](#comment-l'utiliser-?)

## Démo 

### Exemple de notre BDD 

![image](https://github.com/RB-2804/Cr0ss-iT/assets/130835974/5d2b2a8c-09b9-4b8f-bc8c-609b529b6ee4)


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

  ![image_2024-03-24_224156500](https://github.com/RB-2804/Cr0ss-iT/assets/130835974/24e92af5-727a-4118-b880-a343a0eba67f)

  - Cet onglet permet d'enregistrer manuellement un élève à l'aide d'un formulaire.
  - Il propose également un bouton "Créer QR Code" pour générer des QR codes uniques associés à chaque élève.
  - Un bouton "Importer un fichier" permet d'importer un fichier CSV pour enregistrer automatiquement les élèves dans la base de données.

### Schéma conceptuel (non abouti)

![image](https://github.com/RB-2804/Cr0ss-iT/assets/130835974/8b9f2090-18c7-446a-aef5-8e6a9d193e28)

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
