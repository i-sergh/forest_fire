import cv2
import numpy as np
import sys
from os import listdir
from os.path import isfile, join


# TODO
def get_files_list(file_path):
    files = [join(file_path, f) for f in listdir(file_path) if isfile(join(file_path, f))]
    return files 

def _find_by_color(img: np.uint8, low: tuple, high: tuple) -> (np.uint8, tuple):
    """
    _find_by_color возвращает маску и контуры объекта определенного цвета
    Находит объекты по промежуткам в пространстве HSV

    Возвращает:
    ____________
        img_mask: np.uint8 - двумерный массив маски изображения
        cont: tuple of arrays - возвращает кортеж контуров, найденных по цвету на изображении
        
    Атрибуты:
    _________
    img: np.uint8 -  массив изображения (цветовое пространство BGR)

    low: tuple - минимальное значение порога;  кортеж из 3-х значений, каждое значение в промежутке 0-255

    high: tuple - максимальное значение порога; кортеж из 3-х значений, каждое значение в промежутке 0-255
                        каждое значение кортежа high должно быть больше соответствующего ему по индеску кортежа low
                        high[0] > low[0], high[1] > low[1], high[2] > low[2]

                        
    """
    img_blur = cv2.blur(img, (10, 10))
    
    img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV )
    
    img_mask = cv2.inRange(img_hsv, low, high)

    cont, h = cv2.findContours( img_mask, cv2.RETR_TREE,
                                                  cv2.CHAIN_APPROX_SIMPLE )
    return img_mask, cont
        
def get_center_of_ignition(img: np.uint8) -> (np.uint8, tuple):
    return _find_by_color(img, (0,70, 70),
                                                 (50, 255, 255) )

def get_center_of_ignition_ic(img: np.uint8) -> (np.uint8, tuple):
    return _find_by_color(img, (0,70, 70),
                                                (30, 255, 255) )

def  get_smoke():
    pass
