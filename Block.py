import pygame

Pblock = pygame.image.load('Block.png')

class block:
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y
        self.vx = 0
        self.vy = 0

    def draw(self, screen):
        screen.blit(Pblock, (self.xPos, self.yPos))
        #pygame.draw.rect(screen, (200, 200, 200), (self.xPos, self.yPos, 50, 50))

    def move(self):
        self.xPos += self.vx
        self.yPos += self.vy

    def Bcollision(self, map):

        if map[int(self.yPos / 50)][int((self.xPos + 48) / 50)] != 2:  # Check the right side of the player
            self.xPos += 3  # Move right if there's no block
        
        # LEFT
        if map[int(self.yPos / 50)][int(self.xPos / 50)] != 2:  # Check the left side of the player
            self.xPos -= 3  # Move left if there's no block

        # DOWN
        if map[int((self.yPos + 48) / 50)][int(self.xPos / 50)] != 2:  # Check the bottom side of the player
            self.yPos += 3  # Move down if there's no block

        # UP
        if map[int(self.yPos / 50)][int(self.xPos / 50)] != 2:  # Check the top side of the player
            self.yPos -= 3  # Move up if there's no block
            
        else:
            self.yPos += 0
            self.xPos += 0

    def NLCollision(self, map):
        if map[int(self.yPos / 50)][int((self.xPos + 50) / 50)] == 3 or map[int(self.yPos / 50)][int(self.xPos / 50)] == 3 or map[int((self.yPos + 50) / 50)][int(self.xPos / 50)] == 3 or map[int(self.yPos / 50)][int(self.xPos / 50)] == 3:
                 # Check and assign x and y position based on where the "3" block is
            if map[int(self.yPos / 50)][int((self.xPos + 50) / 50)] == 3:
                self.xPos = int((self.xPos + 50) / 50) * 50  # Set xPos to the column of the "3" block
                self.yPos = int(self.yPos / 50) * 50  # Set yPos to the row of the "3" block
                return True
            
            elif map[int(self.yPos / 50)][int(self.xPos / 50)] == 3:
                self.xPos = int(self.xPos / 50) * 50  # Set xPos to the column of the "3" block
                self.yPos = int(self.yPos / 50) * 50  # Set yPos to the row of the "3" block
                return True

            elif map[int((self.yPos + 50) / 50)][int(self.xPos / 50)] == 3:
                self.xPos = int(self.xPos / 50) * 50  # Set xPos to the column of the "3" block
                self.yPos = int((self.yPos + 50) / 50) * 50  # Set yPos to the row of the "3" block
                return True

            elif map[int(self.yPos / 50)][int(self.xPos / 50)] == 3:
                self.xPos = int(self.xPos / 50) * 50  # Set xPos to the column of the "3" block
                self.yPos = int(self.yPos / 50) * 50  # Set yPos to the row of the "3" block
                return True
