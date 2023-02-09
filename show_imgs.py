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
import sys
from os import system

from utils import  get_center_of_ignition_ic,  get_files_list

print(sys.path)

system('color a')
system('cls')
print(__doc__)

PATH = 'samples/ic_imgs/'

imgs_list  = get_files_list(PATH) 
print(imgs_list)
if imgs_list == []:
    print('err: images reading error!\nno images in the path ' +  sys.path[0] + '\\' + '\\'.join(PATH.split('/')), file=sys.stderr)

IMG_COUNTER = 0

frame = cv2.imread( imgs_list[IMG_COUNTER] )
print(imgs_list[IMG_COUNTER] + ' is opened')
SHOW_FIRE_LAYER = True


#frame = np.zeros((100, 100, 3), dtype = np.uint8())

while True:

    ERR_COUNTER = 0

    mask, cont = get_center_of_ignition_ic(frame)

    if SHOW_FIRE_LAYER:
        frame[mask==255] = (0,255,255) 
    
    cv2.imshow('forest fire', frame)
    #cv2.imshow('forest fire mask', mask) 
    
    key = cv2.waitKey(1)

    if key == 27:
        break
    if key == 32:
        SHOW_FIRE_LAYER = not SHOW_FIRE_LAYER
        frame = cv2.imread( imgs_list[IMG_COUNTER] )
        print(imgs_list[IMG_COUNTER] + ' is opened')
    if key == ord('e'):
        IMG_COUNTER += 1
        if IMG_COUNTER == len(imgs_list):
            IMG_COUNTER = 0
        frame = cv2.imread( imgs_list[IMG_COUNTER] )
        print(imgs_list[IMG_COUNTER] + ' is opened')
    if key == ord('q'):
        IMG_COUNTER -= 1
        if IMG_COUNTER < 0:
            IMG_COUNTER = len(imgs_list) - 1
        print(IMG_COUNTER)
        frame = cv2.imread( imgs_list[IMG_COUNTER] )
        print(imgs_list[IMG_COUNTER] + ' is opened')
        
cv2.destroyAllWindows()
