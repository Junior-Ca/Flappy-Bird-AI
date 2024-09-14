import pygame
import os

BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))

class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
    
    # the ground moves as the bird move
    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        # if the first image is out of the window, put it behind the second image
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        
        # if the second image is out of the window, put it behind the first image
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    # draw the ground
    def draw(self, window):
        window.blit(self.IMG, (self.x1, self.y))
        window.blit(self.IMG, (self.x2, self.y))