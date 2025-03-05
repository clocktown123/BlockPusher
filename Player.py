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

    def draw(self, screen):
        pygame.draw.rect(screen, (150, 100, 100), (self.x, self.y, 30, 30))
    def move(self, keys, map):
        #print("true 2")
        #LEFT MOVEMENT
        if keys[A] == True:
            self.vx = 3
            self.direction = A
        #RIGHT MOVEMENT
        elif keys[D] == True:
            self.vx = -3
            self.direction = D
        #TURN OFF X VELOCITY
        else:
            self.vx = 0
        
        if keys[W] == True:
            self.vy = -3
            self.direction = W
        elif keys[S] == True:
            self.vy = 3
            self.direction = S
        else:
            self.vy = 0

        self.x += self.vx
        self.y += self.vy

    def BlockCollision(self, Bx, By):
        if self.x + 30 > Bx and self.x < Bx + 50:
            if self.y + 30 > By and self.y < By:
                # Player is touching the box from below
                By += 2  # Move the box down
            elif self.y < By +50 and self.y + 30 > By + 50:
                # Player is touching the box from above
                By -= 2  # Move the box up

        if self.y + 30 > By and self.y < By + 50:
            if self.x + 30 > Bx and self.x < Bx:
                # Player is touching the box from the right
                Bx += 2  # Move the box right
            elif self.x < Bx + 50 and self.x + 30 > Bx + 50:
                # Player is touching the box from the left
                Bx -= 2  # Move the box left



    def collision(self, map):

        if map[int(self.y / 50)][int((self.x + 30) / 50)] != 2:  # Check the right side of the player
            self.x += 3  # Move right if there's no block
        

        # LEFT
        if map[int(self.y / 50)][int(self.x / 50)] != 2:  # Check the left side of the player
            self.x -= 3  # Move left if there's no block

        # DOWN
        if map[int((self.y + 30) / 50)][int(self.x / 50)] != 2:  # Check the bottom side of the player
            self.y += 3  # Move down if there's no block

        # UP
        if map[int(self.y / 50)][int(self.x / 50)] != 2:  # Check the top side of the player
            self.y -= 3  # Move up if there's no block
        
        else:
            self.y += 0
            self.x += 0
