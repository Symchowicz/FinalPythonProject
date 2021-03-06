from random import randint
from fonctions import *
import pygame

# from joueur import *

pygame.init()

class game:

    def __init__(self):

        self.player = player()
        self.is_running = True
        self.in_menu = True
        self.in_game = False
        self.in_choix_legends = False
        self.mouse = False
        self.son_hover = [False,False,False,False,False,False,False]
        self.musique = 0.5
        self.effet_sonore = 0.5
        self.luminosite = 100
        self.menu_parametre = False

        ## CONSTANTES MENU
        self.menu_regles = False
        self.menu_regles_page = 1
        self.parametres = False

        ## CONSTANTES CHOIX LEGENDS
        self.pret_J1 = False
        self.pret_J2 = False
        self.menu_legends_J1 = 0
        self.menu_legends_J2 = 0
        self.list_legends = ['bigband', 'isis', 'gunnar', 'kitt', 'harry', 'lucie']

        #INFOS LEGENDS
        self.infos_legends_j1 = False
        self.infos_legends_j2 = False

        ## CONSTANTES INGAME
        self.menu_pause = False
        self.tour = randint(0,1)
        self.round = [1,1]
        self.sujets = ["Ta mere", "Ton pere", "Ton créateur", "Ton homme", "Tes cheveux", "Tes vêtements", "Ta beauté", "Ton style", "Ton flow", "Tu", "Ta demarche", "Ta femme", "Ton odeur", "Ton âge", "Ta musique"]
        self.verbes = ["se battre", "être", "devenir", "ressembler à", "me rendre", "correspondre à", "ne pas être capable d'être", "me faire penser à"]
        self.complement = ["une chèvre", "un cochon", "un pigeon", "un vieux plouc", "une morue", "de l’eau", "une ratatouille", "moi", "toi", "un prisonnier", "à ma hauteur", "une paysanne", "un village", "une forêt", "un poulet rôti", "sourd", "fou", "si moche", "aveugle", "moche", "malade", "abominable", "un monstre", "un laboratoire"]
        self.liaison = ["pour", "et", "à l'image de", "comme", "et", "comme", "dans"]
        '''self.final = [",c'est repugnant ", ",quelle monstre ", ". Eloignez cette bete ", ", vieux plouc ", ", folichon va ", ", espece de marionette ", ", babolard a papa", ",sac a patate solitaire ", ", sale paysan "]'''

        self.sujetsref = ["Ta mere", "Ton pere", "Ton créateur", "Ton homme", "Tes cheveux", "Tes vêtements", "Ta beauté", "Ton style", "Ton flow", "Tu", "Ta demarche", "Ta femme", "Ton odeur", "Ton âge", "Ta musique"]
        self.verbesref = ["se battre", "être", "devenir", "ressembler à", "me rendre", "correspondre à", "ne pas être capable d'être", "me faire penser à"]
        self.complementref = ["une chèvre", "un cochon", "un pigeon", "un vieux plouc", "une morue", "de l’eau", "une ratatouille", "moi", "toi", "un prisonnier", "à ma hauteur", "une paysanne", "un village", "une forêt", "un poulet rôti", "sourd", "fou", "si moche", "aveugle", "moche", "malade", "abominable", "un monstre", "un laboratoire"]
        self.liaisonref = ["pour", "et", "à l'image de", "comme", "et", "comme", "dans"]
        '''self.finalref = [",c'est repugnant ", ",quelle monstre ", ". Eloignez cette bete ", ", vieux plouc ", ", folichon va ", ", espece de marionette ", ", babolard a papa", ",sac a patate solitaire ", ", sale paysan "]'''
        self.stage_select = None
        self.alpha = 300
        self.rect_utilise = [True,True,True,True,True,True,True,True,True,True,True,True]
        self.prop = []

        ### STATS DES LEGENDS
        self.stats = {
            'bigband': ('Musique', 'Laboratoire', 'Nourriture'),
            'gunnar': ('Famille', 'Lieux'),
            'harry': ('Pere','Animaux', 'Style'),
            'isis': ('Age', 'Style'),
            'kitt': ('Laboratoire', 'Musique', 'Eau'),
            'lucie': ('Famille', 'Age', 'Eau'),
        }
        self.faiblesse = {
            'Musique' : ("Ta musique", "abominable", "un monstre"),
            'Laboratoire' : ("Ton créateur",),
            'Style' : ("Tes cheveux", "Tes vêtements", "Ta beauté", "Ton style", "Ton flow","Ta démarche", "un monstre", "un vieu plouc", "une paysanne", "si moche/moches", "moche", "abominable",),
            'Famille' : ("Ta mère", "Ton père", "Ta femme", "Ton Homme",),
            'Age' : ("Ton age","un vieu plouc"),
            'Lieux' : ("village", "une forêt", "un laboratoire", "un prisonnier"),
            'Animaux' : ("une chèvre", "un cochon", "un pigeon", "une morue"),
            'Pere' : "Ton Pere",
            'Eau' : "de l'eau" ,
            'Nourriture' : ("un poulet rôti" , "une ratatouille",)
        }
        '''self.prop.append(self.sujets[x])
        self.prop.pop[x]'''

        ### IMAGE DU JEU
        self.image = {

            # Curseurs
            'image_curseur': pygame.image.load('assets/image/curseur.png'),
            'image_curseur_click': pygame.image.load('assets/image/curseur_click.png'),

            # Luminosité
            '80%' : pygame.image.load('assets/image/luminosite/80%.png'),
            '60%' : pygame.image.load('assets/image/luminosite/60%.png'),
            '40%' : pygame.image.load('assets/image/luminosite/40%.png'),
            '20%' : pygame.image.load('assets/image/luminosite/20%.png'),
            '0%' : pygame.image.load('assets/image/luminosite/0%.png'),


            ### MENU

                # Background
                'background_menu' : pygame.image.load('assets/image/menu principal/fond_menu.jpg'),

                # Boutons menu
                'bouton_jouer' : pygame.image.load('assets/image/menu principal/bouton_jouer.png'),
                'bouton_regles' : pygame.image.load('assets/image/menu principal/bouton_regles.png'),
                'bouton_parametres' : pygame.image.load('assets/image/menu principal/bouton_parametres.png'),
                'bouton_quitter' : pygame.image.load('assets/image/menu principal/bouton_quitter.png'),

                # Boutons menu hover
                'bouton_jouer_hover' : pygame.image.load('assets/image/menu principal/bouton_jouer_hover.png'),
                'bouton_regles_hover' : pygame.image.load('assets/image/menu principal/bouton_regles_hover.png'),
                'bouton_parametres_hover' : pygame.image.load('assets/image/menu principal/bouton_parametres_hover.png'),
                'bouton_quitter_hover' : pygame.image.load('assets/image/menu principal/bouton_quitter_hover.png'),

                # Images regles
                'fond_regles_1' : pygame.image.load('assets/image/menu principal/regles_1.png'),
                'fond_regles_2' : pygame.image.load('assets/image/menu principal/regles_2.png'),
                'fleche_regles_1' : pygame.image.load('assets/image/fleche_droite.png'),
                'fleche_regles_2' : pygame.image.load('assets/image/fleche_gauche.png'),
                'bouton_fermer' : pygame.image.load('assets/image/fermer.png'),

                # Images parametre
                'fond_parametre': pygame.image.load('assets/image/menu principal/parametres.png'),
                'plus': pygame.image.load('assets/image/plus.png'),
                'moins': pygame.image.load('assets/image/moins.png'),


            ### CHOIX LEGENDS

                # Background
                'background_menu_jouer': pygame.image.load('assets/image/Personnages/Menu/fond_choix_legends.jpg'),

                # Image statique
                'choisir': pygame.image.load('assets/image/Personnages/Menu/choisir.png'),

                # Bouton retour
                'bouton_retour': pygame.image.load('assets/image/Personnages/Menu/bouton_retour.png'),

                # Bouton dynamique
                'jouer_off': pygame.image.load('assets/image/Personnages/Menu/bouton_jouer_choix_legends.png'),
                'jouer_on': pygame.image.load('assets/image/Personnages/Menu/bouton_jouer_hover_choix_legends.png'),

                'pret_off': pygame.image.load('assets/image/Personnages/Menu/bouton_pret.png'),
                'pret_on': pygame.image.load('assets/image/Personnages/Menu/bouton_pret_hover.png'),

                # Bouton carrousel
                'fleche_droite': pygame.image.load('assets/image/fleche_droite.png'),
                'fleche_gauche': pygame.image.load('assets/image/fleche_gauche.png'),
                'fleche_droite_info': pygame.image.load('assets/image/Personnages/Menu/fleche_droite_or.png'),
                'fleche_gauche_info': pygame.image.load('assets/image/Personnages/Menu/fleche_gauche_or.png'),

                # Bouton cartes info
                "bouton_fermer_infos" : pygame.image.load('assets/image/Personnages/Menu/infos/fermer_infos.png'),
                "bouton_infos_j1" : pygame.image.load('assets/image/Personnages/Menu/infos/bouton_infos.png'),
                "bouton_infos_j2" : pygame.image.load('assets/image/Personnages/Menu/infos/bouton_infos.png'),

                ## Carte personnage

                    # Bigband
                    'bigband_J1_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/bigband_J1.png'),
                    'bigband_J1_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/bigband_selectionne_J1.png'),
                    'bigband_J2_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/bigband_J2.png'),
                    'bigband_J2_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/bigband_selectionne_J2.png'),

                    # Gunnar
                    'gunnar_J1_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/gunnar_J1.png'),
                    'gunnar_J1_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/gunnar_selectionne_J1.png'),
                    'gunnar_J2_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/gunnar_J2.png'),
                    'gunnar_J2_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/gunnar_selectionne_J2.png'),

                    # Harry
                    'harry_J1_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/harry_J1.png'),
                    'harry_J1_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/harry_selectionne_J1.png'),
                    'harry_J2_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/harry_J2.png'),
                    'harry_J2_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/harry_selectionne_J2.png'),

                    # Isis
                    'isis_J1_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/isis_J1.png'),
                    'isis_J1_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/isis_selectionnee_J1.png'),
                    'isis_J2_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/isis_J2.png'),
                    'isis_J2_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/isis_selectionnee_J2.png'),

                    # Kitt
                    'kitt_J1_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/kitt_J1.png'),
                    'kitt_J1_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/kitt_selectionnee_J1.png'),
                    'kitt_J2_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/kitt_J2.png'),
                    'kitt_J2_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/kitt_selectionnee_J2.png'),

                    # Lucie
                    'lucie_J1_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/lucie_J1.png'),
                    'lucie_J1_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/lucie_selectionnee_J1.png'),
                    'lucie_J2_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/lucie_J2.png'),
                    'lucie_J2_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/lucie_selectionnee_J2.png'),
                
                ## Infos personnages

                    'isis_infos' : pygame.image.load('assets/image/Personnages/Menu/infos/info_isis.png'),
                    'gunnar_infos' : pygame.image.load('assets/image/Personnages/Menu/infos/info_gunnar.png'),
                    'kitt_infos' : pygame.image.load('assets/image/Personnages/Menu/infos/info_kitt.png'),
                    'lucie_infos' : pygame.image.load('assets/image/Personnages/Menu/infos/info_lucie.png'),
                    'harry_infos' : pygame.image.load('assets/image/Personnages/Menu/infos/info_harry.png'),
                    'bigband_infos' : pygame.image.load('assets/image/Personnages/Menu/infos/info_bigband.png'),




            ### IN-GAME

                ## Personnage en jeu

                    # Bigband
                    'bigband_J1_1': pygame.image.load('assets/image/Personnages/Bigband/bigband_J1/Bigband_neutre_J1.png'),
                    'bigband_J1_2': pygame.image.load('assets/image/Personnages/Bigband/bigband_J1/Bigband_surpris_J1.png'),
                    'bigband_J1_3': pygame.image.load('assets/image/Personnages/Bigband/bigband_J1/Bigband_ombre_J1.png'),
                    'bigband_J1_4': pygame.image.load('assets/image/Personnages/Bigband/bigband_J1/Bigband_sourire_J1.png'),
                    'bigband_J1_5': pygame.image.load('assets/image/Personnages/Bigband/bigband_J1/Bigband_regard_intense_J1.png'),
                    'bigband_J2_1': pygame.image.load('assets/image/Personnages/Bigband/bigband_J2/Bigband_neutre_J2.png'),
                    'bigband_J2_2': pygame.image.load('assets/image/Personnages/Bigband/bigband_J2/Bigband_surpris_J2.png'),
                    'bigband_J2_3': pygame.image.load('assets/image/Personnages/Bigband/bigband_J2/Bigband_ombre_J2.png'),
                    'bigband_J2_4': pygame.image.load('assets/image/Personnages/Bigband/bigband_J2/Bigband_sourire_J2.png'),
                    'bigband_J2_5': pygame.image.load('assets/image/Personnages/Bigband/bigband_J2/Bigband_regard_intense_J2.png'),

                    # Gunnar
                    'gunnar_J1_1': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J1/Gunnar_neutre_J1.png'),
                    'gunnar_J1_2': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J1/Gunnar_reflexion_J1.png'),
                    'gunnar_J1_3': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J1/Gunnar_enerve_J1.png'),
                    'gunnar_J1_4': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J1/Gunnar_provocation_J1.png'),
                    'gunnar_J1_5': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J1/Gunnar_fourbe_J1.png'),
                    'gunnar_J2_1': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J2/Gunnar_neutre_J2.png'),
                    'gunnar_J2_2': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J2/Gunnar_reflexion_J2.png'),
                    'gunnar_J2_3': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J2/Gunnar_enerve_J2.png'),
                    'gunnar_J2_4': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J2/Gunnar_provocation_J2.png'),
                    'gunnar_J2_5': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J2/Gunnar_fourbe_J2.png'),

                    # Harry
                    'harry_J1_1': pygame.image.load('assets/image/Personnages/Harry/harry_J1/Harry_neutre_J1.png'),
                    'harry_J1_2': pygame.image.load('assets/image/Personnages/Harry/harry_J1/Harry_pose_J1.png'),
                    'harry_J1_3': pygame.image.load('assets/image/Personnages/Harry/harry_J1/Harry_geste_parler_J1.png'),
                    'harry_J1_4': pygame.image.load('assets/image/Personnages/Harry/harry_J1/Harry_fier_J1.png'),
                    'harry_J1_5': pygame.image.load('assets/image/Personnages/Harry/harry_J1/Harry_pose_sourire_J1.png'),
                    'harry_J2_1': pygame.image.load('assets/image/Personnages/Harry/harry_J2/Harry_neutre_J2.png'),
                    'harry_J2_2': pygame.image.load('assets/image/Personnages/Harry/harry_J2/Harry_pose_J2.png'),
                    'harry_J2_3': pygame.image.load('assets/image/Personnages/Harry/harry_J2/Harry_geste_parler_J2.png'),
                    'harry_J2_4': pygame.image.load('assets/image/Personnages/Harry/harry_J2/Harry_fier_J2.png'),
                    'harry_J2_5': pygame.image.load('assets/image/Personnages/Harry/harry_J2/Harry_pose_sourire_J2.png'),

                    # Isis
                    'isis_J1_1': pygame.image.load('assets/image/Personnages/Isis/isis_J1/Isis_neutre_J1.png'),
                    'isis_J1_2': pygame.image.load('assets/image/Personnages/Isis/isis_J1/Isis_regard_intense_J1.png'),
                    'isis_J1_3': pygame.image.load('assets/image/Personnages/Isis/isis_J1/Isis_transformation_J1.png'),
                    'isis_J1_4': pygame.image.load('assets/image/Personnages/Isis/isis_J1/Isis_rire_J1.png'),
                    'isis_J1_5': pygame.image.load('assets/image/Personnages/Isis/isis_J1/Isis_sourire_gene_J1.png'),
                    'isis_J2_1': pygame.image.load('assets/image/Personnages/Isis/isis_J2/Isis_neutre_J2.png'),
                    'isis_J2_2': pygame.image.load('assets/image/Personnages/Isis/isis_J2/Isis_regard_intense_J2.png'),
                    'isis_J2_3': pygame.image.load('assets/image/Personnages/Isis/isis_J2/Isis_transformee_J2.png'),
                    'isis_J2_4': pygame.image.load('assets/image/Personnages/Isis/isis_J2/Isis_rire_J2.png'),
                    'isis_J2_5': pygame.image.load('assets/image/Personnages/Isis/isis_J2/Isis_sourire_gene_J2.png'),

                    # Kitt
                    'kitt_J1_1': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J1/Kitt_1_J1.png'),
                    'kitt_J1_2': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J1/Kitt_12_J1.png'),
                    'kitt_J1_3': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J1/Kitt_10_J1.png'),
                    'kitt_J1_4': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J1/Kitt_4_J1.png'),
                    'kitt_J1_5': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J1/Kitt_6_J1.png'),
                    'kitt_J2_1': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J2/Kitt_1_J2.png'),
                    'kitt_J2_2': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J2/Kitt_12_J2.png'),
                    'kitt_J2_3': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J2/Kitt_10_J2.png'),
                    'kitt_J2_4': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J2/Kitt_4_J2.png'),
                    'kitt_J2_5': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J2/Kitt_6_J2.png'),

                    # Lucie
                    'lucie_J1_1': pygame.image.load('assets/image/Personnages/Lucie/lucie_J1/Lucie_neutre_J1.png'),
                    'lucie_J1_2': pygame.image.load('assets/image/Personnages/Lucie/lucie_J1/Lucie_blessee_aie_J1.png'),
                    'lucie_J1_3': pygame.image.load('assets/image/Personnages/Lucie/lucie_J1/Lucie_mort_J1.png'),
                    'lucie_J1_4': pygame.image.load('assets/image/Personnages/Lucie/lucie_J1/Lucie_sourire_J1.png'),
                    'lucie_J1_5': pygame.image.load('assets/image/Personnages/Lucie/lucie_J1/Lucie_controle_J1.png'),
                    'lucie_J2_1': pygame.image.load('assets/image/Personnages/Lucie/lucie_J2/Lucie_neutre_J2.png'),
                    'lucie_J2_2': pygame.image.load('assets/image/Personnages/Lucie/lucie_J2/Lucie_blessee_aie_J2.png'),
                    'lucie_J2_3': pygame.image.load('assets/image/Personnages/Lucie/lucie_J2/Lucie_mort_J2.png'),
                    'lucie_J2_4': pygame.image.load('assets/image/Personnages/Lucie/lucie_J2/Lucie_sourire_J2.png'),
                    'lucie_J2_5': pygame.image.load('assets/image/Personnages/Lucie/lucie_J2/Lucie_controle_J2.png'),

                ## Nuages de texte
                'nuage_J1' : pygame.image.load('assets/image/en_jeu/nuage_J1.png'),
                'nuage_J2' : pygame.image.load('assets/image/en_jeu/nuage_J2.png'),

                ## Background

                    #Isis
                    'isis_back' : pygame.image.load('assets/image/en_jeu/background/isis_background.jpg'),

                    #Bigband
                    'bigband_back' : pygame.image.load('assets/image/en_jeu/background/bigband_background.jpg'),

                    #K.I.T.T
                    'kitt_back' : pygame.image.load('assets/image/en_jeu/background/kitt_background.jpg'),

                    #Gunnar
                    'gunnar_back' : pygame.image.load('assets/image/en_jeu/background/gunnar_background.jpg'),

                    #Lucie
                    'lucie_back' : pygame.image.load('assets/image/en_jeu/background/lucie_background.jpg'),

                    #Harry
                    'harry_back' : pygame.image.load('assets/image/en_jeu/background/harry_background.jpg'),

                ## Menu Pause

                    'fond_menu_pause' : pygame.image.load('assets/image/en_jeu/menu_pause/fond_menu_pause.png'),
                    'bouton_reprendre' : pygame.image.load('assets/image/en_jeu/menu_pause/bouton_reprendre_pause.png'),
                    'bouton_reprendre_hover' : pygame.image.load('assets/image/en_jeu/menu_pause/bouton_reprendre_hover_pause.png'),
                    'bouton_reset' : pygame.image.load('assets/image/en_jeu/menu_pause/bouton_reset_pause.png'),
                    'bouton_reset_hover' : pygame.image.load('assets/image/en_jeu/menu_pause/bouton_reset_hover_pause.png'),
                    'bouton_retour_pause': pygame.image.load('assets/image/en_jeu/menu_pause/bouton_retour_pause.png'),
                    'bouton_retour_pause_hover': pygame.image.load('assets/image/en_jeu/menu_pause/bouton_retour_hover_pause.png'),
                    'bouton_parametres_pause': pygame.image.load('assets/image/en_jeu/menu_pause/bouton_parametres_pause.png'),
                    'bouton_parametres_pause_hover': pygame.image.load('assets/image/en_jeu/menu_pause/bouton_parametres_hover_pause.png'),
                    'bouton_quitter_pause': pygame.image.load('assets/image/en_jeu/menu_pause/bouton_quitter_pause.png'),
                    'bouton_quitter_pause_hover': pygame.image.load('assets/image/en_jeu/menu_pause/bouton_quitter_hover_pause.png'),

                ## Voulez-vous rejouer ?

                    'fond_end' : pygame.image.load('assets/image/en_jeu/end_game/fond_end.png'),
                    'non' : pygame.image.load('assets/image/en_jeu/end_game/non.png'),
                    'non_hover' : pygame.image.load('assets/image/en_jeu/end_game/non_hover.png'),
                    'oui' : pygame.image.load('assets/image/en_jeu/end_game/oui.png'),
                    'oui_hover' : pygame.image.load('assets/image/en_jeu/end_game/oui_hover.png'),

        }

        ### RECT DU JEU + Position

        self.rect_menu = {
            'bouton_jouer_hover_rect' : self.image['bouton_jouer_hover'].get_rect(),
            'bouton_regles_hover_rect' : self.image['bouton_regles_hover'].get_rect(),
            'bouton_parametres_hover_rect' : self.image['bouton_parametres_hover'].get_rect(),
            'bouton_quitter_hover_rect' : self.image['bouton_quitter_hover'].get_rect(),
            'bouton_fermer_rect' : self.image['bouton_fermer'].get_rect(),
            'bouton_regles_1' : self.image['fleche_regles_1'].get_rect(),
            'bouton_regles_2' : self.image['fleche_regles_2'].get_rect(),
            'moins_1' : self.image['moins'].get_rect(),
            'moins_2' : self.image['moins'].get_rect(),
            'moins_3' : self.image['moins'].get_rect(),
            'plus_1' : self.image['plus'].get_rect(),
            'plus_2' : self.image['plus'].get_rect(),
            'plus_3' : self.image['plus'].get_rect(),
            'bouton_fermer_parametre_rect': self.image['bouton_fermer'].get_rect(),
        }

        self.rect_position_menu ={
            'bouton_jouer_hover_rect': position_rect(self.rect_menu['bouton_jouer_hover_rect'], 664, 570),
            'bouton_regles_hover_rect': position_rect(self.rect_menu['bouton_regles_hover_rect'], 652, 651),
            'bouton_parametres_hover_rect': position_rect(self.rect_menu['bouton_parametres_hover_rect'], 606.5, 736),
            'bouton_quitter_hover_rect': position_rect(self.rect_menu['bouton_quitter_hover_rect'], 646, 811),
            'bouton_fermer_rect': position_rect(self.rect_menu['bouton_fermer_rect'], 1319, 465),
            'bouton_regles_1': position_rect(self.rect_menu['bouton_regles_1'], 1325, 902),
            'bouton_regles_2': position_rect(self.rect_menu['bouton_regles_2'], 1223, 902),
            'moins_1': position_rect(self.rect_menu['moins_1'], 625, 648),
            'moins_2': position_rect(self.rect_menu['moins_2'], 625, 761),
            'moins_3': position_rect(self.rect_menu['moins_3'], 625, 872),
            'plus_1': position_rect(self.rect_menu['plus_1'], 784, 647),
            'plus_2': position_rect(self.rect_menu['plus_2'], 784, 760),
            'plus_3': position_rect(self.rect_menu['plus_3'], 784, 871),
            'bouton_fermer_parametre_rect': position_rect(self.rect_menu['bouton_fermer_parametre_rect'], 1104, 456),
        }

        self.rect_choix_legends = {
            'jouer_rect': self.image['jouer_off'].get_rect(),
            'pret_rect_J1': self.image['pret_off'].get_rect(),
            'pret_rect_J2': self.image['pret_off'].get_rect(),
            'fleche_gauche_rect_J1': self.image['fleche_gauche'].get_rect(),
            'fleche_droite_rect_J1': self.image['fleche_droite'].get_rect(),
            'fleche_gauche_rect_J2': self.image['fleche_gauche'].get_rect(),
            'fleche_droite_rect_J2': self.image['fleche_droite'].get_rect(),
            'bouton_retour_rect': self.image['bouton_retour'].get_rect(),
            'bouton_infos_j1' : self.image['bouton_infos_j1'].get_rect(),
            'bouton_infos_j2' : self.image['bouton_infos_j2'].get_rect(),
            'bouton_fermer_infos_j1' : self.image['bouton_fermer_infos'].get_rect(),
            'bouton_fermer_infos_j2' : self.image['bouton_fermer_infos'].get_rect(),
        }
        self.rect_position_choix_legends = {
            'jouer_rect': position_rect(self.rect_choix_legends['jouer_rect'], 550, 452),
            'pret_rect_J1': position_rect(self.rect_choix_legends['pret_rect_J1'], 198, 900),
            'pret_rect_J2': position_rect(self.rect_choix_legends['pret_rect_J2'], 1028, 900),
            'fleche_gauche_rect_J1': position_rect(self.rect_choix_legends['fleche_gauche_rect_J1'], 105, 806),
            'fleche_droite_rect_J1': position_rect(self.rect_choix_legends['fleche_droite_rect_J1'], 465, 806),
            'fleche_gauche_rect_J2': position_rect(self.rect_choix_legends['fleche_gauche_rect_J2'], 935, 806),
            'fleche_droite_rect_J2': position_rect(self.rect_choix_legends['fleche_droite_rect_J2'], 1295, 806),
            'bouton_retour_rect': position_rect(self.rect_choix_legends['bouton_retour_rect'], 80, 20),
            'bouton_infos_j1' : position_rect(self.rect_choix_legends['bouton_infos_j1'], 100, 210),
            'bouton_infos_j2' : position_rect(self.rect_choix_legends['bouton_infos_j2'], 1305, 210),
            'bouton_fermer_infos_j1' : position_rect(self.rect_choix_legends['bouton_fermer_infos_j1'], 492, 204),
            'bouton_fermer_infos_j2' : position_rect(self.rect_choix_legends['bouton_fermer_infos_j2'], 926, 204),
        }

        self.rect_ingame = {
            'rect_1' : pygame.Rect(545,326,350, 44),
            'rect_2' : pygame.Rect(545,376,350, 44),
            'rect_3' : pygame.Rect(545,426,350, 44),
            'rect_4' : pygame.Rect(545,476,350, 44),
            'rect_5' : pygame.Rect(545,526,350, 44),
            'rect_6' : pygame.Rect(545,576,350, 44),
            'rect_7' : pygame.Rect(545,626,350, 44),
            'rect_8' : pygame.Rect(545,676,350, 44),
            'rect_9' : pygame.Rect(545,726,350, 44),
            'rect_10' : pygame.Rect(545,776,350, 44),
            'rect_11' : pygame.Rect(545,826,350, 44),
            'rect_12' : pygame.Rect(545,876,350, 44),
            'rect_13' : pygame.Rect(548,926,169, 44),
            'rect_14' : pygame.Rect(717,926,169, 44),
            'bouton_reprendre_hover_rect' : self.image['bouton_reprendre_hover'].get_rect(),
            'bouton_reset_hover_rect' : self.image['bouton_reset_hover'].get_rect(),
            'bouton_retour_pause_hover_rect' : self.image['bouton_retour_pause_hover'].get_rect(),
            'bouton_parametres_pause_hover_rect': self.image['bouton_parametres_pause_hover'].get_rect(),
            'bouton_quitter_pause_hover_rect': self.image['bouton_quitter_pause_hover'].get_rect(),
            'non_rect' : self.image['non'].get_rect(),
            'non_hover_rect' : self.image['non_hover'].get_rect(),
            'oui_rect' : self.image['oui'].get_rect(),
            'oui_hover_rect' : self.image['oui_hover'].get_rect(),

        }

        self.rect_position_ingame = {
            'bouton_reprendre_hover_rect': position_rect(self.rect_ingame['bouton_reprendre_hover_rect'], 632, 481),
            'bouton_reset_hover_rect': position_rect(self.rect_ingame['bouton_reset_hover_rect'], 532, 578),
            'bouton_retour_pause_hover_rect': position_rect(self.rect_ingame['bouton_retour_pause_hover_rect'], 583, 675),
            'bouton_parametres_pause_hover_rect': position_rect(self.rect_ingame['bouton_parametres_pause_hover_rect'], 621, 772),
            'bouton_quitter_pause_hover_rect': position_rect(self.rect_ingame['bouton_quitter_pause_hover_rect'], 646, 869),
            'non_hover_rect' : position_rect(self.rect_ingame['non_hover_rect'], 808, 425),
            'oui_hover_rect' : position_rect(self.rect_ingame['oui_hover_rect'], 550, 425),

        }

class player:
    def __init__(self):
        self.max_Hp_J1 = 500
        self.max_Hp_J2 = 500
        self.Hp_J1 = 500
        self.Hp_J2 = 500
        # barre de vie
        self.bar_position_J2 = [920, 20, self.max_Hp_J2, 50]
        self.bar_vie_J1 = (0, 204, 82)
        self.bar_vie_J2 = (0, 204, 82)
        self.legends_J1 = None
        self.legends_J2 = None
        self.faiblesse_J1 = None
        self.faiblesse_J2 = None
        self.p1_phrase = [[], False]
        self.p2_phrase = [[], False]
        self.score_J1 = 0
        self.score_J2 = 0

