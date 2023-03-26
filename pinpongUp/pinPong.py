import pygame
from random import randint
import time 
pygame.init()
window = pygame.display.set_mode((500,500))
black = (0,128,0)
window.fill(black)
clock = pygame.time.Clock()

game_over = False
move_UP = False
move_DOWN = False
move_UP1 = False
move_DOWN1 = False
dx1 = 3.5
dy1 = 3.5

prom = input("Введіть ім'я першого гравця")
prom2 = input("Введіть ім'я другого гравця")
level = int(input("Введіть швидкість мяча від 1 до 10"))

if level == 0:
    level = int(input("Нуль це занадто легко!!!"))
if level == 1:
    dx = 1
    dy = 1
if level == 2:
    dx = 2
    dy = 2
if level ==3:
    dy = 3
    dx = 3
if level ==4:
    dx = 4
    dy = 4
if level == 5:
    dx = 5
    dy = 5
if level == 6:
    dy = 6
    dx = 6
if level == 7:
    dx = 7
    dy = 7
if level ==8:
    dx = 8
    dy = 8
if level ==9 :
    dx = 9
    dy = 9
if level ==10:
    dx = 10
    dy = 10


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        """ область: прямоугольник в нужном месте и нужного цвета """
        #запоминаем прямоугольник:
        self.rect = pygame.Rect(x, y, width, height)
        #цвет заливки - или переданный параметр, или общий цвет фона
        self.fill_color = black
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def colliderect(self,rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self ,filename,x = 0,y=0,width=10,height = 10):
        super().__init__(x=x,y=y,width=width,height=height,color = None)
        self.image = pygame.image.load(filename)

    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Label(Area):
    def set_text(self,text , frize=12 , text_color=(0,0,0)):
        
        self.image = pygame.font.SysFont("verdana", frize).render(text,True,text_color)
    def draw (self,shift_x=0,shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

start_time = time.time()
cur_time = start_time
point = 0
point1 = 0
score = Label(200,20,0,0,black)
score.set_text("0",45,(0,0,0))
score.draw(0,0)
score1 = Label(270,20,0,0,black)
score1.set_text("0",45,(0,0,0))
score1.draw(0,0)
point = 0
platform1 = Picture("pixil-frame-0 (8).png",-190,-50,5,115)
platform1.draw()
platform2 = Picture("pixil-frame-0 (9).png",257,-50,5,115)
platform2.draw()
ball = Picture("pixil-frame-0 (10).png",1,1,50,50)

lin = Picture("pixil-frame-0 (11).png",15,1)
lin.draw()




time_text = Label(0,0,0,0,black)
time_text.set_text('Час:',40,(0,0,0))
time_text.draw(20, 20)

gg2= list()
mist2 = 1 
gg = list()
mist = 1
gg1 = list()
mist1 = 1

mist3 = 1
gg3 = list()
for i in  range (mist):
    ball2 = Picture("pixil-frame-0 (15).png",1,1,27.5,27.5)
    gg.append(ball2)

for i in range(mist1):
    ball3 = Picture("pixil-frame-0 (15).png",1,1,27.5,27.5)
    gg1.append(ball3)

for i in range(mist2):
    ball4 = Picture("pixil-frame-0 (15).png",-1,-1,27.5,27.5)
    gg2.append(ball4)

for i in range(mist3):
    ball5 = Picture("pixil-frame-0 (15).png",-1,-1,27.5,27.5)
    gg3.append(ball5)



dx3 = 4.5
dy3 = 4.5

dx2 = 3
dy2 = 3

dx4 = 4
dy4 = 4

timer = Label(50,55,0,0,black)
timer.set_text("0",45,(0,0,0))
timer.draw(0,0)

lose = Label(170,30,0,0,black)
lose.set_text("Час Вийшов!!!",55,(255,0,0))

harding = Label(175,150,0,0,black)
harding.set_text("Ускладнення!!",30,(0,0,0))

while not game_over:
    platform1.fill()
    platform2.fill()
    ball.fill()
    window.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_UP = True
            if event.key == pygame.K_s:
                move_DOWN = True

            if event.key == pygame.K_UP:
                move_UP1 = True
            if event.key == pygame.K_DOWN:
                move_DOWN1 = True
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_UP = False
            if event.key == pygame.K_s:
                move_DOWN = False
            if event.key == pygame.K_UP:
                move_UP1 = False
            if event.key == pygame.K_DOWN:
                move_DOWN1 = False

    

    




    """Рух"""
    if move_UP:
        platform1.rect.y -= 4
    if move_DOWN:
        platform1.rect.y +=4
    if move_UP1:
        platform2.rect.y -= 4
    if move_DOWN1:
        platform2.rect.y +=4
    
    
    
    ball.rect.x += dx
    ball.rect.y += dy 
   
    if ball.rect.y >= 280 or ball.rect.y < -180:
        dy *= -1



    
    
    
    """рух """


    



    """Торкання"""
    if ball.rect.colliderect(platform1.rect):
        dx *= -1
    if ball.rect.colliderect(platform2.rect):
        dx *= -1

   
    
    


    if platform1.rect.y < -191.5:
        move_UP = False
    if platform1.rect.y > 280:
        move_DOWN = False

    
    if platform2.rect.y < -185:
        move_UP1 = False
    if platform2.rect.y > 280:
        move_DOWN1 = False

    if ball.rect.x > 330:
        point += 1
        score.set_text(str(point),40,(30,30,30))
        ball = Picture("pixil-frame-0 (10).png",1,1,50,50)
        
        
        score.draw(0,0)


    if ball.rect.x < -260 :
        point1 += 1
        score1.set_text(str(point1),40,(30,30,30))
        ball = Picture("pixil-frame-0 (10).png",1,1,50,50)
    
        score1.draw(0,0)

   

    """Торкання"""

    """Час"""
    new_time = time.time()
    if int(new_time) + int(cur_time) >= 1:#Лічильник з секундами
        timer.set_text(str(int(new_time - start_time)),40,(30,30,30))#Виводемо його на екран
        timer.draw(0,0)#Виводемо його
        cur_time = new_time
    
    
        """Виграш"""
    #Жовт
    if point == 10:
        win = Label(30,120,0,0,black)
        win.set_text(prom +" Виграв!",30,(0,0,0))
        
        kubok = Picture("pixil-frame-0 (12).png",-150,0)
        win.draw()
        kubok.draw()
        game_over = True

        #син
    if point1 == 10:
        win = Label(250,120,0,0,black)
        win.set_text(prom2 +" Виграв!",30,(0,0,0))
        
        kubok = Picture("pixil-frame-0 (12).png",25,0)
        win.draw()
        kubok.draw()
        game_over = True

    if new_time - start_time >= 300:
        lose.draw()
        game_over = True
        if point > point1:
            win = Label(30,120,50,50,black)
            win.set_text(prom +" Виграв!",30,(0,0,0))
        
            kubok = Picture("pixil-frame-0 (12).png",-150,0)
            win.draw()
            kubok.draw()
            
            game_over = True
            
        if point1 > point:
            win = Label(250,120,50,50,black)
            win.set_text(prom +" Виграв!",30,(0,0,0))
        
            kubok = Picture("pixil-frame-0 (12).png",25,0)
            win.draw()
            kubok.draw()
            game_over = True

        if point == point1:
            nv = Label(170,150,50,40,black)
            nv.set_text("Нічия!",55,(75,0,130))
            nv.draw()
            kubok = Picture("pixil-frame-0 (12).png",25,0)
            kubok1 = Picture("pixil-frame-0 (12).png",-200,0)
            kubok.draw()
            kubok1.draw()
            game_over = True


    """Події"""
   

    if new_time - start_time >= 20:
        black = (255,255,255)
        harding.draw()
    if new_time -start_time >= 40:
        black = (0,128,0)
        harding.set_text("Ускладнення!!",0,(0,0,0))
    
    
    if new_time - start_time >= 50:
        for p in gg:
            p.draw()
        
            ball2.rect.x += dx1
            ball2.rect.y += dy1
            if ball2.rect.y > 275 or ball2.rect.y < -220:
                dy1 *= -1
            if ball2.rect.colliderect(platform1.rect):
                dx1 *= -1
            if ball2.rect.colliderect(platform2.rect):
                dx1 *= -1

            if ball2.rect.x > 330:
                point += 1
                score.set_text(str(point),40,(30,30,30))
                ball2 = Picture("pixil-frame-0 (15).png",1,1,30,30)
                dy1 = 0
                dx1 = 0
            
            
            score.draw(0,0)


        if ball2.rect.x < -260 :
            point1 += 1
            score1.set_text(str(point1),40,(30,30,30))
            ball2 = Picture("pixil-frame-0 (15).png",1,1,30,30)
            dx1 = 0
            dy1 = 0
            
            
    
            score1.draw(0,0)


    if new_time - start_time >= 90:
        
        ball.rect.x += dx
        ball.rect.y += dy
    if new_time - start_time >= 110:
        ball.rect.x += dx
        ball.rect.y += dy
    if new_time - start_time >= 130:
        ball.rect.x += dx
        ball.rect.y += dy
    if new_time - start_time >= 150:
        ball.rect.x += dx
        ball.rect.y += dy



    if new_time - start_time >= 70:
        for p in gg1:
            p.draw()
        
            ball3.rect.x += dx2
            ball3.rect.y += dy2
            if ball3.rect.y > 275 or ball3.rect.y < -220:
                dy2 *= -1
            if ball3.rect.colliderect(platform1.rect):
                dx2 *= -1
            if ball3.rect.colliderect(platform2.rect):
                dx2 *= -1

            
            if ball3.rect.x > 330:
                point += 1
                score.set_text(str(point),40,(30,30,30))
                ball3 = Picture("pixil-frame-0 (15).png",1,1,30,30)
                dy2 = 0
                dx2 = 0
            if ball3.rect.x < -260 :
                point1 += 1
                score1.set_text(str(point1),40,(30,30,30))
                ball3 = Picture("pixil-frame-0 (15).png",1,1,30,30)
                dx2 = 0
                dy2 = 0

    if new_time - start_time >= 90:
        for q in gg2:
            q.draw()
        
            ball4.rect.x += dx3
            ball4.rect.y += dy3
            if ball4.rect.y > 275 or ball4.rect.y < -220:
                dy3 *= -1
            if ball4.rect.colliderect(platform1.rect):
                dx3 *= -1
            if ball4.rect.colliderect(platform2.rect):
                dx3 *= -1

            
            if ball4.rect.x > 330:
                point += 1
                score.set_text(str(point),40,(30,30,30))
                ball4 = Picture("pixil-frame-0 (15).png",1,1,30,30)
                dy3 = 0
                dx3 = 0
            if ball4.rect.x < -260 :
                point1 += 1
                score1.set_text(str(point1),40,(30,30,30))
                ball4 = Picture("pixil-frame-0 (15).png",1,1,30,30)
                dx3 = 0
                dy3 = 0


    if new_time - start_time >= 115:
        for q in gg3:
            q.draw()
        
            ball5.rect.x += dx4
            ball5.rect.y += dy4
            if ball5.rect.y > 275 or ball5.rect.y < -220:
                dy4 *= -1
            if ball5.rect.colliderect(platform1.rect):
                dx4 *= -1
            if ball5.rect.colliderect(platform2.rect):
                dx4 *= -1

            
            if ball5.rect.x > 330:
                point += 1
                score.set_text(str(point),40,(30,30,30))
                ball5 = Picture("pixil-frame-0 (15).png",1,1,30,30)
                dy4 = 0
                dx4 = 0
            if ball5.rect.x < -260 :
                point1 += 1
                score1.set_text(str(point1),40,(30,30,30))
                ball5 = Picture("pixil-frame-0 (15).png",1,1,30,30)
                dx4 = 0
                dy4 = 0
    


    if new_time - start_time >= 100:
        black = (255,255,255)
        harding.set_text("Ускладнення!!",30,(0,0,0))
        harding.draw()

    if new_time -start_time >= 120:
        black = (0,128,0)
        harding.set_text("Ускладнення!!",0,(0,0,0))

    
            
        """Події"""
    
    score.draw()
    score1.draw()
    time_text.draw(20,20)
    timer.draw(0,0)
    lin.draw()
    ball.draw()
    platform2.draw()
    platform1.draw()
    pygame.display.update()
    clock.tick(40)
    
pygame.display.update()