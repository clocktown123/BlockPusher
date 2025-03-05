import pygame

Pblock = pygame.image.load('Block.png')

class block:
    def __init__(self):
        self.xPos = 450
        self.yPos = 450
        self.vx = 0
        self.vy = 0

    def draw(self, screen):
        screen.blit(Pblock, (self.xPos, self.yPos))
        #pygame.draw.rect(screen, (200, 200, 200), (self.xPos, self.yPos, 50, 50))

    def move(self):
        self.xPos += self.vx
        self.yPos += self.vy
