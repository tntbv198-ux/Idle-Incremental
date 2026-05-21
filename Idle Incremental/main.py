import pygame,numpy
from sys import exit
pygame.init()
info=pygame.display.Info()
width=info.current_w
height=info.current_h
screen=pygame.display.set_mode((width,height), pygame.RESIZABLE)
pygame.display.set_caption("Idle Incremental")
font=pygame.font.Font("Idle Incremental/BalsamiqSans-Bold.ttf",30)
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
tick=0
def text(text,color,x,y):
    img=font.render(text,True,color)
    screen.blit(img,(x,y))
def draw():
    screen.fill("#272528")
fps,clock=60,pygame.time.Clock()
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    draw()
    text("Hello World!",(255,255,255),100,100)
    clock.tick(fps)
    pygame.display.update()
pygame.quit()
exit()
