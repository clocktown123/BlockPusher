import pygame
from Map import MapF
from Player import player
from Block import block

pygame.init()
pygame.display.set_caption("top down grid map game")
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

p1 = player()
b1 = block()

A = 0
D = 1
W = 2
S = 3

keys = [False, False, False, False]


mxpos = 0
mypos = 0

mousePos = (mxpos, mypos)
mouseDown = False

ticker = 0

mapNum = 1

map = [[1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1]]

map2 = [[1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1]]


text_font = pygame.font.SysFont("Sans", 30, bold = True)

def draw_text(text, font, text_col, tx, ty):
    img = font.render(text, True, text_col)
    screen.blit(img, (tx, ty))

while True: #GAME LOOP######################################################
    clock.tick(60) # fps
    ticker+=1
    #input section--------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True


    if event.type == pygame.KEYDOWN:
             
        if event.key == pygame.K_RIGHT:
            keys[A] = True
        if event.key == pygame.K_LEFT:
            keys[D] = True
                #RowNum = 3
        if event.key == pygame.K_UP:
            keys[W] = True
                #RowNum = 1
        if event.key == pygame.K_DOWN:
            keys[S] = True
                #RowNum = 2

        
    if event.type == pygame.KEYUP:

        if event.key == pygame.K_RIGHT:
            keys[A] = False
                #RowNum = 0
        if event.key == pygame.K_LEFT:
            keys[D] = False
                #RowNum = 3
        if event.key == pygame.K_UP:
            keys[W] = False
                #RowNum = 1
        if event.key == pygame.K_DOWN:
            keys[S] = False
                #RowNum = 2

    #physics section----------------------------------------------------------

    # p1.collision(map)
    p1.BlockCollision(b1.xPos, b1.yPos)
    b1.move()

    if p1.x + 30 > b1.xPos and p1.x < b1.xPos + 50:
            if p1.y + 30 > b1.yPos and p1.y < b1.yPos:
                # Player is touching the box from below
                b1.yPos += 2  # Move the box down
                p1.y = b1.yPos - 30
            elif p1.y < b1.yPos +50 and p1.y + 30 > b1.yPos + 50:
                # Player is touching the box from above
                b1.yPos -= 2  # Move the box up
                p1.y = b1.yPos + 50

    if p1.y + 30 > b1.yPos and p1.y < b1.yPos + 50:
        if p1.x + 30 > b1.xPos and p1.x < b1.xPos:
            # Player is touching the box from the right
            b1.xPos += 2  # Move the box right
            p1.x = b1.xPos - 30
        elif p1.x < b1.xPos + 50 and p1.x + 30 > b1.xPos + 50:
            # Player is touching the box from the left
            b1.xPos -= 2  # Move the box left
            p1.x = b1.xPos + 50

    if mapNum == 1:
        p1.move(keys , map)
    #elif mapNum == 2:
        #p1.move(keys2 , map2)

        #render section ---------------------------------------------------
    screen.fill((230,100,100))# Clear the screen pink

    if mapNum == 1:
        MapF(screen, map)
        
    if mapNum == 2:
        MapF(screen, map2)

    p1.draw(screen)

    b1.draw(screen)

    pygame.display.flip()#this actually puts the pixel on the screen

    
pygame.quit()
