import pygame
import random
from Map import MapF
from Player import player
from Block import block, Farblock

pygame.init()
pygame.display.set_caption("BlockPusher")
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

p1 = player()
b1 = [block(100, 150),block(400, 400)]
b2 = [Farblock(200, 400)]


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

state = 1

startButton = False
Tutorial = False
Back = False


nextLVL = False
nextLVL2 = False
nextLVL3 = False
nextLVL4 = False
nextLVL5 = False

canMove = [True, True, True, True]

map = [[2,2,2,2,2,2,2,2,2,2,2,2],
       [2,8,1,1,1,1,1,1,1,1,8,2],
       [2,1,1,1,1,1,8,1,1,3,1,2],
       [2,1,1,1,2,1,1,1,1,1,1,2],
       [2,1,8,1,2,1,1,1,1,1,1,2],
       [2,2,1,2,2,1,1,8,1,1,1,2],
       [2,1,1,8,2,1,1,1,1,1,1,2],
       [2,1,1,1,2,1,1,1,1,1,1,2],
       [2,1,1,1,2,8,1,1,8,1,1,2],
       [2,1,3,1,2,1,1,1,1,1,1,2],
       [2,1,1,1,2,1,1,1,1,1,8,2],
       [2,2,2,2,2,2,2,2,2,2,2,2]]

map2 = [[2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,3,1,1,1,8,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,8,2],
       [2,1,8,1,2,1,1,2,1,1,1,2],
       [2,2,2,2,2,4,4,2,2,2,2,2],
       [2,1,1,1,2,1,1,2,1,1,1,2],
       [2,8,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,8,1,2],
       [2,1,1,1,1,8,1,1,1,1,1,2],
       [2,1,8,1,1,1,1,1,1,1,8,2],
       [2,2,2,2,2,2,2,2,2,2,2,2]]

map3 = [[2,2,2,2,2,2,2,2,2,2,2,2],
       [2,8,2,1,2,2,2,2,1,1,4,2],
       [2,1,1,1,8,1,1,1,8,1,2,2],
       [2,2,2,1,1,2,4,4,2,1,4,2],
       [2,3,1,1,4,4,2,2,1,8,2,2],
       [2,2,1,8,4,1,1,8,1,1,4,2],
       [2,4,1,1,1,8,1,1,1,1,2,2],
       [2,2,4,2,1,1,1,1,4,1,1,2],
       [2,8,2,1,1,1,2,1,1,1,8,2],
       [2,2,1,8,1,2,2,1,1,2,4,2],
       [2,4,4,4,2,4,2,4,2,2,2,2],
       [2,2,2,2,2,2,2,2,2,2,2,2]]

map4 = [[2,2,2,2,2,2,2,2,2,2,2,2],
        [2,6,8,1,1,1,7,1,1,1,1,2],
        [2,1,1,1,1,1,7,1,1,3,8,2],
        [2,1,1,8,1,1,7,1,1,1,1,2],
        [2,1,1,1,1,1,7,7,7,7,7,2],
        [2,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,8,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,8,1,1,2],
        [2,1,8,1,1,8,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,1,8,1,2],
        [2,1,1,8,1,1,1,1,1,1,1,2],
        [2,2,2,2,2,2,2,2,2,2,2,2]]

map5 = [[2,2,2,2,2,2,2,2,2,2,2,2],
        [2,3,2,1,1,7,1,1,4,4,4,2],
        [2,1,2,1,1,2,1,8,1,1,4,2],
        [2,1,1,8,2,2,6,1,4,1,4,2],
        [2,1,1,1,1,2,1,1,4,1,4,2],
        [2,1,8,1,1,2,4,1,4,8,4,2],
        [2,1,1,1,8,2,4,1,4,1,4,2],
        [2,1,1,2,2,2,4,1,4,1,1,2],
        [2,2,1,8,1,7,1,1,1,1,1,2],
        [2,1,1,1,1,2,4,1,4,1,4,2],
        [2,1,8,1,1,2,4,1,8,1,4,2],
        [2,2,2,2,2,2,2,2,2,2,2,2]]





blockBag = []


text_font = pygame.font.SysFont("Sans", 30, bold = True)
smol_text_font = pygame.font.SysFont("Sans", 20, bold = True)

def draw_text(text, font, text_col, tx, ty):
    img = font.render(text, True, text_col)
    screen.blit(img, (tx, ty))

gameover = False

while gameover == False: #GAME LOOP######################################################
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

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseDown = True
    if event.type == pygame.MOUSEBUTTONUP:
        mouseDown = False

    #physics section----------------------------------------------------------

    if mapNum == 1:
        p1.collision(map)
        for g in b1:
            g.Bcollision(map)
    elif mapNum == 2:
        p1.collision(map2)
        for g in b1:
            g.Bcollision(map2)
    elif mapNum == 3:
        p1.collision(map3)
        for g in b2:
            g.Bcollision(map3)
    elif mapNum == 4:
        p1.collision(map4)
        for g in b1:
            g.Bcollision(map4)

    elif mapNum == 5:
        p1.collision(map5)
        b1[0].Bcollision(map5)
        for g in b2:
            g.Bcollision(map5)
        

    if mapNum == 1:
        all_collisions = True  # Assume all collisions are True at the start
        
        for m in b1:
            m.NLCollision(map)
            if not m.NLCollision(map):  # If any collision is False, set the flag to False
                all_collisions = False
                #break  # No need to check further if one collision fails

        if all_collisions:  # If all were True, proceed
            nextLVL = True
            p1.x = 100
            p1.y = 400
    if mapNum == 2:
        all_collisions = True  # Assume all collisions are True at the start
        
        for m in b1:
            m.NLCollision(map2)
            if not m.NLCollision(map2):  # If any collision is False, set the flag to False
                all_collisions = False
                #break  # No need to check further if one collision fails

        if all_collisions:  # If all were True, proceed
            nextLVL2 = True
            p1.x = 100
            p1.y = 450
    if mapNum == 3:
        all_collisions = True  # Assume all collisions are True at the start
        
        for m in b2:
            m.NLCollision(map3)
            if not m.NLCollision(map3):  # If any collision is False, set the flag to False
                all_collisions = False
                #break  # No need to check further if one collision fails

        if all_collisions:  # If all were True, proceed
            nextLVL3 = True
            p1.x = 100
            p1.y = 450
            b1[0].xPos = 400
            b1[0].yPos = 150
            b1[1].xPos = 200
            b1[1].yPos = 400
            for m in b1:
                m.walk = False
    if mapNum == 4:
        all_collisions = True  # Assume all collisions are True at the start
        
        for m in b1:
            if m.NLCollision(map4) == True:  # If any collision is False, set the flag to False
                all_collisions = False
                #break  # No need to check further if one collision fails

        if all_collisions == False:  # If all were True, proceed
            b1[0].Button = False
            nextLVL4 = True
            b1[0].xPos = 450
            b1[0].yPos = 200
            b1[0].walk = False
            p1.x = 450
            p1.y = 100
            b2[0].xPos = 200
            b2[0].yPos = 400
            

    if mapNum == 5:
        all_collisions = True  # Assume all collisions are True at the start
        
        for m in b2:
            m.NLCollision(map5)
            if  m.NLCollision(map5):  # If any collision is False, set the flag to False
                all_collisions = False
                #break  # No need to check further if one collision fails

        if all_collisions == False:  # If all were True, proceed
            nextLVL5 = True


    if mapNum == 4:
        for m in b1:
            m.ButtonCollision(map4)

    elif mapNum == 5:
        for m in b1:
            m.ButtonCollision(map5)
            
        

    #print(p1.direction)
    if mapNum == 1 or mapNum == 2 or mapNum == 4:
        for m in b1:
            m.Pcollision(p1)
    elif mapNum == 3:
        for m in b2:
            m.PlayerCollision(p1)
    elif mapNum == 5:
        b1[0].Pcollision(p1)
        for m in b2:
            m.PlayerCollision(p1)

    print(mapNum)
    print(b1[0].Button)
                
    #print(p1.direction)
    

    if nextLVL == True :
        mapNum = 2
    if nextLVL2 == True:
        mapNum = 3
    if nextLVL3 == True:
        mapNum = 4
    if nextLVL4 == True:
        mapNum = 5
    if nextLVL5 == True:
        print("gj")


    # for i in b2:
    #     i.move()
    

    if mapNum == 1:
        p1.move(keys , map)
    elif mapNum == 2:
        p1.move(keys , map2)
    elif mapNum == 3:
        p1.move(keys, map3)
    elif mapNum == 4:
        p1.move(keys, map4)
    elif mapNum == 5:
        p1.move(keys, map5)
    
    #button collision---------------------------------------------------------------------------------

    if p1.isAlive == False:
        state = 1

    if state == 1:
        if mousePos[0]>300 and mousePos[0]<500 and mousePos[1]>300 and mousePos[1]<450:
            startButton = True
        else:
            startButton = False
        
        if mousePos[0]>100 and mousePos[0]<300 and mousePos[1]>300 and mousePos[1]<450:
            Tutorial = True
        else:
            Tutorial = False

        if startButton == True and mouseDown == True:
            state = 2
        if Tutorial == True and mouseDown == True:
            state = 3

    if state == 3:

        if mousePos[0]>200 and mousePos[0]<400 and mousePos[1]>450 and mousePos[1]<600:
            Back = True
        else:
            Back = False

        if Back == True and mouseDown == True:
            state = 1

    #render section -------------------------------------------------------------------------------

    if state == 1:
        screen.fill((230, 100, 100))

        if startButton == False:
            pygame.draw.rect(screen, (100, 230, 100), (300, 300, 200, 150))
        else:
            pygame.draw.rect(screen, (200, 250, 200), (300, 300, 200, 150))

        draw_text("Start", text_font, (0,0,0), 350, 350)

        if Tutorial == False:
            pygame.draw.rect(screen, (200, 20, 100), (100, 300, 200, 150))
        else:
            pygame.draw.rect(screen, (220, 20, 200), (100, 300, 200, 150))
        
        draw_text("Tutorial", text_font, (0,0,0), 150, 350)

        
    elif state == 2:
        screen.fill((230,100,100))# Clear the screen pink

        if mapNum == 1:
            MapF(screen, map, blockBag)
            
        if mapNum == 2:
            MapF(screen, map2, blockBag)

        if mapNum == 3:
            MapF(screen, map3, blockBag)
        
        if mapNum == 4:
            MapF(screen, map4, blockBag)

        if mapNum == 5:
            MapF(screen, map5, blockBag)
        
        if mapNum == 1 or mapNum == 2 or mapNum == 4:
            for i in range(len(b1)):
                b1[i].draw(screen)

        if mapNum == 3:
            for i in b2:
                i.draw(screen)

        if mapNum == 5:
            b1[0].draw(screen)
            for i in b2:
                i.draw(screen)


        p1.draw(screen)

    elif state == 3:
        screen.fill((245, 245, 220))
        
        draw_text("push barrels into mine entrances", smol_text_font, (0,0,0), 20, 50)
        draw_text("dodge landmines (those dark circles)", smol_text_font, (0,0,0), 20, 100)
        draw_text("tumble weeds wont stop moving until they hit a wall", smol_text_font, (0,0,0), 20, 150)
        draw_text("place barrels on red circles to open up areas", smol_text_font, (0,0,0), 20, 200)


        if Back == False:
            pygame.draw.rect(screen, (200, 20, 100), (200, 450, 200, 150))
        else:
            pygame.draw.rect(screen, (220, 20, 200), (200, 450, 200, 150))

        draw_text("Back", text_font, (0,0,0), 250, 500)
        

    pygame.display.flip()#this actually puts the pixel on the screen

    
pygame.quit()
