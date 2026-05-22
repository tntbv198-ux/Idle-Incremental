import pygame,numpy,os
from pygame.locals import * #type:ignore
from sys import exit
os.system("pip install pygame-ce numpy")
pygame.init()
info=pygame.display.Info()
width=info.current_w
height=info.current_h
screen=pygame.display.set_mode((width,height), pygame.RESIZABLE)
pygame.display.set_caption("Idle Incremental")
block=Rect(width-300,50,250,75)
button=Rect(width-300,200,250,75)
red=(255,0,0)
orange=(255,128,0)
yellow=(255,155,0)
green=(0,255,0)
turquoise=(0,255,125)
cyan=(0,255,255)
blue=(0,0,255)
purple=(255,0,128)
pink=(255,0,255)
white=(255,255,255)
score=0
price=15
perclick=1
buy=pygame.mixer.Sound("D:/Idle Incremental/Resources/Activate.mp3")
click=False
def text(size,text,color,x,y):
    global font
    font=pygame.font.Font("D:/Idle Incremental/Resources/BalsamiqSans-Bold.ttf",size)
    img=font.render(text,True,color)
    screen.blit(img,(x,y))
def drawrectandtext():
    global score,price,perclick
    pygame.draw.rect(screen,red,block,border_radius=15)
    pygame.draw.rect(screen,white,button,border_radius=15)
    text(50,"Welcome to Idle Incremental!",(255,255,255),500,360)
    text(24,"Red: "+str(int(price)),(255,255,255),1150,75)
    text(24,"Clicker!",(0,0,0),1150,225)
    text(36,"Score: "+str(int(score)),(255,255,255),150,180)
    text(36,"Per click: "+str(int(perclick)),(255,255,255),150,220)
def rectcollidemouse():
    global click,score,price,perclick
    if event.type==pygame.MOUSEBUTTONDOWN and not click:
        click=True
        while event.type==pygame.MOUSEBUTTONUP:
            if block.collidepoint(pos) and event.type!=pygame.MOUSEBUTTONDOWN:
                click=True
            if button.collidepoint(pos) and event.type!=pygame.MOUSEBUTTONDOWN:
                click=True
    if event.type==pygame.MOUSEBUTTONUP and click:
        click=False
        if block.collidepoint(pos):
            buy.play()
            score-=price
            price*=1.1
            perclick+=1
        if button.collidepoint(pos):
            score+=perclick
def draw():
    screen.fill("#272528")
    drawrectandtext()
def main():
    draw()
    rectcollidemouse()
fps,clock=60,pygame.time.Clock()
run=True
while run:
    pos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    main()
    clock.tick(fps)
    pygame.display.update()
pygame.quit()
exit()
