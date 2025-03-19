import pygame

A = 0
D = 1
W = 2
S = 3

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

    def draw(self, screen):
        pygame.draw.rect(screen, (150, 100, 100), (self.x, self.y, 50, 50))
    def move(self, keys, map):
        #print("true 2")
        #LEFT MOVEMENT
        if keys[A] == True and self.moves[0] == True and self.right == True:
            self.vx = 50
            self.direction = A
            self.moves[0] = False
        #RIGHT MOVEMENT
        elif keys[D] == True and self.moves[1] == True and self.left == True:
            self.vx = -50
            self.direction = D
            self.moves[1] = False
        #TURN OFF X VELOCITY
        else:
            self.vx = 0
        
        if keys[W] == True and self.moves[2] == True and self.up == True:
            self.vy = -50
            self.direction = W
            self.moves[2] = False
        elif keys[S] == True and self.moves[3] == True and self.down == True:
            self.vy = 50
            self.direction = S
            self.moves[3] = False
        else:
            self.vy = 0

        self.x += self.vx
        self.y += self.vy



    def collision(self, map):

        if map[int(self.y / 50)][int((self.x + 50) / 50)] == 2:  # Check the right side of the player
            self.right = False
        else: 
            self.right = True
        

        # LEFT
        if map[int(self.y / 50)][int((self.x - 50) / 50)] == 2:  # Check the left side of the player
            self.left = False
        else:
            self.left = True

        #DOWN
        if map[int((self.y + 50) / 50)][int(self.x / 50)] == 2:  # Check the bottom side of the player
            self.down = False
        else:
            self.down = True

        # UP
        if map[int((self.y - 50) / 50)][int(self.x / 50)] == 2:  # Check the top side of the player
            self.up = False
        else:
            self.up = True
        
        # else:
        #     self.y += 0
        #     self.x += 0
