import pyautogui as pag
from time import sleep

def find():
    image = ["find1.png", "find2.png", "find3.png"]
    id = 0
    while True:
        mousePosX, mousePosY = pag.position() #найти координаты по расположению мышки
        pag.moveTo(63, 7)
        try:
            template = pag.locateOnScreen(image/image[id])
        except IndexError:
            print("Ошибка")
            break
        if template == None:
            id = id + 1
        else:
            cood = []
            try:
                for element in template:
                    cood.append(element + 15)
            except:
                print("None")
            template = cood
            del template[2:4]
            print(template)
            pag.moveTo(template)
            break