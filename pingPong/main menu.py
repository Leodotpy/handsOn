import pygame, sys #setup python
import cv2, time

#have it like google duo which has face in background with semi transparent grey

#create pygame window/ set resolution
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game')
screenw, screenh = 800,800
screen = pygame.display.set_mode((screenw,screenh),0,32)


mainClock.tick(60)

#font
font = pygame.font.SysFont(None, 20)

#box
def draw_text (text, font, colour, surface, x, y):
    textobj = font.render(text,1,colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

click = False

def menu():
    while True:

        wCam, hCam = 800,800

        #screen.fill((97,97,97))
        cap=cv2.VideoCapture(0)
        cap.set(3,wCam)
        cap.set(4,hCam)

    while True:
        success, img = cap.read()
        cv2.imshow("Image",img)
        cv2.waitKey(1)

        draw_text('main menu', font, (255,255,255), screen, 20, 20)

        #allows draw_text to be pressed
        mx, my = pygame.mouse.get_pos()

        button_1=pygame.Rect(310,int(screenw/2),200,75)

        if button_1.collidepoint((mx,my)):
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            if click:
                game()
        else:
            pygame.mouse.set_cursor(*pygame.cursors.diamond)

        pygame.draw.rect(screen,(255,0,0), button_1)


        click = False
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button ==1:
                    click=True
        pygame.display.flip()

def game():
    running = True
    while running:
        screen.fill((255,0,0))

        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()

menu()
