#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:56:54 2024

@author: llb
"""

import pygame
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import sqlite3
from qrcode import make
import cv2
import time
import sys

# SCREEN window
pygame.init()
LARGEUR = 1280
LONGUEUR = 720
SCREEN = pygame.display.set_mode((LARGEUR, LONGUEUR))
pygame.display.set_caption('Cr0ss_iT')

# background color
BCKGR_COLOR = (103, 146, 149)

# colors
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
GRIS = (178, 196, 196)
GRIS_FONCE = (87, 111, 112)

# coordonées des boutons
BT_ACCUEIL = [0, 0, 200, 50]
BT_INSCRIPTIONS = [200, 0, 200, 50]
BT_RESULTARRIVAL = [400, 0, 200, 50]
BT_CLASSEMENTS = [600, 0, 200, 50]
BT_COURSE = [800, 0, 200, 50]

# etat des fenetre
ACCUEIL_SC = 'accueil'
INSCRIPTIONS_SC = 'inscriptions'
DEPART_SC = 'arrivees'
COURSE_SC = 'course'
CLASSEMENT_SC = 'classement'


def camera(tps1, liste_eleves, liste_resultat, id_eleves_course):
    """
        Fonction qui utilise la caméra pour détecter et lire les QR codes.

        Args:
            tps1 (float): Le temps de début de la course.
            liste_eleves (list): Liste des identifiants des élèves déjà enregistrés.
            liste_resultat (list): Liste des résultats des élèves.
            id_eleves_course (list): Liste des identifiants des élèves participant à la course.

        Returns:
            list: Liste mise à jour des résultats des élèves.
    """
    global usertext_cam

    data = None
    a = None
    while True:

        cap = cv2.VideoCapture(int(user_text_cam))  # le numero correspond à numéro de la webcam utilisée
        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()

        while True:
            _, img = cap.read()
            # detect and decode
            data, bbox, _ = detector.detectAndDecode(img)
            # check if there is a QRCode in the image
            if data == 'stop':
                break
            elif data:
                a = int(data)
                if a not in liste_eleves:
                    if a in id_eleves_course:
                        liste_eleves.append(a)
                        liste_resultat.append([a, time.time_ns() - tps1])
                break

            cv2.imshow("QRCODEscanner", img)
            if cv2.waitKey(1) == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
        if data == 'stop':
            break

    return liste_resultat

def convertir_temps_nano_en_format(temps_nano):
    """
        Convertit le temps en nanosecondes en format (minutes:secondes,millisecondes).

        Args:
            temps_nano (int): Temps en nanosecondes à convertir.

        Returns:
            str: Temps converti au format (minutes:secondes,millisecondes).
    """
    temps_secondes = temps_nano / 1e9
    minutes = int(temps_secondes // 60)
    secondes = int(temps_secondes % 60)
    millisecondes = int((temps_secondes - int(temps_secondes)) * 1000)

    resultat_format = f"{minutes:02d}:{secondes:02d},{millisecondes:03d}"
    
    return resultat_format


def remplissage_table_eleves():
    """
    Lit un fichier CSV et remplit la table 'eleves' dans la base de données.
    """
    db = "Data/BDD_Course.db"

    with open(csv_file, 'r',  encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=';')
        liste = list(reader)

    conn = sqlite3.connect(db)

    cur = conn.cursor()
    cur.execute("SELECT nom FROM eleves ;")

    for i in range(len(liste)):
        cur = conn.cursor()
        cur.execute("INSERT INTO eleves (nom, classe, sexe) VALUES (?, ?, ?) ;", (liste[i][0], liste[i][1],None))

        conn.commit()
        cur.close()

    conn.close()


def select_csv_file():
    """
       Permet à l'utilisateur de sélectionner un fichier CSV via une interface graphique.

       Returns:
           str: Chemin absolu du fichier CSV sélectionné.
    """
    Tk().withdraw()
    filename = askopenfilename(filetypes=[("CSV Files", "*.csv")])
    return filename


# fonction pour creer un bouton
def create_b(surface, X, Y, LARGEUR, hauteur, couleur_bord, texte, couleur_texte, taille_text):
    """
    Crée un bouton dans une surface pygame.

    Args:
        surface (pygame.Surface): Surface sur laquelle dessiner le bouton.
        X (int): Coordonnée x du coin supérieur gauche du bouton.
        Y (int): Coordonnée y du coin supérieur gauche du bouton.
        LARGEUR (int): Largeur du bouton.
        hauteur (int): Hauteur du bouton.
        couleur_bord (tuple): Couleur du bord du bouton au format (R, G, B).
        texte (str): Texte à afficher dans le bouton.
        couleur_texte (tuple): Couleur du texte du bouton au format (R, G, B).
        taille_text (int): Taille de la police du texte.

    """
    pygame.draw.rect(surface, couleur_bord, (X, Y, LARGEUR, hauteur))
    font = pygame.font.Font(None, taille_text)
    text = font.render(texte, True, couleur_texte)
    surface.blit(text, (X + LARGEUR // 2 - text.get_width() // 2, Y + hauteur // 2 - text.get_height() // 2))


# fonction pour creer une zone de texte
def create_tb(surface, X, Y, LARGEUR, hauteur, texte, couleur_texte, taille_police):
    """
    Crée une zone de texte dans une surface pygame.

    Args:
        surface (pygame.Surface): Surface sur laquelle dessiner la zone de texte.
        X (int): Coordonnée x du coin supérieur gauche de la zone de texte.
        Y (int): Coordonnée y du coin supérieur gauche de la zone de texte.
        LARGEUR (int): Largeur de la zone de texte.
        hauteur (int): Hauteur de la zone de texte.
        texte (str): Texte à afficher dans la zone de texte.
        couleur_texte (tuple): Couleur du texte de la zone de texte au format (R, G, B).
        taille_police (int): Taille de la police du texte.

    """
    font = pygame.font.Font(None, taille_police)
    text = font.render(texte, True, couleur_texte)
    surface.blit(text, (X, Y))



# fonction pour afficher l'ecran
def affichage(a, b, c, d, e):
    """
    Affiche les éléments graphiques dans la fenêtre pygame.

    Args:
        a (tuple): Couleur du fond.
        b (tuple): Couleur du bouton "Accueil".
        c (tuple): Couleur du bouton "Inscriptions".
        d (tuple): Couleur du bouton "Départ".
        e (tuple): Couleur du bouton "Course".

    """
    SCREEN.fill(BCKGR_COLOR)
    create_b(SCREEN, BT_ACCUEIL[0], BT_ACCUEIL[1], BT_ACCUEIL[2], BT_ACCUEIL[3], a, "Accueil", NOIR, 36)
    create_b(SCREEN, BT_INSCRIPTIONS[0], BT_INSCRIPTIONS[1], BT_INSCRIPTIONS[2], BT_INSCRIPTIONS[3], b, "Inscriptions",
             NOIR, 36)
    create_b(SCREEN, BT_RESULTARRIVAL[0], BT_RESULTARRIVAL[1], BT_RESULTARRIVAL[2], BT_RESULTARRIVAL[3], c, "Départ",
             NOIR, 36)
    create_b(SCREEN, BT_CLASSEMENTS[0], BT_CLASSEMENTS[1], BT_CLASSEMENTS[2], BT_CLASSEMENTS[3], d, "Course", NOIR, 36)
    create_b(SCREEN, BT_COURSE[0], BT_COURSE[1], BT_COURSE[2], BT_COURSE[3], e, "Classement", NOIR, 36)


def qrcode():
    """
        Génère des codes QR pour chaque élève et les enregistre en tant qu'images PNG.
    """
    id_eleves = requete("SELECT id_eleves FROM eleves")
    prenom_eleves = requete("SELECT nom FROM eleves ")

    for i in range(len(id_eleves)):
        img = make(id_eleves[i][0])
        img.save(f"{prenom_eleves[i][0]}.png")

def requete(r):
    """
        Exécute une requête SQL sur la base de données.

        Args:
            r (str): Requête SQL à exécuter.

        Returns:
            list: Résultat de la requête.
    """
    connexion = sqlite3.connect("Data/BDD_Course.db")
    curseur = connexion.cursor()

    curseur.execute(r)

    reponse = curseur.fetchall()
    connexion.close()

    return reponse


def requete_insert(r,v):
    """
        Exécute une requête SQL d'insertion sur la base de données.

        Args:
            r (str): Requête SQL d'insertion à exécuter.
            v (tuple): Valeurs à insérer dans la requête.

        Returns:
            None
    """
    connexion = sqlite3.connect("Data/BDD_Course.db")
    curseur = connexion.cursor()

    curseur.execute(r,v)

    connexion.commit()
    curseur.close()
    connexion.close()

def requete_del(r):
    """
        Exécute une requête SQL de suppression sur la base de données.

        Args:
            r (str): Requête SQL de suppression à exécuter.

        Returns:
            None
    """
    connexion = sqlite3.connect("Data/BDD_Course.db")
    curseur = connexion.cursor()

    curseur.execute(r)

    connexion.commit()
    curseur.close()
    connexion.close()

def create_classement(surface, X, Y, liste_elements, couleur_bord, couleur_texte, taille_text):
    """
    Crée un classement visuel sur une surface pygame.

    Args:
        surface (pygame.Surface): La surface sur laquelle dessiner le classement.
        X (int): La coordonnée X du coin supérieur gauche du classement.
        Y (int): La coordonnée Y du coin supérieur gauche du classement.
        liste_elements (list): La liste des éléments à afficher dans le classement.
        couleur_bord (tuple): La couleur du bord des éléments (format : (R, G, B)).
        couleur_texte (tuple): La couleur du texte des éléments (format : (R, G, B)).
        taille_text (int): La taille du texte des éléments.
    """
    max_largeur = max([len(element) * taille_text // 2.5 for element in liste_elements])
    x_c = X
    y_c = Y
    i = 0
    font = pygame.font.Font(None, taille_text)

    for element in liste_elements:
        largeur = max_largeur
        rect = pygame.Rect(x_c, y_c, largeur, taille_text)
        pygame.draw.rect(surface, couleur_bord, rect)
        text = font.render(element, True, couleur_texte)
        text_rect = text.get_rect(center=rect.center)
        surface.blit(text, text_rect.topleft)
        y_c += taille_text + 5

        i += 1
        if i == 20:
            x_c += max_largeur + 5
            y_c = Y
            i = 0

########### variables ###########
etat = ACCUEIL_SC # État de l'interface actuelle
genre = "Choisissez une option" # Genre de l'utilisateur
coul = GRIS # Couleur de fond par défaut
nom = "" # Nom de l'utilisateur
prenom = "" # Prénom de l'utilisateur
classe = "" # Classe de l'utilisateur
course = "" # Nom de la course
classe_p = "" # Classe participante à une course
d = "" # Distance à parcourir
cam = "" # Numéro de la caméra
genre_participant = "genre" # Genre du participant à une course

choix = False # Variable de sélection
choix2 = False # Variable de sélection 2
depart = False # Variable de départ de la course
insc_save = False # Variable de sauvegarde d'inscription
choisir_course = False # Variable de choix de course

user_text_nom = '' # Texte entré par l'utilisateur pour le nom
user_text_prenom = '' # Texte entré par l'utilisateur pour le prénom
user_text_classe = '' # Texte entré par l'utilisateur pour la classe
user_text_course = '' # Texte entré par l'utilisateur pour le nom de la course
user_text_classe_p = '' # Texte entré par l'utilisateur pour la classe participante
user_text_distance = '' # Texte entré par l'utilisateur pour la distance
user_text_cam = '' # Texte entré par l'utilisateur pour le numéro de caméra
db = "Data/BDD_Course.db" # Nom de la base de données
id_eleves_course = None # ID des élèves dans une course
liste = []

liste_course = [] # Liste des courses disponibles
liste_course_class = [] # Liste des courses pour le classement
course_id_tableaux = None # ID de la course sélectionnée
nom_course = None # Nom de la course sélectionnée
nom_eleves_course = [] # Noms des élèves dans une course
premier = True # Indicateur du premier élève dans une course
requete_id = False # Indicateur de requête pour ID
camera_on = False # Indicateur de la caméra activée
nouvelle_course = True # Indicateur d'une nouvelle course
liste_eleves = [] # Liste des élèves
liste_resultat = [] # Liste des résultats de la course
liste_participants_course = [] # Liste des participants à une course
tps1 = time.time_ns() # Temps de départ de la course
eleves = [] # Élèves inscrits à une course
#################################


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos() # Récupère les coordonnées de la souris

            if BT_ACCUEIL[0] < mouse_x < BT_ACCUEIL[0] + BT_ACCUEIL[2] and BT_ACCUEIL[1] < mouse_y < BT_ACCUEIL[1] + \
                    BT_ACCUEIL[3]:
                etat = ACCUEIL_SC
                liste_course = []

            elif BT_INSCRIPTIONS[0] < mouse_x < BT_INSCRIPTIONS[0] + BT_INSCRIPTIONS[2] and BT_INSCRIPTIONS[
                1] < mouse_y < BT_INSCRIPTIONS[1] + BT_INSCRIPTIONS[3]:
                etat = INSCRIPTIONS_SC
                liste_course = []


            elif BT_RESULTARRIVAL[0] < mouse_x < BT_RESULTARRIVAL[0] + BT_RESULTARRIVAL[2] and BT_RESULTARRIVAL[
                1] < mouse_y < BT_RESULTARRIVAL[1] + BT_RESULTARRIVAL[3]:
                etat = DEPART_SC
                liste_course = []

            elif BT_CLASSEMENTS[0] < mouse_x < BT_CLASSEMENTS[0] + BT_CLASSEMENTS[2] and BT_CLASSEMENTS[1] < mouse_y < \
                    BT_CLASSEMENTS[1] + BT_CLASSEMENTS[3]:
                etat = COURSE_SC
                liste_course = []
            
            elif BT_COURSE[0] < mouse_x < BT_COURSE[0] + BT_COURSE[2] and BT_COURSE[1] < mouse_y < \
                    BT_COURSE[1] + BT_COURSE[3]:
                etat = CLASSEMENT_SC
                liste_course = []

            # menu depliant dans inscription pour choisir un genre
            if (370 < mouse_x < 400 and 250 < mouse_y < 275):
                choix = not choix

            # menu depliant dans depart pour choisir une course
            if (375 < mouse_x < 400 and 100 < mouse_y < 125):
                depart = not depart

            # menu dépliant dans course pour choisir le genre qui participe a la course
            if (525 < mouse_x < 550 and 200 < mouse_y < 225):
                choix2 = not choix2

            # menu dépliant dans départ pour choisir la course a lancée
            if (300 < mouse_x < 550 and 100 < mouse_y < 125):
                choisir_course = not choisir_course

        # Gestion des états de l'application
        if etat == ACCUEIL_SC:
            affichage(BCKGR_COLOR, GRIS, GRIS, GRIS, GRIS)

            # instructions

            create_tb(SCREEN, 450, 100, LARGEUR - 200, LONGUEUR - 200, "Cr0ss_iT", BLANC, 103)

            # les images
            fond = pygame.image.load('Assets/cross.jpg')
            fond = fond.convert()

            screen_rect = SCREEN.get_rect()
            image_rect = fond.get_rect()

            X = (screen_rect.width - image_rect.width) // 2
            Y = (screen_rect.height - image_rect.height) // 2

            SCREEN.blit(fond, (X, Y))
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #quitter l'application
            create_b(SCREEN, 1055, 695, 225, 25, BLANC, "Quitter", GRIS_FONCE, 28)
            if 1055 < mouse_x < 1280 and 695 < mouse_y < 720:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()

        if etat == INSCRIPTIONS_SC:

            affichage(GRIS, BCKGR_COLOR, GRIS, GRIS, GRIS)

            create_b(SCREEN, 950, 100, 225, 25, BLANC, "Créer QRcode", GRIS_FONCE, 28)

            #creer les qrcodes
            if 950 < mouse_x < 1175 and 100 < mouse_y < 125:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    qrcode()

            # données nom
            create_tb(SCREEN, 50, 100, LARGEUR - 200, LONGUEUR - 200, "Nom :", BLANC, 32)
            create_b(SCREEN, 150, 100, 200, 25, GRIS, "", GRIS_FONCE, 28)
            if user_text_nom:
                create_b(SCREEN, 150, 100, 200, 25, GRIS, user_text_nom, GRIS_FONCE, 28)
            elif nom:
                create_b(SCREEN, 150, 100, 200, 25, GRIS, "Entrez un nom", GRIS_FONCE, 28)

            active = False
            nom = True
            if 150 < mouse_x < 350 and 100 < mouse_y < 125:
                    active = True
                    nom = False

            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    user_text_nom = user_text_nom[:-1]
                    nom = False
                else:
                    user_text_nom += event.unicode

            # données prénom
            create_tb(SCREEN, 50, 150, LARGEUR - 200, LONGUEUR - 200, "Prénom :", BLANC, 32)
            create_b(SCREEN, 150, 150, 200, 25, GRIS, "", GRIS_FONCE, 28)
            if user_text_prenom:
                create_b(SCREEN, 150, 150, 200, 25, GRIS, user_text_prenom, GRIS_FONCE, 28)
            elif prenom:
                create_b(SCREEN, 150, 150, 200, 25, GRIS, "Entrez un prénom", GRIS_FONCE, 28)

            active_p = False
            prenom = True
            if 150 < mouse_x < 350 and 150 < mouse_y < 175:
                active_p = True
                prenom = False

            if event.type == pygame.KEYDOWN and active_p:
                if event.key == pygame.K_BACKSPACE:
                    user_text_prenom = user_text_prenom[:-1]
                else:
                    user_text_prenom += event.unicode


            # données classe
            create_tb(SCREEN, 50, 200, LARGEUR - 200, LONGUEUR - 200, "Classe :", BLANC, 32)
            create_b(SCREEN, 150, 200, 200, 25, GRIS, "", GRIS_FONCE, 28)
            if user_text_classe:
                create_b(SCREEN, 150, 200, 200, 25, GRIS, user_text_classe, GRIS_FONCE, 28)
            elif classe:
                create_b(SCREEN, 150, 200, 200, 25, GRIS, "Entrez une classe", GRIS_FONCE, 28)

            active_c = False
            classe = True
            if 150 < mouse_x < 350 and 200 < mouse_y < 225:
                active_c = True
                classe = False

            if event.type == pygame.KEYDOWN and active_c:
                if event.key == pygame.K_BACKSPACE:
                    user_text_classe = user_text_classe[:-1]
                else:
                    user_text_classe += event.unicode

            create_b(SCREEN, 370, 200, 25, 25, BLANC, "i", GRIS_FONCE, 28)

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if 370 < mouse_x < 395 and 200 < mouse_y < 255:
                if event.type == pygame.MOUSEMOTION:
                    create_b(SCREEN, 395, 200, 250, 40, GRIS_FONCE, "CM2 / 6e / 2nd / 1ere / Tle", BLANC, 28)

            # données genre
            create_tb(SCREEN, 50, 250, LARGEUR - 200, LONGUEUR - 200, "Genre :", BLANC, 32)
            create_b(SCREEN, 150, 250, 225, 25, coul, genre, GRIS_FONCE, 28)
            create_b(SCREEN, 370, 250, 25, 25, GRIS, "v", GRIS_FONCE, 28)

            # menu dépliant
            if choix:
                create_b(SCREEN, 210, 275, 200, 25, GRIS, "Féminin", GRIS_FONCE, 28)
                create_b(SCREEN, 210, 300, 200, 25, GRIS, "Masculin", GRIS_FONCE, 28)

                mouse_x, mouse_y = pygame.mouse.get_pos()

                if 210 < mouse_x < 410 and 275 < mouse_y < 300:
                    create_b(SCREEN, 210, 275, 200, 25, BLANC, "Féminin", GRIS_FONCE, 28)  # devient BLANC en survolant

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        genre = "Féminin"
                        coul = BLANC
                        choix = not choix

                if 210 < mouse_x < 410 and 300 < mouse_y < 325:
                    create_b(SCREEN, 210, 300, 200, 25, BLANC, "Masculin", GRIS_FONCE,
                             28)  # devient BLANC en survolant

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        genre = "Masculin"
                        coul = BLANC
                        choix = not choix

            # bouton enregistrer
            create_b(SCREEN, 600, 300, 225, 25, BLANC, "Enregistrer", GRIS_FONCE, 28)

            if 600 < mouse_x < 825 and 300 < mouse_y < 325:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    nom_eleves = user_text_nom +" " + user_text_prenom

                    i = requete("SELECT MAX(id_eleves) FROM eleves")
                    if i[0][0] is None:
                        i = 0
                    else :
                        i = i[0][0]+1
                    requete_insert("INSERT INTO eleves VALUES (?,?,?,?);",(i,nom_eleves, user_text_classe, genre))
                    user_text_nom = ""
                    user_text_classe = ""
                    user_text_prenom = ""
                    genre ="Choisissez une option"
                    coul = GRIS


            # importer un fichier
            create_tb(SCREEN, 0, 400, LARGEUR - 200, LONGUEUR - 200,
                      " --------------------------------------------------------------------------------------- ou ---------------------------------------------------------------------------------------",
                      GRIS, 32)
            create_b(SCREEN, 520, 500, 225, 25, BLANC, "Importer un fichier", GRIS_FONCE, 32)

            if 520 < mouse_x < 750 and 500 < mouse_y < 525:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    csv_file = select_csv_file()
                    try:
                        remplissage_table_eleves()

                    except:
                        mouse_x = 0
                        mouse_y = 0

        if etat == DEPART_SC:

            affichage(GRIS, GRIS, BCKGR_COLOR, GRIS, GRIS)
            
            #bouton démarrer
            create_b(SCREEN, 900, 100, 225, 25, BLANC, "Démarrer", GRIS_FONCE, 28)

            #choix numero camera
            if user_text_cam:
                create_b(SCREEN, 625, 100, 225, 25, GRIS, user_text_cam, GRIS_FONCE, 28)
            elif cam:
                create_b(SCREEN, 625, 100, 225, 25, GRIS, "Numéro de la caméra", GRIS_FONCE, 28)
            elif not cam:
                create_b(SCREEN, 625, 100, 225, 25, GRIS, "Numéro de la caméra", GRIS_FONCE, 28)

            active_cam = False
            cam = True
            if 625 < mouse_x < 850 and 100 < mouse_y < 125:
                active_cam = True
                cam = False

            if event.type == pygame.KEYDOWN and active_cam:
                if event.key == pygame.K_BACKSPACE:
                    user_text_cam = user_text_cam[:-1]
                    cam = False
                else:
                    user_text_cam += event.unicode

            #demarre la course
            if 900 < mouse_x < 1125 and 100 < mouse_y < 125 and course_id_tableaux != None and nom_course != None:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if nouvelle_course:
                        tps1 = time.time_ns()
                        nouvelle_course = False

                liste_resultat = camera(tps1, liste_eleves, liste_resultat, id_eleves_course)
                mouse_x = 0
                mouse_y = 0
                for resul in range(len(liste_resultat)):
                    liste_resultat[resul][1] = convertir_temps_nano_en_format(liste_resultat[resul][1])

                for resul in liste_resultat:
                    requete_insert("INSERT INTO participe VALUES (?, ?, ?, ?) ",(course_id_tableaux, resul[0], resul[1], None))

            if liste_course == []:
                courses = requete("SELECT id_course,nom FROM course ;")
                for i in range(len(courses)):
                    liste_course.append(courses[i])

            # CHOISIR UNE COURSE
            create_tb(SCREEN, 50, 100, LARGEUR - 200, LONGUEUR - 200, "Choisir une course :", BLANC, 32)

            if course_id_tableaux == None:
                create_b(SCREEN, 300, 100, 225, 25, coul, "choisir", GRIS_FONCE, 28)
            else:
                create_b(SCREEN, 300, 100, 225, 25, BLANC, liste_course[j][1], GRIS_FONCE, 28)

            create_b(SCREEN, 525, 100, 25, 25, GRIS, "v", GRIS_FONCE, 28)

            if choisir_course:

                for i in range(len(liste_course)):
                    y_c = 125 + i * 25
                    create_b(SCREEN, 525, y_c, 200, 25, GRIS, liste_course[i][1], GRIS_FONCE, 28)

                    if (525 < mouse_x < y_c and 100 < mouse_y < 125):
                        create_b(SCREEN, 525, y_c, 200, 25, GRIS, liste_course[i][1], BLANC, 28)

                if 525 < mouse_x < 725 and 125 < mouse_y and event.type == pygame.MOUSEBUTTONDOWN:
                    j = 0
                    while 125 + 25 * j < mouse_y < 125 + 25 * len(liste_course):
                        j += 1
                    j -= 1

                    course_id_tableaux = liste_course[j][0]
                    nom_course = liste_course[j][1]
                    requete_id = True
                    nouvelle_course = True
                    liste_resultat = []
                    liste_tps = []
                    liste_eleves = []
                    id_eleves_course = []
                    premier = True

                    if requete_id:
                        nom_courses = requete(f"SELECT classe FROM course WHERE nom = '{courses[j][1]}'")
                        id_eleves_tuple = requete(f"SELECT DISTINCT(eleves.id_eleves) FROM eleves JOIN course  ON eleves.sexe = course.genre WHERE eleves.classe LIKE '{nom_courses[0][0][0]}%' AND eleves.sexe = (SELECT genre FROM course WHERE nom = '{liste_course[j][1]}')  ;")
                        for i in range (len(id_eleves_tuple)):
                            id_eleves_course.append(id_eleves_tuple[i][0])

                        requete_id = False

                        eleves_tuple = requete(f"SELECT DISTINCT(eleves.nom) , eleves.classe FROM eleves JOIN course  ON eleves.sexe = course.genre WHERE eleves.classe LIKE '{nom_courses[0][0][0]}%' AND eleves.sexe = (SELECT genre FROM course WHERE nom = '{liste_course[j][1]}')  ;")
                        eleves = []
                        for i in range(len(eleves_tuple)):
                            eleves.append(eleves_tuple[i])

                    choisir_course = not choisir_course

            else:
                if course_id_tableaux == None:
                    create_b(SCREEN, 300, 100, 225, 25, coul, "choisir", GRIS_FONCE, 28)
                else:
                    create_b(SCREEN, 300, 100, 225, 25, BLANC, liste_course[j][1], GRIS_FONCE, 28)

                x_c = 5
                y_c = 150
                eleves_course = []
                for i in range(len(eleves)):
                    eleves_course.append(eleves[i][0])
                    create_classement(SCREEN, x_c, y_c, eleves_course, GRIS, GRIS_FONCE, 23)

        if etat == COURSE_SC:

            affichage(GRIS, GRIS, GRIS, BCKGR_COLOR, GRIS)

            create_tb(SCREEN, 50, 100, LARGEUR - 200, LONGUEUR - 200, "Nom de la course :", BLANC, 32)
            create_b(SCREEN, 300, 100, 225, 25, GRIS, "", GRIS_FONCE, 28)
            if user_text_course:
                create_b(SCREEN, 300, 100, 225, 25, GRIS, user_text_course, GRIS_FONCE, 28)
            elif course:
                create_b(SCREEN, 300, 100, 225, 25, GRIS, "nom", GRIS_FONCE, 28)

            active_co = False
            course = True
            if 300 < mouse_x < 525 and 100 < mouse_y < 125:
                active_co = True
                course = False

            # Gère la saisie utilisateur pour le nom de la course
            if event.type == pygame.KEYDOWN and active_co:
                if event.key == pygame.K_BACKSPACE:
                    user_text_course = user_text_course[:-1]
                else:
                    user_text_course += event.unicode


            create_b(SCREEN, 545, 150, 25, 25, BLANC, "i", GRIS_FONCE, 28)

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if 545 < mouse_x < 570 and 150 < mouse_y < 175:
                if event.type == pygame.MOUSEMOTION:
                    create_b(SCREEN, 570, 150, 250, 40, GRIS_FONCE, "CM2 / 6e / 2nd / 1ere / Tle", BLANC, 28)

            create_tb(SCREEN, 50, 150, LARGEUR - 200, LONGUEUR - 200, "Classe participante :", BLANC, 32)
            create_b(SCREEN, 300, 150, 225, 25, GRIS, "", GRIS_FONCE, 28)
            if user_text_classe_p:
                create_b(SCREEN, 300, 150, 225, 25, GRIS, user_text_classe_p, GRIS_FONCE, 28)
            elif classe_p:
                create_b(SCREEN, 300, 150, 225, 25, GRIS, "classe", GRIS_FONCE, 28)

            active_cl_p = False
            classe_p = True
            if 300 < mouse_x < 525 and 150 < mouse_y < 175:
                active_cl_p = True
                classe_p = False

            if event.type == pygame.KEYDOWN and active_cl_p:
                if event.key == pygame.K_BACKSPACE:
                    user_text_classe_p = user_text_classe_p[:-1]
                else:
                    user_text_classe_p += event.unicode

            # distance
            create_tb(SCREEN, 50, 250, LARGEUR - 200, LONGUEUR - 200, "Distance a parcourir :", BLANC, 32)
            create_b(SCREEN, 300, 250, 225, 25, GRIS, "", GRIS_FONCE, 28)
            if user_text_distance:
                create_tb(SCREEN, 300, 250, 225, 25, user_text_distance, GRIS_FONCE, 28)
            elif d :
                create_b(SCREEN, 300, 250, 225, 25, GRIS, "distance", GRIS_FONCE, 28)

            active_d = False
            d = True
            if 300 < mouse_x < 525 and 250 < mouse_y < 275:
                active_d = True
                d = False

            if event.type == pygame.KEYDOWN and active_d:
                if event.key == pygame.K_BACKSPACE:
                    user_text_distance = user_text_distance[:-1]
                else:
                    user_text_distance += event.unicode

            create_tb(SCREEN, 50, 200, LARGEUR - 200, LONGUEUR - 200, "Genre participante :", BLANC, 32)
            create_b(SCREEN, 300, 200, 225, 25, coul, genre_participant, GRIS_FONCE, 28)
            create_b(SCREEN, 525, 200, 25, 25, GRIS, "v", GRIS_FONCE, 28) # bouton pour ouvrir le menu déroulant du genre du participant

            # menu dépliant
            if choix2:
                create_b(SCREEN, 350, 225, 200, 25, GRIS, "Féminin", GRIS_FONCE, 28)
                create_b(SCREEN, 350, 250, 200, 25, GRIS, "Masculin", GRIS_FONCE, 28)

                mouse_x, mouse_y = pygame.mouse.get_pos()

                if 350 < mouse_x < 550 and 225 < mouse_y < 250:
                    create_b(SCREEN, 350, 225, 200, 25, BLANC, "Féminin", GRIS_FONCE, 28)  # devient BLANC en survolant

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        genre_participant = "Féminin"
                        coul = BLANC
                        choix2 = not choix2

                if 350 < mouse_x < 550 and 250 < mouse_y < 275:
                    create_b(SCREEN, 350, 250, 200, 25, BLANC, "Masculin", GRIS_FONCE,
                             28)  # devient BLANC en survolant

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        genre_participant = "Masculin"
                        coul = BLANC
                        choix2 = not choix2

            # bouton pour enregistrer les informations de la course
            create_b(SCREEN, 600, 300, 225, 25, BLANC, "Enregistrer", GRIS_FONCE, 28)

            if 600 < mouse_x < 875 and 300 < mouse_y < 325:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Récupère la date et l'heure actuelles
                    heure = time.strftime("%H:%M:%S", time.localtime())
                    date = time.strftime("%Y-%m-%d", time.localtime())
                    i_c = requete("SELECT MAX(id_course) FROM course") # identifiant de la nouvelle course
                    if type(i_c[0][0]) != int :
                        i_c = 1
                    else:
                        i_c = i_c[0][0]+1
                    # Insère les informations de la course dans la base de données
                    requete_insert("INSERT INTO course VALUES  (?,?,?,?,?,?,?);", (i_c, heure, user_text_course, user_text_distance, date, genre_participant, user_text_classe_p))

                    # Réinitialise les valeurs pour les prochaines entrées
                    genre_participant = "genre"
                    user_text_classe_p = ""
                    user_text_course = ""
                    user_text_distance = ""
                    coul = GRIS

            mouse_x, mouse_y = pygame.mouse.get_pos()
            create_b(SCREEN, 100, 400, 225, 25, BLANC, "REINITIALISER TOUT", GRIS_FONCE, 28)
            # Réinitialise toutes les tables de la base de données
            if 100 < mouse_x < 325 and 400 < mouse_y < 425:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    requete_del("DELETE FROM participe ;")
                    requete_del("DELETE FROM course ;")
                    requete_del("DELETE FROM eleves ;")
                    requete_del("DELETE FROM SQLITE_SEQUENCE WHERE name='eleves';")

            create_b(SCREEN, 100, 450, 225, 25, BLANC, "REINITIALISER Course", GRIS_FONCE, 28)
            # Réinitialise la table course
            if 100 < mouse_x < 325 and 400 < mouse_y < 475:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    requete_del("DELETE FROM course ;")

            create_b(SCREEN, 100, 500, 225, 25, BLANC, "REINITIALISER Participe", GRIS_FONCE, 27)
            # Réinitialise la table participe
            if 100 < mouse_x < 325 and 500 < mouse_y < 525:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    requete_del("DELETE FROM participe ;")

            create_b(SCREEN, 100, 550, 225, 25, BLANC, "REINITIALISER Eleves", GRIS_FONCE, 28)
            # Réinitialise la table élèves
            if 100 < mouse_x < 325 and 550 < mouse_y < 575:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    requete_del("DELETE FROM eleves ;")
                    requete_del("DELETE FROM SQLITE_SEQUENCE WHERE name='eleves';")

        if etat == CLASSEMENT_SC :

            affichage(GRIS, GRIS, GRIS, GRIS, BCKGR_COLOR)

            # requête pour obtenir le classement des participants par course
            classment = requete("SELECT p.id_course, e.nom FROM  participe p INNER JOIN eleves e ON p.id_eleves = e.id_eleves ORDER BY p.id_course, p.temps")

            # dictionnaire pour stocker les participants par course triés par leur temps
            classement = {}
            for row in classment:
                id_course, nom_eleve = row
                if id_course not in classement:
                    classement[id_course] = []
                classement[id_course].append(nom_eleve)

            if liste_course_class == []:
                classm = requete("SELECT id_course,nom FROM course;")
                for i in range(len(classm)):
                    liste_course_class.append(classm[i])

            create_tb(SCREEN, 50, 100, LARGEUR - 200, LONGUEUR - 200, "Choisir une course :", BLANC, 32)

            if course_id_tableaux == None:
                create_b(SCREEN, 300, 100, 225, 25, coul, "choisir", GRIS_FONCE, 28)
            else:
                create_b(SCREEN, 300, 100, 225, 25, BLANC, liste_course_class[j][1], GRIS_FONCE, 28)

            create_b(SCREEN, 525, 100, 25, 25, GRIS, "v", GRIS_FONCE, 28)

            if choisir_course:

                for i in range(len(liste_course_class)):
                    y_c = 125 + i * 25
                    create_b(SCREEN, 525, y_c, 200, 25, GRIS, liste_course_class[i][1], GRIS_FONCE, 28)

                    if (525 < mouse_x < y_c and 100 < mouse_y < 125):
                        create_b(SCREEN, 525, y_c, 200, 25, GRIS, liste_course_class[i][1], BLANC, 28)

                if 525 < mouse_x < 725 and 125 < mouse_y and event.type == pygame.MOUSEBUTTONDOWN:
                    j = 0
                    while 125 + 25 * j < mouse_y < 125 + 25 * len(liste_course_class):
                        j += 1
                    j -= 1

                    course_id_tableaux = liste_course_class[j][0]
                    nom_course = liste_course_class[j][1]

                    if course_id_tableaux in classement:
                        liste_participants_course = classement[course_id_tableaux]

                    choisir_course = not choisir_course

            # Affiche le classement des participants à la course sélectionnée
            x_c = 5
            y_c = 150

            if liste_participants_course:

                # Affiche les trois premiers participants avec des couleurs spécifiques
                if len(liste_participants_course) >= 3:
                    create_classement(SCREEN, 450, 150, [f"{1}. {liste_participants_course[0]}"], (255,215,0), (255,255,255), 28)
                    create_classement(SCREEN, 350, 185, [f"{2}. {liste_participants_course[1]}"], (192,192,192), (255,255,255), 28)
                    create_classement(SCREEN, 650, 185, [f"{3}. {liste_participants_course[2]}"], (110, 77, 37), (255,255,255), 28)

                # Affiche le reste des participants
                for i, participant in enumerate(liste_participants_course[3:], start=4):
                    create_classement(SCREEN, 5, 250 + (i - 4) * 25, [f"{i}. {participant}"], GRIS, GRIS_FONCE, 28)

    pygame.display.update()#Met à jour l'affichage

pygame.quit()
