import pygame
import os
import random
from bird import Bird

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")))

class Pipe:
   
   # class variables
   GAP = 200 
   VEL = 5

   # initialize Pipe
   def __init__(self, x):
       self.x = x
       self.height = 0

       self.top = 0
       self.bottom = 0
       self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
       self.PIPE_BOTTOM = PIPE_IMG

       self.passed = False
       self.set_height()
    
   # setting up the height of the pipe
   def set_height(self):
        
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP
    
   # move the pipe
   def move(self):
       self.x -= self.VEL

   # draw both pipes
   def draw(self, window):
       window.blit(self.PIPE_TOP, (self.x, self.top))
       window.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

   # determine if the bird collided with the pipe
   def collide(self, bird):
       bird_mask = bird.get_mask()
       top_mask = pygame.mask.from_surface(self.PIPE_TOP)
       bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

       top_offset = (self.x - bird.x, self.top - round(bird.y))
       bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

       # checks pixel overlap between the bird mask and the pipe mask using the bottom offset
       b_point = bird_mask.overlap(bottom_mask, bottom_offset)
       t_point = bird_mask.overlap(top_mask, top_offset)

       # if the bird collided with the pipe 
       if t_point or b_point:
           return True

       return False