import pygame, sys #setup python

#create pygame window/ set resolution
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game')
screen = pygame.display.set_mode((800,800),0,32)

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

        screen.fill((0,0,0))
        draw_text('main menu', font, (255,255,255), screen, 20, 20)

        #allows draw_text to be pressed
        mx, my = pygame.mouse.get_pos()

        button_1=pygame.Rect(50,100,200,50)
        button_2=pygame.Rect(50,200,200,50)
        if button_1.collidepoint((mx,my)):
            if click:
                pass
        if button_2.collidepoint((mx,my)):
            if click:
                pass
        pygame.draw.rect(screen,(255,0,0), button_1)
        pygame.draw.rect(screen,(255,0,0), button_2)

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

def game():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
    pygame.display.update()
    mainClock.tick(60)

menu()
