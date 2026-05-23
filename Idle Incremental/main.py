try:
    import pygame,numpy
except:
    print(f"Error: Can't startup because there're no modules this game.")
    print(f"Try to install using \"pip install <module> <module2> ...\".")
from pygame.locals import * #type:ignore
from sys import exit
pygame.init()
info=pygame.display.Info()
width=info.current_w
height=info.current_h
screen=pygame.display.set_mode((width,height), pygame.RESIZABLE)
pygame.display.set_caption("Idle Incremental")
block=Rect(width-300,50,250,75)
button=Rect(width-300,200,250,75)
red="#FF0000"
orange="#FF8000"
yellow="#FFFF00"
green="#00FF00"
turquoise="#00FF80"
cyan="#00FFFF"
blue="#0000FF"
purple="#8000FF"
pink="#FF00FF"
white="#FFFFFF"
score=0
price=10
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
            buttonclick(block)
            buttonclick(button)
    elif event.type==pygame.MOUSEBUTTONUP and click:
        click=False
        if block.collidepoint(pos):
            if score>=int(price):
                buy.play()
                score-=int(price)
                price*=1.1
                perclick+=1
        elif button.collidepoint(pos):
            score+=perclick
def notclick():
    global click
    click=False
    return
def buttonclick(button):
    global click
    if (not button.collidepoint(pos)) and event.type==pygame.MOUSEBUTTONDOWN and click:
        while (button.collidepoint(pos) and event.type==pygame.MOUSEBUTTONUP) or event.type==pygame.MOUSEBUTTONUP:
            if button.collidepoint(pos) and event.type==pygame.MOUSEBUTTONUP and click:
                notclick()
        notclick()
    elif button.collidepoint(pos) and event.type==pygame.MOUSEBUTTONDOWN and click:
        while not button.collidepoint(pos) and event.type==pygame.MOUSEBUTTONUP and click:
            notclick()
        if not button.collidepoint(pos):
            while not click and button.collidepoint(pos):
                notclick()
        elif not button.collidepoint(pos) and click:
            while event.type==pygame.MOUSEBUTTONUP:
                notclick()
            notclick()
        notclick()
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
