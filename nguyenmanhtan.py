import pygame, random, sys, os, time
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TEXTCOLOR = (0, 150, 0)
BACKGROUNDCOLOR = (30, 80, 0)
FPS = 40
BADDIEMINSPEED =5
BADDIEMAXSPEED = 6
ADDNEWBADDIERATE = 16
PLAYERMOVERATE = 5
mang = 3
topScore=0

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # escape quits
                    terminate()
                return

def vacham(playerRect, phandien):
    for b in phandien:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#thiết lập pygame, cửa sổ và con trỏ chuột
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('the war!')
pygame.mouse.set_visible(True)

#thiet lap anh nhan vat
playerImage = pygame.image.load('anh1.png')
chaien3 = pygame.image.load('chaien3.png')
doremon4 = pygame.image.load('doremon4.png')
playerRect = playerImage.get_rect()
suneo2 = pygame.image.load('suneo2.png')
mauvat = [chaien3, doremon4, suneo2]
letrai = pygame.image.load('leftt.png')
lephai = pygame.image.load('rightt.png')

font = pygame.font.SysFont(None, 42)# thietlap font
drawText('YOU ARE THE BEST!', font, windowSurface, (WINDOWWIDTH / 2) - 137, (WINDOWHEIGHT / 3)+80)
pygame.display.update()
waitForPlayerToPressKey()

while (mang > 0):#thietlapbatdautrochoi
    phandien = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0

    while True: # vong lap tro choi chay trong khi dang choi
        score += 1

        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN:
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()

                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_UP:
                    moveUp = False
                if event.key == K_DOWN:
                    moveDown = False

                if event.key == K_SPACE:
                    time.sleep(2)

        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = 50
            newBaddie = {'rect': pygame.Rect(random.randint(120, 485), 0 - baddieSize, 23, 40),
                         'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface': pygame.transform.scale(random.choice(mauvat), (23, 40)),
                         }#pygame.Rect((left, top), (width, height))
            phandien.append(newBaddie)
            sideLeft = {'rect': pygame.Rect(0, 0, 110, 600),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface': pygame.transform.scale(letrai, (126, 599)),
                        }#scale(Surface, (width, height))
            phandien.append(sideLeft)
            sideRight = {'rect': pygame.Rect(500, 0, 303, 600),
                         'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface': pygame.transform.scale(lephai, (303, 599)),
                         }
            phandien.append(sideRight)

        #di chuyen ng choi xung quanh
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        for b in phandien:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        for b in phandien[:]:#xoa cac phan dien neu roi xuong duoi cung
            if b['rect'].top > WINDOWHEIGHT:
                phandien.remove(b)

        font = pygame.font.SysFont(None, 38)#thiet lap font
        windowSurface.fill(BACKGROUNDCOLOR)
        drawText(' diem: %s' % (score), font, windowSurface, 128, 0)
        drawText('diem cao nhat: %s' % (topScore), font, windowSurface, 128, 21)
        drawText('luot choi: %s' % (mang), font, windowSurface, 128, 41)

        windowSurface.blit(playerImage, playerRect)#draw rect cho ng choi

        for b in phandien :# draw tung nhan vat phan dien
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        if vacham(playerRect, phandien):
            if score > topScore:
                topScore = score
            break

        mainClock.tick(FPS)

    mang = mang - 1
    time.sleep(1)
    font = pygame.font.SysFont(None, 52)
    if (mang == 0):

        drawText('game over', font, windowSurface, (WINDOWWIDTH / 3)+40, (WINDOWHEIGHT / 3)+70)
        drawText('Press any key to play again.', font, windowSurface, (WINDOWWIDTH /3) - 110, (WINDOWHEIGHT / 3) + 95)
        pygame.display.update()
        time.sleep(2)
        waitForPlayerToPressKey()
        mang= 3