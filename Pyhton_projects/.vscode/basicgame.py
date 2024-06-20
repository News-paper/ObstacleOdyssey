# to create a basic layout 
import pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Name")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

pygame.quit()

# to create a character
# Load the player image
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()

# Set the initial position of the player
player_rect.x = 100
player_rect.y = 100

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the player
    screen.blit(player_image, player_rect)

    # Update the display
    pygame.display.flip()

pygame.quit()

# to aadd a moment to the player
# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    # Draw the player
    screen.blit(player_image, player_rect)

    # Update the display
    pygame.display.flip()

pygame.quit()

# to create obticles so the that the player can experience collison and etc
# Load the obstacle image
obstacle_image = pygame.image.load("obstacle.png")
obstacle_rect = obstacle_image.get_rect()
obstacle_rect.x = 400
obstacle_rect.y = 300

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    # Check for collisions
    if player_rect.colliderect(obstacle_rect):
        # Handle collision (e.g., end game, reset player position)
        running = False

    # Draw the player and obstacle
    screen.blit(player_image, player_rect)
    screen.blit(obstacle_image, obstacle_rect)

    # Update the display
    pygame.display.flip()

pygame.quit()
