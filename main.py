import pygame
import random
from Map import MapF
from Player import player
from Block import block

pygame.init()
pygame.display.set_caption("BlockPusher")
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

p1 = player()
b1 = [block(400, 400),block(400, 300)]


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

canMove = [True, True, True, True]

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
       [2,4,4,4,4,4,4,4,4,4,4,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2]]

blockBag = []


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
            p1.moves[0] = True
        if event.key == pygame.K_LEFT:
            keys[D] = False
            p1.moves[1] = True
        if event.key == pygame.K_UP:
            keys[W] = False
            p1.moves[2] = True
        if event.key == pygame.K_DOWN:
            keys[S] = False
            p1.moves[3] = True

    #physics section----------------------------------------------------------

    if mapNum == 1:
        p1.collision(map)
        for g in b1:
            g.Bcollision(map)
    elif mapNum == 2:
        p1.collision(map2)
        for g in b1:
            g.Bcollision(map2)


    for i in blockBag:
        i.move()

    
    
    #print(canMove[0])
    functs = []

    if mapNum == 1:
        for m in b1:
            m.NLCollision(map)
            functs.append(m.NLCollision(map))
            if all(functs):
                nextLVL = True
    if mapNum == 2:
         for m in b1:
            m.NLCollision(map2)
            # functs.append(m.NLCollision(map))
            # if all(functs):
            #     nextLVL = True

    #print(p1.direction)
    for m in b1:
        m.Pcollision(p1)

                
    print(p1.direction)
    

    if nextLVL == True :
        mapNum = 2

    if mapNum == 1:
        p1.move(keys , map)
    elif mapNum == 2:
        p1.move(keys , map2)


        #render section ---------------------------------------------------
    screen.fill((230,100,100))# Clear the screen pink

    if mapNum == 1:
        MapF(screen, map, blockBag)
        
    if mapNum == 2:
        MapF(screen, map2, blockBag)

    for i in range(len(b1)):
        b1[i].draw(screen)

    p1.draw(screen)
    
        

    pygame.display.flip()#this actually puts the pixel on the screen

    
pygame.quit()
