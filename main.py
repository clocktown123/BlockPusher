import pygame
import random
from Map import MapF
from Player import player
from Block import block

pygame.init()
pygame.display.set_caption("top down grid map game")
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

p1 = player()


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

nextLVL = False
nextLVLs2 = False

map = [[2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,3,1,2],
       [2,1,1,1,2,1,1,1,1,1,1,2],
       [2,1,1,1,2,1,1,1,1,1,1,2],
       [2,2,1,2,2,1,1,1,1,1,1,2],
       [2,1,1,1,2,1,1,1,1,1,1,2],
       [2,1,1,1,2,1,1,1,1,1,1,2],
       [2,1,1,1,2,1,1,1,1,1,1,2],
       [2,1,3,1,2,1,1,1,1,1,1,2],
       [2,1,1,1,2,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2]]

map2 = [[2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2]]


text_font = pygame.font.SysFont("Sans", 30, bold = True)

def draw_text(text, font, text_col, tx, ty):
    img = font.render(text, True, text_col)
    screen.blit(img, (tx, ty))

numBlocks = 2

blockBag = []
for i in range(numBlocks):
    blockBag.append(block(random.randrange(300, 450), random.randrange(150, 450)))

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
    for h in range(len(blockBag)):
        p1.BlockCollision(blockBag[h].xPos, blockBag[h].yPos)
        p1.BlockCollision(blockBag[h].xPos, blockBag[h].yPos)
    if mapNum == 1:
        p1.collision(map)
        for g in blockBag:
            g.Bcollision(map)
    elif mapNum == 2:
        p1.collision(map2)
        for g in blockBag:
            g.Bcollision(map2)


    for i in blockBag:
        i.move()

    functs = []

    if mapNum == 1:
        for p in range(len(blockBag)):
            blockBag[p].NLCollision(map)
            functs.append(blockBag[p].NLCollision(map))
            if all(functs):
                nextLVL = True

    for m in blockBag:
        if p1.x + 30 > m.xPos and p1.x < m.xPos + 50:
                if p1.y + 30 > m.yPos and p1.y < m.yPos:
                    # Player is touching the box from below7
                    m.yPos += 2  # Move the box down
                    p1.y = m.yPos - 30
                elif p1.y < m.yPos +50 and p1.y + 30 > m.yPos + 50:
                    # Player is touching the box from above
                    m.yPos -= 2  # Move the box up
                    p1.y = m.yPos + 50

        if p1.y + 30 > m.yPos and p1.y < m.yPos + 50:
            if p1.x + 30 > m.xPos and p1.x < m.xPos:
                # Player is touching the box from the right
                m.xPos += 2  # Move the box right
                p1.x = m.xPos - 30
            elif p1.x < m.xPos + 50 and p1.x + 30 > m.xPos + 50:
                # Player is touching the box from the left
                m.xPos -= 2  # Move the box left
                p1.x = m.xPos + 50


    # if p1.x + 30 > b2.xPos and p1.x < b2.xPos + 50:
    #         if p1.y + 30 > b2.yPos and p1.y < b2.yPos:
    #             # Player is touching the box from below
    #             b2.yPos += 2  # Move the box down
    #             p1.y = b2.yPos - 30
    #         elif p1.y < b2.yPos +50 and p1.y + 30 > b2.yPos + 50:
    #             # Player is touching the box from above
    #             b2.yPos -= 2  # Move the box up
    #             p1.y = b2.yPos + 50

    # if p1.y + 30 > b2.yPos and p1.y < b2.yPos + 50:
    #     if p1.x + 30 > b2.xPos and p1.x < b2.xPos:
    #         # Player is touching the box from the right
    #         b2.xPos += 2  # Move the box right
    #         p1.x = b2.xPos - 30
    #     elif p1.x < b2.xPos + 50 and p1.x + 30 > b2.xPos + 50:
    #         # Player is touching the box from the left
    #         b2.xPos -= 2  # Move the box left
    #         p1.x = b2.xPos + 50
    

    if nextLVL == True :
        mapNum = 2

    if mapNum == 1:
        p1.move(keys , map)
    elif mapNum == 2:
        p1.move(keys , map2)


        #render section ---------------------------------------------------
    screen.fill((230,100,100))# Clear the screen pink

    if mapNum == 1:
        MapF(screen, map)
        
    if mapNum == 2:
        MapF(screen, map2)

    p1.draw(screen)

    for k in blockBag:
        k.draw(screen)

    pygame.display.flip()#this actually puts the pixel on the screen

    
pygame.quit()
