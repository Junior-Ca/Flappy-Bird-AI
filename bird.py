import pygame
import os

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png"))), 
             pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png")))]

# represent the bird
class Bird:

    # Class Variables
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROTATION_VEL = 20
    ANIMATION_TIME = 5

    # intiatlize the bird
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    # the bird jumps up
    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y
    
    # movement of the bird
    def move(self):
        self.tick_count += 1

        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2

        # ensuring the bird doesn't acceleration down too fast
        if d >= 16:
            d = 16

        # ensuring the bird jumps up is faster
        if d < 0:
            d -= 2
        
        self.y = self.y + d
        
        # tilt bird upwards if going up
        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        
        # tilt bird downward if going down
        else:
            if self.tilt > -90:
                self.tilt -= self.ROTATION_VEL
    
    # display the bird flapping its wing
    def draw(self, window):
        self.img_count += 1

        # The image count determines the bird image state

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]

        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]

        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
            
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]

        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        # if the brid is tilting downward
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        # tilt the bird with with the image
        rotate_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotate_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        window.blit(rotate_image, new_rect.topleft)

    # get the mask of the bird to determine collision
    def get_mask(self):
        return pygame.mask.from_surface(self.img)