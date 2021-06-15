import pygame
from random import randint
import time

# initialize pygame
pygame.init()

WIDTH = 800
# set up our window display using pygame
WIN = pygame.display.set_mode((WIDTH, WIDTH))
# set a caption for the display
pygame.display.set_caption("Bubble Sort")

# color initialization
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# set background color
background = BLACK

# empty array of heights
height = []

# randomly generate array of 5 values, append to list
for i in range(5):
    height.append(randint(10, 750))

def show(height):
    # go through the array of heights and display the rectangle
    for i in range(len(height)):
        pygame.draw.rect(WIN, RED, (20 + 160 * i, height[i], 120, WIN.get_height() - height[i]))

def main():

    # the run is for the entire program, keep it on a loop
    run = True

    while run:

        # getting the keys which are pressed
        keys = pygame.key.get_pressed()

        # execute is to execute the bubble sort algorithm
        execute = False

        # QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # press space to execute
        if keys[pygame.K_SPACE]:
            execute = True

        if execute == False:
            WIN.fill(background)

            # call the show function, pass the randomly generated heights
            show(height)

            pygame.display.update()

        # if the execute flag is true
        else:
            # bubble sort algorithm
            for i in range(len(height) - 1):
                for j in range(len(height) - i - 1):
                    if height[j] < height[j+1]:
                        height[j], height[j+1] = height[j+1], height[j]

                    WIN.fill(background)
                    show(height)
                    pygame.time.delay(50)
                    pygame.display.update()

    pygame.quit()

main()