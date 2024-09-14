import pygame
import neat
import time
import os
import random
from bird import Bird
from pipe import Pipe
from base import Base
from utils import draw_window

# global variables
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800
GENERATION = 0
pygame.font.init()


def eval_genomes(genomes, config):
    global GENERATION
    GENERATION += 1
    nets = [] # neural network that control each bird
    ge = [] # genomes of the birds
    birds = []

    # set up the genome network
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        ge.append(g)


    base = Base(730)
    pipes = [Pipe(600)]
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    run = True

    score = 0

    clock = pygame.time.Clock()

    # game loop
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        pipe_index = 0

        # if there are birds
        if len(birds) > 0:

            # determine which pipe should count to the fitness score
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_index = 1

        # if there are no birds left
        else:
            run = False
            break

        # get the bird move on the screen
        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1

            # determine if the bird should jump or not
            output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_index].height), abs(bird.y - pipes[pipe_index].bottom)))
            
            if output[0] > 0.5:
                bird.jump()

        add_pipe = False
        remove = []
        for pipe in pipes:
            
            # for each birds within the generation
            for x, bird in enumerate(birds):

                # checks collision
                if pipe.collide(bird):

                    # lower the fitness score and remove the bird
                    ge[x].fitness -= 1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                # check if the bird went pass the pipe
                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True
                
            # checks if the pipe is off the screen
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove.append(pipe)

                
            pipe.move()

        # adds pipe
        if add_pipe:
            score += 1

            # increase fitness score when they make it through the pipe
            for g in ge:
                g.fitness += 5
            
            pipes.append(Pipe(600))
        
        # remove the pipe
        for r in remove:
            pipes.remove(r)

        # for each bird in each generation
        for x, bird in enumerate(birds):

            # if the bird hits the out of bounds, remove that bird
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)

        # if the bird reaches a certain amount of score, finish the generation
        if score > 50:
            run = False
            break
    
        base.move()
        draw_window(window, birds, pipes, base, score, GENERATION)

def run(config_path):

    # define all subheading in the config text file
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    population = neat.Population(config)

    # output stats of each generation
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    # set fitness generation it will run
    winner = population.run(eval_genomes,50)


if __name__ == "__main__":
    local_directory = os.path.dirname(__file__)
    config_path = os.path.join(local_directory, "config-feedforward.txt")
    run(config_path)