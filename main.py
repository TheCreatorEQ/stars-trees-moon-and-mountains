import math
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN
import random


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
circle_x = 200
circle_y = 0
sky = (0,20,80)
grass = (0,50,23)
road = (40,40,40)
star = (2,20,80)
leaf = (0,40,0)
trunk = (50,25,0)
snow = (140,140,140)
# ---------------------------

def tree(treepos, treesize, leaf, trunk):
    pygame.draw.rect(screen, trunk, [treepos[0], treepos[1], treesize, treesize])
    triW = treepos[0] - 2.5*treesize, treepos[1]
    triE = treepos[0] + 3.5*treesize, treepos[1]
    triN = treepos[0] + 0.5*treesize, treepos[1] - 4*treesize
    triW2 = treepos[0] - 2*treesize, treepos[1] - 2.5*treesize
    triE2 = treepos[0] + 3*treesize, treepos[1] - 2.5*treesize
    triN2 = treepos[0] + 0.5*treesize, treepos[1] - 6*treesize
    pygame.draw.polygon(screen, leaf, points=[triW,triE, triN])
    pygame.draw.polygon(screen, leaf, points=[triW2, triE2, triN2])


def moon(moonpos, moon, hole): #!!!!!!!!!!!!!!!
    holepos = list(moonpos)
    holepos[0] -=20
    holepos[1] +=10
    holepos = tuple(holepos)
    pygame.draw.circle(screen, moon, moonpos, 25)
    pygame.draw.circle(screen, hole, holepos, 25)


def create_star(starPos, color):
    starN = [(starPos[0]), starPos[1]+8]
    starNE = [(starPos[0]+2), starPos[1]+2]
    starE = [(starPos[0]+8), starPos[1]]
    starES = [(starPos[0]+2), starPos[1]-2]
    starS = [(starPos[0]), starPos[1]-8]
    starSW = [(starPos[0]-2), starPos[1]-2]
    starW = [(starPos[0]-8), starPos[1]]
    starWN = [(starPos[0]-2), starPos[1]+2]
    pygame.draw.polygon(screen, star, points=[tuple(starN),tuple(starNE),tuple(starE),tuple(starES),tuple(starS),tuple(starSW),tuple(starW),tuple(starWN)])

running = True
flag = False
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)

#---------------------------------------------------
    #Sky color
    change = list(sky)
    if circle_y <= 340:
        if circle_x <= 300:
            if change[0] != 60:
                change[0] += 1
            if change[1] != 200:
                change[1] += 2
            if change[2] != 240:
                change[2] += 2

    if circle_y <= 400:
        if circle_x >= 400 and circle_x <= 520:
            if change[0] != 0:
                change[0] -= 1
            if change[1] != 20:
                change[1] -= 1
            if change[2] != 80:
                change[2] -= 1
    else:
        change[0] = 0
        change[1] = 20
        change[2] = 80

    #grass color
    change1 = list(grass)
    if circle_y <= 340:
        if circle_x <= 320:
            if change1[1] != 154:
                change1[1] += 1

        if circle_y <= 400:
            if circle_x >= 420 and circle_x <= 520:
                if change1[1] != 50:
                    change1[1] -= 1
    #road color
    change2 = list(road)
    if circle_y <= 340:
        if circle_x <= 320:
            if change2[1] != 192:
                change2[0] += 2
                change2[1] += 2
                change2[2] += 2

        if circle_y <= 400:
            if circle_x >= 430 and circle_x <= 520:
                if change2[1] != 40:
                    change2[0] -= 2
                    change2[1] -= 2
                    change2[2] -= 2


    change4 = list(trunk)
    if circle_y <= 340:
        if circle_x <= 300:
            if change4[0] != 200:
                change4[0] += 1
            if change4[1] != 100:
                change4[1] += 1

    if circle_y <= 400:
        if circle_x >= 400 and circle_x <= 520:
            if change4[0] != 50:
                change4[0] -= 1
            if change4[1] != 25:
                change4[1] -= 1

    change5 = list(leaf)
    if circle_y <= 340:
        if circle_x <= 300:
            if change5[1] != 100:
                change5[1] += 1

    if circle_y <= 400:
        if circle_x >= 400 and circle_x <= 520:
            if change5[1] != 40:
                change5[1] -= 1


    change6 = list(snow)
    if circle_y <= 340:
        if circle_x <= 300:
            if change6[0] != 254:
                change6[0] += 2
            if change6[1] != 254:
                change6[1] += 2
            if change6[2] != 254:
                change6[2] += 2

    if circle_y <= 400:
        if circle_x >= 400 and circle_x <= 520:
            if change6[0] != 140:
                change6[0] -= 1
            if change6[1] != 140:
                change6[1] -= 1
            if change6[2] != 140:
                change6[2] -= 1



    sky = tuple(change)
    grass = tuple(change1)
    road = tuple(change2)
    trunk = tuple(change4)
    leaf = tuple(change5)
    snow = tuple(change6)

    #-------------------NEEDS WORK------------------
    change3 = list(star)
    if circle_y > 430:
        if circle_x >= 320:
            if change3[0] != 254:
                change3[0] += 2
            if change3[1] != 254:
                change3[1] += 2
            if change3[2] != 0:
                change3[2] -= 1

        if circle_x <= 320 and circle_x >= 160:
            if change3[0] != 0:
                change3[0] -= 2
            if change3[1] != 20:
                change3[1] -= 2
            if change3[2] != 80:
                change3[2] += 2

        star = tuple(change3)

    if circle_y <= 430:
        star = sky

    #_---------------------------------------------




#----------------------------------------------

    # Circle movement
    if circle_x == 520:
        flag = False
    elif circle_x == 120:
        flag = True
    if flag == False:
        circle_x -= 1
        circle_y = math.sqrt(40000 - (circle_x-320)**2) + 270
    else:
        circle_x += 1
        circle_y = 270 - math.sqrt(40000 - (circle_x-320)**2)
    #circle_y = math.sqrt(40000 - ((circle_x-320)**2)) + 240






    # DRAWING
    screen.fill(sky)  # always the first drawing command
    create_star((150,150), star)
    create_star((100,100), star)
    create_star((290, 122), star)
    create_star((451, 95), star)
    create_star((589, 173), star)
    create_star((311, 150), star)
    create_star((173, 54), star)
    create_star((32, 43), star)
    create_star((382, 39), star)
    create_star((605, 31), star)
    moon((510, 88), star, sky)
    pygame.draw.circle(screen, (255,255,0), (circle_x, circle_y), 25)
    pygame.draw.rect(screen, grass, [0, 330, 640, 150])
    pygame.draw.polygon(screen, road ,points=[(200, 480),(440, 480),(340, 330),(300, 330)])
    pygame.draw.polygon(screen, road ,points=[(5,329),(43,288),(65,294),(127,230),(174,271), (200,258),(250,329)])
    pygame.draw.polygon(screen, snow ,points=[(106, 252),(117, 264),(126, 254),(134, 261),(142, 254),(150, 261),(150, 250),(127,230)])
    pygame.draw.polygon(screen, snow ,points=[(212, 276),(195, 282),(194, 275),(181, 279),(178, 269),(200,258)])
    pygame.draw.polygon(screen, snow ,points=[(43,288),(31, 302),(35, 310),(50, 302),(55, 305),(56, 299),(66, 299),(63, 294)])


    tree((410, 358), 5, leaf, trunk)
    tree((472, 350), 5, leaf, trunk)
    tree((514, 346), 5, leaf, trunk)
    tree((562, 348), 5, leaf, trunk)
    tree((618, 358), 5, leaf, trunk)

    tree((368, 334), 5, leaf, trunk)
    tree((431, 333), 5, leaf, trunk)
    tree((594, 335), 5, leaf, trunk)
    tree((367, 353), 5, leaf, trunk)
    tree((280, 339), 5, leaf, trunk)

    tree((390, 385), 10, leaf, trunk)
    tree((250, 375), 10, leaf, trunk)
    tree((190, 449), 15, leaf, trunk)
    tree((429, 436), 15, leaf, trunk)



    # Must be the last two lines,(200,329),(200,329),(200,329)
    # of the game loop
    pygame.display.flip()
    clock.tick(60)
    #---------------------------


pygame.quit()
