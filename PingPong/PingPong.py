'''from pygame import *
from time import time as timer

img_bg = 'Pong bg.png'


w = 800
h = 500

display.set_caption('PingPong')
win = display.set_mode((w,h))
bg = transform.scale(image.load(img_bg), (w,h))

ping1 = 'ping.png'
ping2 = 'ping.png'
bol = 'bol.png'

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, pos_x, pos_y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = speed
    
    def draw(self):
        win.blit(self.image(self.rect.x, self.rect.y))

class Player(GameSprite):
    def move_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < h - 30:
            self.rect.y += self.speed
    
    def move_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < h - 30:
            self.rect.y += self.speed

ping11 = Player(ping1, 10, h/1.5, 20, 50, 10)
ping22 = Player(ping2, 790, h/1.5, 20, 50, 10)

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        win.blit(bg, (0, 0))
        ping11.draw()
        ping22.draw()
    
    display.update()
    time.delay(60)'''

from pygame import *

img_bg = 'Pong bg.png'


w = 800
h = 500

display.set_caption('PingPong')
win = display.set_mode((w,h))
bg = transform.scale(image.load(img_bg), (w,h))

ping1 = 'ping.png'
ping2 = 'ping.png'
bol = 'bol.png'

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #e.g. 55,55 - parameters
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < h - 80:
           self.rect.y += self.speed
           
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < h - 80:
           self.rect.y += self.speed

ping11 = Player(ping1, 10, h/2.2, 10, 10, 70)
ping22 = Player(ping2, 780, h/2.2, 10, 10, 70)
bol = GameSprite(bol, w/2.05, h/2.05, 4, 20, 20)


font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (60, 60, 60))
lose2 = font.render('PLAYER 2 LOSE!', True, (60, 60, 60))

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        win.blit(bg, (0, 0))
        ping11.reset()
        ping22.reset()
        ping11.update_l()
        ping22.update_r()
        bol.reset()
    
    display.update()
    time.delay(60)