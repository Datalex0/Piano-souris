#Importation du module tkinter (affichage et paramétrage de la fenêtre)
from tkinter import *
#Importation du module pygame
import pygame

# Initialisation de pygame
pygame.init()
pygame.mixer.init()
 
notes = {
    'DO': pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano souris/SRC/Notes/1_DO.wav"),
    'RE': pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano souris/SRC/Notes/2_RE.wav"),
    'MI': pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano souris/SRC/Notes/3_MI.wav"),
    'FA': pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano souris/SRC/Notes/4_FA.wav"),
    'SOL': pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano souris/SRC/Notes/5_SOL.wav"),
    'LA': pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano souris/SRC/Notes/6_LA.wav"),
    'SI': pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano souris/SRC/Notes/7_SI.wav"),
    
    'DO2': pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano souris/SRC/Notes/8_DO2.wav"),
    'RE2': pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano souris/SRC/Notes/9_RE2.wav"),
    'MI2': pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano souris/SRC/Notes/10_MI2.wav"),
    'FA2': pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano souris/SRC/Notes/11_FA2.wav"),
    'SOL2': pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano souris/SRC/Notes/12_SOL2.wav"),
    'LA2': pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano souris/SRC/Notes/13_LA2.wav"),
    'SI2': pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano souris/SRC/Notes/14_SI2.wav")
}

def jouerNote(note):
    son = notes[note]
    son.play()
     
#Fenetre principal
Fenetre = Tk()
Fenetre.title("Clavier Piano Numerique") #Definition du nom de la fenetre
Fenetre.columnconfigure(0, weight = 1) #position colonne
Fenetre.rowconfigure(0, weight = 5) #position ligne
Fenetre.rowconfigure(1, weight = 5) #position ligne
Fenetre.rowconfigure(2, weight = 1) #position ligne
#Importation du cadre 1
cadre1 = Frame(Fenetre, borderwidth = 3, relief = "sunken")
cadre1.grid(row = 0, column = 0, pady = 5, padx = 5, sticky = "ewns")
cadre1.columnconfigure(0, weight = 1)
cadre1.columnconfigure(2, weight = 1)
cadre1.rowconfigure(0, weight = 1)
#Importation du cadre n
cadren = Frame(Fenetre, borderwidth = 3, relief = "sunken")
cadren.grid(row = 1, column = 0, sticky = "ns")
cadren.rowconfigure(0, weight = 1)
cadren.columnconfigure(0, weight = 1)
#Importation du cadre 2
cadre2 = Frame(Fenetre, borderwidth = 3, relief = "sunken")
cadre2.grid(row = 2, column = 0, pady = 5, padx = 5, sticky = "ewns")
cadre2.rowconfigure(0, weight =5)
cadre2.rowconfigure(1,weight = 1)
#creation du frame dans cadre n
frame=Frame(cadren)
frame.grid()
#Definition des boutons cadre noir dans la frame
tdo= Button(frame,state = DISABLED,padx=0,pady=0, height=15,bg="black", width=13,relief=RIDGE)
tdo.grid(row = 0, column = 1,sticky = "ns")
tre= Button(frame,state = DISABLED,padx=0,pady=0, height=15,bg="black", width=13,relief=RIDGE)
tre.grid(row = 0, column = 2, sticky = "ns")
tmi= Button(frame,state = DISABLED,padx=0,pady=0, height=15,bg="black", width=13,relief=RIDGE)
tmi.grid(row = 0, column = 3, sticky = "ns")
tfa= Button(frame,state = DISABLED,padx=0,pady=0, height=15,bg="black", width=13,relief=RIDGE)
tfa.grid(row = 0, column = 4, sticky = "ns")
tsol= Button(frame,state = DISABLED,padx=0,pady=0, height=15,bg="black", width=13,relief=RIDGE)
tsol.grid(row = 0, column = 5, sticky = "ns")
tsol= Button(frame,state = DISABLED,padx=0,pady=0, height=15,bg="black", width=13,relief=RIDGE)
tsol.grid(row = 0, column = 6, sticky = "ns")
tsi= Button(frame,state = DISABLED,padx=0,pady=0, height=15,bg="black", width=13,relief=RIDGE)
tsi.grid(row = 0, column = 7, sticky = "ns")
tdo= Button(frame,state = DISABLED,padx=0,pady=0, height=15,bg="black", width=13,relief=RIDGE)
tdo.grid(row = 0, column = 8, sticky = "ns")
tdo= Button(frame,state = DISABLED,padx=0,pady=0, height=15,bg="black", width=13,relief=RIDGE)
tdo.grid(row = 0, column = 9, sticky = "ns")
tdo= Button(frame,state = DISABLED,padx=0,pady=0, height=15,bg="black", width=13,relief=RIDGE)
tdo.grid(row = 0, column = 10, sticky = "ns")
tdo= Button(frame,state = DISABLED,padx=0,pady=0, height=15,bg="black", width=13,relief=RIDGE)
tdo.grid(row = 0, column = 11, sticky = "ns")
tdo= Button(frame,state = DISABLED,padx=0,pady=0, height=15,bg="black", width=13,relief=RIDGE)
tdo.grid(row = 0, column = 12, sticky = "ns")
tdo= Button(frame,state = DISABLED,padx=0,pady=0, height=15,bg="black", width=13,relief=RIDGE)
tdo.grid(row = 0, column = 13, sticky = "ns")
tdo= Button(frame,state = DISABLED,padx=0,pady=0, height=15,bg="black", width=13,relief=RIDGE)
tdo.grid(row = 0, column = 14, sticky = "ns")

#Bouton note
buttondo = Button(frame,padx=0, height=1,width=12, pady=0,bd=0,text="DO", bg="white",fg="black", command=lambda: jouerNote('DO'))
buttondo.grid(row = 0, column = 1,padx=5,pady=5,sticky = "ns")
buttonre = Button(frame,padx=0, height=1,width=12, pady=0,bd=0,text="RE", bg="white",fg="black", command=lambda: jouerNote('RE'))
buttonre.grid(row = 0, column = 2,padx=5,pady=5,sticky = "ns")
buttondmi = Button(frame,padx=0, height=1,width=12, pady=0,bd=0,text="MI", bg="white",fg="black", command=lambda: jouerNote('MI'))
buttondmi.grid(row = 0, column = 3,padx=5,pady=5,sticky = "ns")
buttondfa = Button(frame,padx=0, height=1,width=12, pady=0,bd=0,text="FA", bg="white",fg="black", command=lambda: jouerNote('FA'))
buttondfa.grid(row = 0, column = 4, padx=5,pady=5,sticky = "ns")
buttondsol = Button(frame,padx=0, height=1,width=12, pady=0,bd=0,text="SOL", bg="white",fg="black", command=lambda: jouerNote('SOL'))
buttondsol.grid(row = 0, column = 5,padx=5,pady=5, sticky = "ns")
buttondla = Button(frame,padx=0, height=1,width=12, pady=0,bd=0,text="LA", bg="white",fg="black", command=lambda: jouerNote('LA'))
buttondla.grid(row = 0, column = 6,padx=5,pady=5, sticky = "ns")
buttondsi = Button(frame,padx=0, height=1,width=12, pady=0,bd=0,text="SI", bg="white",fg="black", command=lambda: jouerNote('SI'))
buttondsi.grid(row = 0, column = 7,padx=5,pady=5, sticky = "ns")
buttondo1 = Button(frame,padx=0, height=1,width=12, pady=0,bd=0,text="DO", bg="white",fg="black", command=lambda: jouerNote('DO2'))
buttondo1.grid(row = 0, column = 8,padx=5,pady=5, sticky = "ns")
buttondo1 = Button(frame,padx=0, height=1,width=12, pady=0,bd=0,text="RE", bg="white",fg="black", command=lambda: jouerNote('RE2'))
buttondo1.grid(row = 0, column = 9,padx=5,pady=5, sticky = "ns")
buttondo1 = Button(frame,padx=0, height=1,width=12, pady=0,bd=0,text="MI", bg="white",fg="black", command=lambda: jouerNote('MI2'))
buttondo1.grid(row = 0, column = 10,padx=5,pady=5, sticky = "ns")
buttondo1 = Button(frame,padx=0, height=1,width=12, pady=0,bd=0,text="FA", bg="white",fg="black", command=lambda: jouerNote('FA2'))
buttondo1.grid(row = 0, column = 11,padx=5,pady=5, sticky = "ns")
buttondo1 = Button(frame,padx=0, height=1,width=12, pady=0,bd=0,text="SOL", bg="white",fg="black", command=lambda: jouerNote('SOL2'))
buttondo1.grid(row = 0, column = 12,padx=5,pady=5, sticky = "ns")
buttondo1 = Button(frame,padx=0, height=1,width=12, pady=0,bd=0,text="LA", bg="white",fg="black", command=lambda: jouerNote('LA2'))
buttondo1.grid(row = 0, column = 13,padx=5,pady=5, sticky = "ns")
buttondo1 = Button(frame,padx=0, height=1,width=12, pady=0,bd=0,text="SI", bg="white",fg="black", command=lambda: jouerNote('SI2'))
buttondo1.grid(row = 0, column = 14,padx=5,pady=5, sticky = "ns")
 

# boucle en attendant une action de l'utilisateur
mainloop()  