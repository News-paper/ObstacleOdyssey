import pygame
import sys


# to initialize the game we have to write init()
pygame.init()
# to get the viewing screen for the game we have to write this code 
# also we have to specify the height and the widht of the screen that we want
screen = pygame.display.set_mode((800, 500))

# Title and icon
pygame.display.set_caption("NiggaMan")

icon = pygame.image.load(black-man.png)
pygame.display.set_icon(icon)

# to display the screen
main = True
while main:
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit