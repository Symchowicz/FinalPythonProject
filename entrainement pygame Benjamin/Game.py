import pygame
from classjoueur import joueur

pygame.init()

# donner le nom a la fenetre de jeu :
pygame.display.set_caption("Trouver un nom de jeu ")

# definir la taille de la fenetre :
fenetre = pygame.display.set_mode((1440, 1024))

Joueur = joueur()

running = True

# Choisir un background ( le background ici présent n'était qu'un test et n'est pas définitif )
background = pygame.image.load('assets/boxe.jpg')

while running:
    #chargement de background
    fenetre.blit(background, (-800, 50))

    #test chargement joueur

    fenetre.blit(Joueur.image, Joueur.rect)

    #permet de mettre a jour l'écran :
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()