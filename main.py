# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:34:39 2020

@author: CLEBRET1
"""

import tkinter
from tkinter import LabelFrame, Label, Listbox, Radiobutton, StringVar, Button
from PIL import ImageTk, Image

#########################
# Variables préliminaires
#########################

chemin_dossier = "//elis.priv/Fichiers/Gie/Utilisateurs/CLEBRET1/Desktop/icons/"

global liste_reponses
liste_reponses = []

global index_question
index_question = 0

################################################
# Creatioon de la structure graphique generale #
################################################

# Creation de la fenetre principale
fenetre = tkinter.Tk()
fenetre.title("Floupy : Le dictateur bienveillant !!")

# Creation du cadre du portrait dans la fenetre
cadre_portrait = LabelFrame(fenetre, text = "portrait_Floupy")
cadre_portrait.pack(side = "left")

# Creation du cadre de la question dans la fenetre
cadre_question = LabelFrame(fenetre, text = "Que veux tu faire ?")
cadre_question.pack(side = "top")

# Creation du cadre de la question dans la fenetre
cadre_conditions = LabelFrame(fenetre, text = "La réponse de Floupy")
cadre_conditions.pack(side = "bottom")

#######################
# Liste des questions #
#######################

# Requete 0

q0 = "Est-ce-que je peux jouer à la console ?"
c0 = ["Es-tu-habillé ?", "Sommes nous actuellement entre 14h et 18h ?", "As tu fais tes devoirs ?"]
r0 = [1,1,1]

requete_0 = [q0, c0, r0]

# Requete 1

q1 = "Est-ce-que je peux aller dans la piscine ?"
c1 = ["Somme nous en Juillet ou Aout ?"]
r1 = [1]

requete_1 = [q1, c1, r1]

# Assemblage de toutes le requetes
requetes = [requete_0, requete_1]

###########################
# ETAPE 3 : Floupy réagit #
###########################

def reaction_finale():

    autorisation = True
    
    # Vérification des réponses (si une réponse fausse -> nok)
    for index, reponse in enumerate(requetes[index_question][2]) : 
        
        try : 
        
            if int(liste_reponses[index].get()) != reponse :
            
                autorisation = False    

        except :
            
            print("You didn't tick all boxes")
            
            return None
    
    # Si toutes les réponses sont Bonnes
    if autorisation == True :
        
        # Formatage de l'image pour intégration à la fenetre
        image_ok = Image.open(chemin_dossier + "ok.jpg")
        image_ok = image_ok.resize((250, 250), Image.ANTIALIAS)
        tkimage_ok = ImageTk.PhotoImage(master = cadre_portrait, image = image_ok)
        
        # Mise à jour du label qui contiendra l'image        
        label_portrait.configure(image = tkimage_ok)
        label_portrait.image = tkimage_ok
    
    # Si il y a des réponses fausses
    if autorisation == False :
        
        # Formatage de l'image pour intégration à la fenetre
        image_nok = Image.open(chemin_dossier + "nok.jpg")
        image_nok = image_nok.resize((250, 250), Image.ANTIALIAS)
        tkimage_nok = ImageTk.PhotoImage(master = cadre_portrait, image = image_nok)

        # Mise à jour du label qui contiendra l'image                
        label_portrait.configure(image = tkimage_nok)
        label_portrait.image = tkimage_nok
    
#################################################
# ETAPE 2 : L'utilisateur choisit une question #
#################################################

def question_choisie(tkevent):

    # Destruction de tous les widgets présent dans le cadre conditions
    for widget in cadre_conditions.winfo_children():
        widget.destroy()
    
    # Récuperation de l'index de la question
    event_question = tkevent.widget
    index_question = int(event_question.curselection()[0])
     
    # Ecriture des conditions et des OUI/NON
    for index, condition in enumerate(requetes[index_question][1]):
        
        # Creation et intégration d'un label comportant la condition
        label_condition = Label(cadre_conditions, text = condition)
        label_condition.pack()
        
        # Creation d'une liste d'objets contenant les réponses choisies
        liste_reponses.append(StringVar())      
        
        # Creation et intégration du bouton OUI
        bouton_oui = Radiobutton(cadre_conditions, variable = liste_reponses[index], text = "oui", value = 1)
        bouton_oui.pack()
        
        # Creation et intégration du bouton NON
        bouton_non = Radiobutton(cadre_conditions, variable = liste_reponses[index], text = "non", value = 0)
        bouton_non.pack()
    
    # Creation et intégration du bouton de validation
    go = Button(cadre_conditions, text = "Alors Floupy ?", command = reaction_finale)
    go.pack()  

#########################################
# ETAPE 1 :Initialisation de la fenetre #
#########################################

# Formatage de l'image pour intégration à la fenetre
image_neutre = Image.open(chemin_dossier + "neutre.jpg")
image_neutre = image_neutre.resize((250, 250), Image.ANTIALIAS)
tkimage_neutre = ImageTk.PhotoImage(master = cadre_portrait, image = image_neutre)

# Creation et intégration du label qui contiendra l'image
label_portrait = Label(cadre_portrait, image = tkimage_neutre)
label_portrait.image = tkimage_neutre
label_portrait.pack()

# Creation de la liste des questions
listbox_questions = Listbox(cadre_question, justify = 'center')
listbox_questions.bind("<<ListboxSelect>>", question_choisie)

# Charger la liste de questions
for index, requete in enumerate(requetes):
    listbox_questions.insert(index, requete[0])

# Intégrer la liste des questions
listbox_questions.config(width = 0)    
listbox_questions.pack(side = "top")

# Creation et intégration d'un label initial dans les conditions
label_noquestion = Label(cadre_conditions, text = "Tu n'as pas encore sélectionné une question")
label_noquestion.pack()

fenetre.call('wm', 'attributes', '.', '-topmost', '1')
fenetre.mainloop()