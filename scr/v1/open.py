import pyautogui as pag
from time import sleep

delay = 1

def add_tab(): #открытие новых вкладок
    for i in range(0, 10):
        pag.moveTo(509, 790)
        pag.click(button="right")
        pag.moveTo(591, 794)
        pag.click()
        pag.moveTo(509, 790)
        pag.scroll(-229)
add_tab()
# def add_tab1(): #открытие новых вкладок
#     for i in range(0, 10):
#         pag.moveTo(509, 790)
#         pag.click(button="right")
#         pag.moveTo(48, 14)
#         pag.click()
#         pag.moveTo(509, 790)
#         pag.moveTo(591, 794)
#         pag.scroll(-229)
#         mousePosX, mousePosY = pag.position() #найти координаты по расположению мышки
#         print(mousePosX, mousePosY)
# add_tab1()

