import pygame, random, Tank

pygame.init()
#Colors
white = (255, 255, 255)
black = (0, 0, 0)

red = (200, 0, 0)
light_red = (255, 0, 0)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)

#Screen setup
screenwidth = 500
screenheight = 500

size = (screenwidth, screenheight)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tank")
#puts all my sprites into a list for easy access
all_sprites_list = pygame.sprite.Group()

#creating first Tank
wolf = Tank(20, 30, red)

all_sprites_list.add(wolf)

carryOn = True
clock = pygame.time.Clock()

while carryOn:
    #Option to keep the game going or quit out at anytime
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.kkey == pygame.k_z:
                carryOn == False
    #setting up the tank movements for Wolf
    keys = pygame.kket.get_pressed()
    if keys[pygame.K_UP]:
        wolf.moveUp(5)
    if keys[pygame.K_DOWN]:
        wolf.moveDown(5)
        
    #screen.blit(background, (0,0))     #You need to make a backkground and put this in

    all_sprites_list.update()

    #Draws all the sprites at the same time
    all_sprites_list.draw(screen)

    #Refreshing Screen
    pygame.display.flip()

    #FPS is 60 for optimal use
    clock.tick(60)

pygame.quit()

