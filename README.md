# Flappy Bird AI

This project is a Flappy Bird clone powered by a Neural Network using the NEAT-Python library. The goal is to evolve a population of birds that can learn to navigate through obstacles (pipes) by jumping at the right time. Each bird is controlled by its own neural network, which takes inputs like the bird’s position and the distance to the pipes. The birds with better performance (measured by how far they travel without hitting a pipe) have a higher chance of passing their neural network's weights to the next generation. Over time, the birds improve and learn to navigate the game more effectively through the process of evolution.

## How it Works
This game uses the NEAT (NeuroEvolution of Augmenting Topologies) algorithm to evolve neural networks. Here's how the process works:
1. Birds: Each generation consists of several birds, each controlled by its own neural network.
2. Pipes: The pipes are randomly generated and move towards the bird.
3. Fitness Function: The fitness of each bird is determined by how far the bird moves through the pipes without colliding.
4. Neural Network: The network receives inputs such as the bird's height and the position of the closest pipe and decides whether to jump or not.
5. Evolution: Birds with better fitness are more likely to pass on their genes (neural network weights) to the next generation. Over time, birds learn to avoid pipes more effectively.

## Installation
### Requirements
To run this project, you need the following Python packages:
+ **pygame**: A set of Python modules designed for writing video games
+ **neat-python**: A Python implementation of the NEAT (NeuroEvolution of Augmenting Topologies) algorithm
<br/><br/>To install the required libraries, run: 
`pip install pygame neat-python`

## How to Run
1. Clone this repository or download the source files.
2. Ensure you have the necessary images in the images/ folder.
3. Run the main.py file to start the game:
`python main.py`

