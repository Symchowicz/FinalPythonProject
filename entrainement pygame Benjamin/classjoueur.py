import pygame
pygame.init()

class joueur(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.pv = 100
        self.max_health = 100
        self.image = pygame.image.load('assets/akuma.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 350