import pygame, random
# Let's import the Car Class
from car import Car

pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

SCREENWIDTH = 720
SCREENHEIGHT = 320

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")

#Background Code
background = pygame.image.load('C:\\Users\starw\Desktop\\background.png')

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()


playerCar = Car(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300

# Add the car to the list of objects
all_sprites_list.add(playerCar)

# Allowing the user to close the window...
carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        playerCar.moveLeft(5)
    if keys[pygame.K_d]:
        playerCar.moveRight(5)
    if keys[pygame.K_s]:
        playerCar.moveUp(5)
    if keys[pygame.K_w]:
        playerCar.moveDown(5)

    screen.blit(background, (0, 0))


    # Game Logic
    all_sprites_list.update()

    # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    all_sprites_list.draw(screen)

    # Refresh Screen
    pygame.display.flip()

    # Number of frames per secong e.g. 60
    clock.tick(60)


pygame.quit()


''' 
    # Drawing on Screen
    screen.fill(GREEN)
    # Draw The Road
    pygame.draw.rect(screen, GREY, [40, 0, 200, 300])
    # Draw Line painting on the road
    pygame.draw.line(screen, WHITE, [140, 0], [140, 300], 5)
'''