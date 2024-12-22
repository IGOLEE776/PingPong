from pygame import *

img_bg = 'Pong bg.png'

w = 1000
h = 500

display.set_caption('Game shootee')
win = display.set_mode((w,h))
bg = transform.scale(image.load(img_bg), (w,h))

win.exec()