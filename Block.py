import pygame

Pblock = pygame.image.load('Barrel.png')
Tumbleweed = pygame.image.load('Tumble.png')

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
        self.Button = False


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
        
        if map[int(self.yPos / 50)][int((self.xPos + 50) / 50)] == 2 or map[int(self.yPos / 50)][int((self.xPos + 50) / 50)] == 7:  # Check the right side of the player
            self.right = False
        else: 
            self.right = True
        

        # LEFT
        if map[int(self.yPos / 50)][int((self.xPos - 50) / 50)] == 2 or map[int(self.yPos / 50)][int((self.xPos - 50) / 50)] == 7:  # Check the left side of the player
            self.left = False
        else:
            self.left = True

        #DOWN
        if map[int((self.yPos + 50) / 50)][int(self.xPos / 50)] == 2 or map[int((self.yPos + 50) / 50)][int(self.xPos / 50)] == 7:  # Check the bottom side of the player
            self.down = False
        else:
            self.down = True

        # UP
        if map[int((self.yPos - 50) / 50)][int(self.xPos / 50)] == 2 or map[int((self.yPos - 50) / 50)][int(self.xPos / 50)] == 7:  # Check the top side of the player
            self.up = False
        else:
            self.up = True

        if map[int(self.yPos / 50)][int(self.xPos/ 50)] == 6:
            self.Button = True
        else:
            self.Button = False
        

    def ButtonCollision(self, mapnum):
        for i in range(12):
            for j in range(12):
                if mapnum[i][j] == 7 and self.Button == True:
                    self.Button = False
                    mapnum[i][j] = 1
        

    def NLCollision(self, map):
        #if map[int(self.yPos / 50)][int((self.xPos + 50) / 50)] == 3 or map[int(self.yPos / 50)][int((self.xPos - 50)/ 50)] == 3 or map[int((self.yPos + 50) / 50)][int(self.xPos / 50)] == 3 or map[int((self.yPos - 50) / 50)][int(self.xPos / 50)] == 3:
                 # Check and assign x and y position based on where the "3" block is

        if map[int(self.yPos / 50)][int(self.xPos / 50)] == 4 or map[int(self.yPos / 50)][int(self.xPos / 50)] == 5:
            self.walk = True
            map[int(self.yPos / 50)][int(self.xPos / 50)] = 5
            return True
        elif map[int(self.yPos / 50)][int(self.xPos/ 50)] == 3:
            self.walk = True
            return True
            
        else:
            self.walk = False
            return False
        

class Farblock:
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
        self.col = False


    def draw(self, screen):
        screen.blit(Tumbleweed, (self.xPos, self.yPos))

    def move(self):
        self.xPos += self.vx
        self.yPos += self.vy

    def PlayerCollision(self, p1):
        # Check if player and block are colliding
        if p1.x + 50 > self.xPos and p1.x < self.xPos + 50 and p1.y + 50 > self.yPos and p1.y < self.yPos + 50 and self.walk == False:
            self.col = True
        if p1.direction == 2 and self.col == True:
            if self.up == True:
                self.yPos -=50
            else:
                self.yPos += 0
                self.col = False

        if p1.direction == 3 and self.col == True:
            if self.down == True:
                self.yPos += 50
            else:
                self.yPos += 0
                self.col = False

        if p1.direction == 1 and self.col == True:
            if self.left == True:
                self.xPos -=50
            else:
                self.xPos += 0
                self.col = False

        if p1.direction == 0 and self.col == True:
            if self.right == True:
                self.xPos += 50
            else:
                self.xPos += 0
                self.col = False



    def Bcollision(self, map):
        
        if map[int(self.yPos / 50)][int((self.xPos + 50) / 50)] == 2:  # Check the right side of the block
            self.right = False
        else: 
            self.right = True
        

        # LEFT
        if map[int(self.yPos / 50)][int((self.xPos - 50) / 50)] == 2:  # Check the left side of the block
            self.left = False
        else:
            self.left = True

        #DOWN
        if map[int((self.yPos + 50) / 50)][int(self.xPos / 50)] == 2:  # Check the bottom side of the block
            self.down = False
        else:
            self.down = True

        # UP
        if map[int((self.yPos - 50) / 50)][int(self.xPos / 50)] == 2:  # Check the top side of the block
            self.up = False
        else:
            self.up = True
        


            
        

    def NLCollision(self, map):
        #if map[int(self.yPos / 50)][int((self.xPos + 50) / 50)] == 3 or map[int(self.yPos / 50)][int((self.xPos - 50)/ 50)] == 3 or map[int((self.yPos + 50) / 50)][int(self.xPos / 50)] == 3 or map[int((self.yPos - 50) / 50)][int(self.xPos / 50)] == 3:
                 # Check and assign x and y position based on where the "3" block is
        if map[int(self.yPos / 50)][int(self.xPos/ 50)] == 3:
            self.walk = True
            return True
            
        else:
            self.walk = False
            return False
