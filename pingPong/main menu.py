import pygame, sys #setup python


#have it like google duo which has face in background with semi transparent grey

#create pygame window/ set resolution
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
icon = pygame.image.load('ping.png')
pygame.display.set_icon(icon)
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

        draw_text('main menu', font, (255,255,255), screen, 20, 20)

        #allows box to be pressed
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

#game
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
                    menu()
        pygame.display.update()

menu()
