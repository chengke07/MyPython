'''
@Author: your name
@Date: 2019-12-30 15:25:32
@LastEditTime : 2019-12-31 08:33:56
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \MyPython\pygame_ex1.py
'''
import pygame
import sys
import time


#初始化Pygame
pygame.init()

size = width,height = 600,400


#创建指定大小的窗口 Surface
screen = pygame.display.set_mode(size)
#设置窗口标题
pygame.display.set_caption('初次见面，请大家多多关照！')

f = open('record.txt','w')

while True:
    
    for event in pygame.event.get():
        f.write(str(event)+'\n')

        if event.type == pygame.QUIT:
            f.close()
            exit()

       




