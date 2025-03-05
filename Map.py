import pygame

brick = pygame.image.load('DBrick.png')
wall = pygame.image.load('Wall.png')

def MapF (screen, map):
    for i in range(12):
                for j in range(12):
                    if map[i][j] == 1:
                        screen.blit(brick, (j*50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 2:
                        screen.blit(wall, (j *50, i * 50), (0, 0, 50, 50))
