import pygame
from pygame import mixer

mixer.init()
ExplosionSF = pygame.mixer.Sound("BlockPushExplosion.mp3")
LandMineClick = pygame.mixer.Sound("BlockPushLM.mp3")
BlockColSF = pygame.mixer.Sound("POP.mp3")
TumbleColSf = pygame.mixer.Sound("TumbleSound.mp3")

Pblock = pygame.image.load('Barrel.png')
DarkPBlock = pygame.image.load("DarkBarrel.png")
Tumbleweed = pygame.image.load('Tumble.png')

explode = pygame.image.load("Explosion.png")
CMine = pygame.image.load("CollapsedMine.png")

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
        self.PlaySound = False
        
        self.showing_image = False
        self.image_start_time = 0
        self.image_stage = 0  # 0: nothing, 1: showing image1, 2: showing image2
        self.image_played = False  # New flag to track if animation played while on tile 3

        self.Wshowing_image = False
        self.Wimage_start_time = 0
        self.Wimage_stage = 0  # 0: nothing, 1: showing image1, 2: showing image2
        self.Wimage_played = False  # New flag to track if animation played while on tile 3

        self.dark = False



    def draw(self, screen):
        if self.dark == False:
            screen.blit(Pblock, (self.xPos, self.yPos))
        elif self.dark == True:
            screen.blit(DarkPBlock, (self.xPos, self.yPos))
        #pygame.draw.rect(screen, (200, 200, 200), (self.xPos, self.yPos, 50, 50))

    def move(self):
        self.xPos += self.vx
        self.yPos += self.vy

    def Pcollision(self, p1):
        if p1.x + 50 > self.xPos and p1.x<self.xPos+50 and p1.y +50 > self.yPos and p1.y < self.yPos+50 and self.walk == False:
                pygame.mixer.Sound.play(BlockColSF)
                BlockColSF.set_volume(0.2)
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
            if self.PlaySound == False:
                pygame.mixer.Sound.play(LandMineClick)
                LandMineClick.set_volume(0.5)
            self.PlaySound = True
        else:
            self.Button = False
        

    def ButtonCollision(self, screen, mapnum, current_time):
        for i in range(12):
            for j in range(12):
                if mapnum[i][j] == 7 and self.Button == True:
                    if self.Wimage_played == False and self.Wshowing_image == False:
                        self.Wshowing_image = True
                        self.Wimage_start_time = current_time
                    if self.Wshowing_image:
                        WTimePassed = current_time - self.Wimage_start_time
                        if WTimePassed < 1000:
                            screen.blit(explode, (j * 50, i * 50))
                            pygame.mixer.Sound.play(ExplosionSF)
                            ExplosionSF.set_volume(0.04)
                        else:
                            self.Button = False
                            mapnum[i][j] = 9
        

    def NLCollision(self, map):
        #if map[int(self.yPos / 50)][int((self.xPos + 50) / 50)] == 3 or map[int(self.yPos / 50)][int((self.xPos - 50)/ 50)] == 3 or map[int((self.yPos + 50) / 50)][int(self.xPos / 50)] == 3 or map[int((self.yPos - 50) / 50)][int(self.xPos / 50)] == 3:
                 # Check and assign x and y position based on where the "3" block is

        if map[int(self.yPos / 50)][int(self.xPos / 50)] == 4:
            pygame.mixer.Sound.play(LandMineClick)
            LandMineClick.set_volume(0.5)
            self.dark = True
        if map[int(self.yPos / 50)][int(self.xPos / 50)] == 4 or map[int(self.yPos / 50)][int(self.xPos / 50)] == 5:
            self.walk = True
            map[int(self.yPos / 50)][int(self.xPos / 50)] = 5
            return True
        elif map[int(self.yPos / 50)][int(self.xPos/ 50)] == 3:
            self.walk = True
            self.dark = False
            return True   
        else:
            self.walk = False
            return False
        
    def ExplosionAni(self, screen, map, current_time):

        # Only trigger once per entry into a '3' tile
        if map[int(self.yPos / 50)][int(self.xPos/ 50)] == 3:
            if self.image_played == False and self.showing_image == False:
                self.showing_image = True
                self.image_start_time = current_time
                self.image_played = True
        else:
            # Reset trigger when leaving the tile
            self.image_played = False

        # Handle image showing logic
        if self.showing_image:
            TimePassed = current_time - self.image_start_time

            if TimePassed < 1000:
                screen.blit(explode, (self.xPos, self.yPos))
                pygame.mixer.Sound.play(ExplosionSF)
                ExplosionSF.set_volume(0.04)
            elif TimePassed > 1000:
                screen.blit(CMine, (self.xPos, self.yPos))

    



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
        self.Playing = False


    def draw(self, screen):
        screen.blit(Tumbleweed, (self.xPos, self.yPos))

    def move(self):
        self.xPos += self.vx
        self.yPos += self.vy

    def PlayerCollision(self, p1):
        # Check if player and block are colliding
        if p1.x + 50 > self.xPos and p1.x < self.xPos + 50 and p1.y + 50 > self.yPos and p1.y < self.yPos + 50 and self.walk == False:
            pygame.mixer.Sound.play(TumbleColSf)
            TumbleColSf.set_volume(0.5)
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
