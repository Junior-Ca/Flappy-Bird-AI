import pygame
import os


pygame.font.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800
STAT_FONT = pygame.font.SysFont("comicsans", 30)

BACKGROUND_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))


def draw_window(window, birds, pipes, base, score, gen):
    window.blit(BACKGROUND_IMG, (0,0))

    for pipe in pipes:
        pipe.draw(window)
    
    text = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    window.blit(text, (WINDOW_WIDTH - 10 - text.get_width(), 10))

    text = STAT_FONT.render("Generation: " + str(gen), 1, (255,255,255))
    window.blit(text, (10, 10))

    base.draw(window)
    for bird in birds:
        bird.draw(window)

    pygame.display.update()