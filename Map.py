import pygame
from Block import block

brick = pygame.image.load('DBrick.png')
wall = pygame.image.load('Wall.png')
Door = pygame.image.load('door.png')
lava = pygame.image.load("Lava.png")


def MapF(screen, map, blockBeg):
    for i in range(12):
        for j in range(12):
            if map[i][j] == 1:
                screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
            elif map[i][j] == 2:
                screen.blit(wall, (j * 50, i * 50), (0, 0, 50, 50))
            elif map[i][j] == 3:
                screen.blit(Door, (j * 50, i * 50), (0, 0, 50, 50))
            elif map[i][j] == 4:
                screen.blit(lava, (j * 50, i * 50), (0, 0, 50, 50))

