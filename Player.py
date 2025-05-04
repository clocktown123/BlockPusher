import pygame
from pygame import mixer

mixer.init()

A = 0
D = 1
W = 2
S = 3

cowboy = pygame.image.load('CowboySprite.png') #load your spritesheet
cowboy.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

ExplosionSF = pygame.mixer.Sound("BlockPushExplosion.mp3")
explode = pygame.image.load("Explosion.png")

class player:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.vx = 0
        self.vy = 0
        self.direction = W
        self.moves = [True, True, True, True]
        self.right = True
        self.left = True
        self.up = True
        self.down = True
        self.isAlive = True

        self.frameWidth = 50
        self.frameHeight = 50
        self.RowNum = 2 #for left animation, this will need to change for other animations
        self.frameNum = 0

        self.showing_image = False
        self.image_start_time = 0
        self.image_stage = 0  # 0: nothing, 1: showing image1, 2: showing image2
        self.image_played = False  # New flag to track if animation played while on tile 3

    def draw(self, screen):
        screen.blit(cowboy, (self.x, self.y), (self.frameWidth*self.frameNum, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight)) 
    def move(self, keys, map):
        #print("true 2")
        #LEFT MOVEMENT
        if keys[A] == True and self.moves[0] == True and self.right == True:
            self.vx = 50
            self.direction = A
            self.moves[0] = False
            self.RowNum = 2
            self.frameNum += 1
            if self.frameNum > 3:
                self.frameNum = 0
        #RIGHT MOVEMENT
        elif keys[D] == True and self.moves[1] == True and self.left == True:
            self.vx = -50
            self.direction = D
            self.moves[1] = False
            self.RowNum = 1
            self.frameNum += 1
            if self.frameNum > 3:
                self.frameNum = 0
        #TURN OFF X VELOCITY
        else:
            self.vx = 0
        
        if keys[W] == True and self.moves[2] == True and self.up == True:
            self.vy = -50
            self.direction = W
            self.moves[2] = False
            self.RowNum = 3
            self.frameNum += 1
            if self.frameNum > 3:
                self.frameNum = 0
        elif keys[S] == True and self.moves[3] == True and self.down == True:
            self.vy = 50
            self.direction = S
            self.moves[3] = False
            self.RowNum = 0
            self.frameNum += 1
            if self.frameNum > 3:
                self.frameNum = 0
        else:
            self.vy = 0

        self.x += self.vx
        self.y += self.vy

    def ExplosionAni(self, screen, map, current_time):

        # Only trigger once per entry into a '3' tile
        if map[int(self.y / 50)][int(self.x/ 50)] == 4:
            if self.image_played == False and self.showing_image == False:
                self.showing_image = True
                self.image_start_time = current_time
                self.image_played = True
        else:
            # Reset trigger when leaving the tile
            self.image_played = False
            self.isAlive = True

        # Handle image showing logic
        if self.showing_image:
            TimePassed = current_time - self.image_start_time

            if TimePassed < 1000:
                screen.blit(explode, (self.x, self.y))
                pygame.mixer.Sound.play(ExplosionSF)
                ExplosionSF.set_volume(0.04)
            elif TimePassed > 1000:
                self.isAlive = False
                




    def collision(self, map):

        if map[int(self.y / 50)][int((self.x + 50) / 50)] == 2 or map[int(self.y / 50)][int((self.x + 50) / 50)] == 7:  # Check the right side of the player
            self.right = False
        else: 
            self.right = True
        

        # LEFT
        if map[int(self.y / 50)][int((self.x - 50) / 50)] == 2 or map[int(self.y / 50)][int((self.x - 50) / 50)] == 7:  # Check the left side of the player
            self.left = False
        else:
            self.left = True

        #DOWN
        if map[int((self.y + 50) / 50)][int(self.x / 50)] == 2 or map[int((self.y + 50) / 50)][int(self.x / 50)] == 7:  # Check the bottom side of the player
            self.down = False
        else:
            self.down = True

        # UP
        if map[int((self.y - 50) / 50)][int(self.x / 50)] == 2 or map[int((self.y - 50) / 50)][int(self.x / 50)] == 7:  # Check the top side of the player
            self.up = False
        else:
            self.up = True
        
        # if map[int(self.y / 50)][int(self.x / 50)] == 4:  # Check the top side of the player
        #     self.isAlive = False
        # else:
        #     self.isAlive = True
        # else:
        #     self.y += 0
        #     self.x += 0
