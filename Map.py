import pygame
from Block import block

Ground = pygame.image.load('Ground.png')
Ground1 = pygame.image.load('Ground1.png')

Lm = pygame.image.load('LandMine.png')

wall = pygame.image.load('Wall.png')
Door = pygame.image.load('MineEntrance.png')
water = pygame.image.load("Water2.png")
holding = pygame.image.load("Holder.png")
Button = pygame.image.load("switch.png")
ExplosionWall = pygame.image.load("TNT.png")
gholding = pygame.image.load("GHolder.png")


def MapF(screen, map, blockBeg):
    for i in range(12):
        for j in range(12):
            #ground-------------------------------
            if map[i][j] == 1:
                screen.blit(Ground, (j * 50, i * 50), (0, 0, 50, 50))
            elif map[i][j] == 8:
                screen.blit(Ground1, (j * 50, i * 50), (0, 0, 50, 50))

            
            elif map[i][j] == 2:
                screen.blit(wall, (j * 50, i * 50), (0, 0, 50, 50))
            elif map[i][j] == 3:
                screen.blit(Door, (j * 50, i * 50), (0, 0, 50, 50))

            elif map[i][j] == 4:
                screen.blit(Lm, (j * 50, i * 50), (0, 0, 50, 50))
            elif map[i][j] == 5:
                screen.blit(holding, (j * 50, i * 50), (0, 0, 50, 50))

            elif map[i][j] == 6:
                screen.blit(Button, (j * 50, i * 50), (0, 0, 50, 50))
            elif map[i][j] == 7:
                screen.blit(ExplosionWall, (j * 50, i * 50), (0, 0, 50, 50))
            elif map[i][j] == 9:
                screen.blit(gholding, (j * 50, i * 50), (0, 0, 50, 50))

            
