import pygame

Pblock = pygame.image.load('Block.png')

class block:
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y
        self.vx = 0
        self.vy = 0
        self.right = True
        self.left = True
        self.up = True
        self.down = True
        self.walk = False


    def draw(self, screen):
        screen.blit(Pblock, (self.xPos, self.yPos))
        #pygame.draw.rect(screen, (200, 200, 200), (self.xPos, self.yPos, 50, 50))

    def move(self):
        self.xPos += self.vx
        self.yPos += self.vy

    def Pcollision(self, p1):
        if p1.x + 50 > self.xPos and p1.x<self.xPos+50 and p1.y +50 > self.yPos and p1.y < self.yPos+50 and self.walk == False:
                if p1.direction == 2 and self.up == True:
                    self.yPos -= 50
                elif p1.direction == 2 and self.up == False:
                    print("down")
                    p1.y = self.yPos+50

                if p1.direction == 3 and self.down == True:
                    self.yPos += 50
                elif p1.direction == 3 and self.down == False:
                    print("up")
                    p1.y = self.yPos - 50
                    
                if p1.direction == 1 and self.left == True:
                    self.xPos -= 50
                elif p1.direction == 1 and self.left == False:
                    p1.x = self.xPos + 50
                    print("left")

                if p1.direction == 0 and self.right == True:
                    self.xPos += 50
                elif p1.direction == 0 and self.right == False:
                    print("right")
                    p1.x = self.xPos - 50


    def Bcollision(self, map):
        
        if map[int(self.yPos / 50)][int((self.xPos + 50) / 50)] == 2:  # Check the right side of the player
            self.right = False
        else: 
            self.right = True
        

        # LEFT
        if map[int(self.yPos / 50)][int((self.xPos - 50) / 50)] == 2:  # Check the left side of the player
            self.left = False
        else:
            self.left = True

        #DOWN
        if map[int((self.yPos + 50) / 50)][int(self.xPos / 50)] == 2:  # Check the bottom side of the player
            self.down = False
        else:
            self.down = True

        # UP
        if map[int((self.yPos - 50) / 50)][int(self.xPos / 50)] == 2:  # Check the top side of the player
            self.up = False
        else:
            self.up = True
        

            
        

    def NLCollision(self, map):
        #if map[int(self.yPos / 50)][int((self.xPos + 50) / 50)] == 3 or map[int(self.yPos / 50)][int((self.xPos - 50)/ 50)] == 3 or map[int((self.yPos + 50) / 50)][int(self.xPos / 50)] == 3 or map[int((self.yPos - 50) / 50)][int(self.xPos / 50)] == 3:
                 # Check and assign x and y position based on where the "3" block is

        if map[int(self.yPos / 50)][int((self.xPos + 50) / 50)] == 4:
            self.walk = True

        elif map[int(self.yPos / 50)][int(self.xPos/ 50)] == 3:
            self.walk = True
            return True
            
        # elif map[int(self.yPos / 50)][int((self.xPos - 50) / 50)] == 3:
        #     self.walk = True
        #     return True

        # elif map[int((self.yPos + 50) / 50)][int(self.xPos / 50)] == 3:
        #     self.walk = True
        #     return True

        # elif map[int((self.yPos - 50) / 50)][int(self.xPos / 50)] == 3:
        #     self.walk = True
        #     return True
            
        else:
            self.walk = False
            return False
