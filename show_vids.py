"""
    Скрипт определения лесных пожаров на видео потоке по цвету 

    Для завершения работы нажать ESC или закрыть этот терминал
    КРЕСТИК В ОКНЕ С ВИДЕО НЕ РАБОТАЕТ! ЭТО НОРМА

    Для отображения/сокрытия слоя найденных объектов нажать ПРОБЕЛ


██ ▇▇ ▆ ▅ ▄ ▃ ▂ ▁▁▁ ▂ ▃ ▄ ▅ ▆ ▇▇ █▉
▉                                 ▉ 
▉         made by i-sergh         ▉
▉                                 ▉
▉ https://www.github.com/i-sergh/ ▉
▍     ▐             ▐             ▐
     ▏       ▐         ▐    ▐ 
▏          ▏      ▏      ▏    ▏  ▏
   ▏   ▏        ▏   ▏      
    
"""

import cv2
import numpy as np
#import sys
from os import system

from utils import  get_center_of_ignition



system('color a')
system('cls')
print(__doc__)

PATH = 'samples/vids/1.mp4'

ERR_COUNTER = 0

SHOW_FIRE_LAYER = True

cap = cv2.VideoCapture(PATH)


while True:
    tr, frame = cap.read()

    # if video ends
    if not tr:
        cap = cv2.VideoCapture(PATH)
        tr, frame = cap.read()
        # if actually no video
        if not tr:
            print('err: video reading error! no video in the path '  + PATH, file=sys.stderr)
            ERR_COUNTER += 1
            if ERR_COUNTER == 10:
                break
            continue
    
    ERR_COUNTER = 0

    mask, cont = get_center_of_ignition(frame)

    if SHOW_FIRE_LAYER:
        frame[mask==255] = (0,255,0) 
    
    cv2.imshow('forest fire', frame)
    #cv2.imshow('forest fire mask', mask)
    
    key = cv2.waitKey(1)

    if key == 27:
        break
    if key == 32:
        SHOW_FIRE_LAYER = not SHOW_FIRE_LAYER
    
cv2.destroyAllWindows()
