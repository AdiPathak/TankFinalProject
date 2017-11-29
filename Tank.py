import pygame

white = (255, 255, 255)

clock = pygame.time.Clock()

class Tank (pygame.sprite.Sprite):

    def __init__(self, height, width, color):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fil(white)
        self.image.set_colorkey(white)

        pygame.draw.rect(self.image, color, [0, 0 , width, height])

        self.rect = self.image.get_rect()

        def moveUp(self, pixels):
            self.rect.y += pixels
        def moveDown(self, pixels):
            self.rect.y -= pixels
        #def rotate(image, angle):

