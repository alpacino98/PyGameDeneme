import pygame
import time
import random


disp_w = 800
disp_h = 1000

point = 0

x = 300
y = 799
w = 130
h = 200

colors = [(255,255,255), (255,0,0), (0,255,0), (0,0,255), (255,100,40), (100,40,255) ]

pygame.init()

myfont = pygame.font.SysFont("monospace", 15)


gameDisplay = pygame.display.set_mode((disp_w,disp_h))
pygame.display.set_caption('A Bit Racce')
clock = pygame.time.Clock()

crashed = False

def rect_create(x,y,w,h,color):
    pygame.draw.rect(gameDisplay, color, (x,y,w,h))
    pass

def full_rec(ran_colors, pos):
    x_w = [ (0, pos,199,200) , (200, pos,199,200), (400, pos,199,200), (600, pos,199,200) ]
    count = 0
    for i in x_w:
        pygame.draw.rect(gameDisplay, ran_colors[count], i)
        count += 1
    pass



level = 0
color_hold = random.choice(colors)
rect_create(x,y,w,h,color_hold)
ran_colors = []
initial = True
change = True
pos = -200
start = time.time()
while not crashed:
    gameDisplay.fill((0,0,0))


    if pos >= 1000:
        change = True
        pos = -200
        ran_colors = []

    if change or initial:
        ran_colors.append(color_hold)
        for i in range(3):
            ran_colors.append(random.choice(colors))
        random.shuffle(ran_colors)
        initial = False
        change = False

    full_rec(ran_colors, pos)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
    
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        x = x - 7
        if x < 0:
            x = x + 7
        player_rec = rect_create(x,y,w,h,color_hold)

    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        x = x + 7
        if x + 130 >= disp_w:
            x = 669
        player_rec = rect_create(x,y,w,h,color_hold)

    else:
        player_rec = rect_create(x,y,w,h,color_hold)

    if pos > 599:
        if x + w < 200:
            if ran_colors[0] == color_hold:
                point = point + 1
            else:
                crashed = True 
        
        elif x + w > 199 and x + w < 400:
            if ran_colors[1] == color_hold:
                point = point + 1
            else:
                crashed = True 
        
        elif x + w > 399 and x + w < 600:
            if ran_colors[2] == color_hold:
                point = point + 1
            else:
                crashed = True 

        elif x + w > 599:
            if ran_colors[3] == color_hold:
                point = point + 1
            else:
                crashed = True

        elif x + w > 0 and x + w < 400:
            if ran_colors[0] == ran_colors[1] == color_hold:
                point = point + 1
            else:
                crashed = True

        elif x + w > 200 and x + w < 600:
            if ran_colors[1] == ran_colors[2] == color_hold:
                point = point + 1
            else:
                crashed = True

        elif x + w > 400 and x + w < 800:
            if ran_colors[2] == ran_colors[3] == color_hold:
                point = point + 5
            else:
                crashed = True
        
        else:
            crashed = True 
        
    now = time.time()
    if point > 400 and point < 800:
        level = 1
        pos = pos + 12
    elif point >=800 and point < 1600:
        level = 2
        pos = pos + 24
    elif point >= 1600:
        level = 3
        pos = pos + 36
    else: 
        pos = pos + 10
    sent = "Points : "  + str(point)
    sent2 = "LEVEL :" + str(level)
    label = myfont.render(sent, 1, (0,255,0))
    label2 = myfont.render(sent2, 1, (0,255,0))
    gameDisplay.blit(label, (600, 50))
    gameDisplay.blit(label2, (50, 50))
    pygame.display.update()    
clock.tick(60)

pygame.quit()
quit()
