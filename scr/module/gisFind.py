import pyautogui as pag

def find():
    image = ["find1.png", "find2.png", "find3.png"]
    id = 0
    while True:
        # mousePosX, mousePosY = pag.position() #найти координаты по расположению мышки
        pag.moveTo(63, 7)
        try:
            template = pag.locateOnScreen("img/" + image[id])
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

def find_ans():
    image = ["ans1.png", "ans2.png", "ans3.png"]
    id = 0
    while True:
        # mousePosX, mousePosY = pag.position() #найти координаты по расположению мышки
        try:
            template = pag.locateOnScreen("img/" + image[id])
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

def find_push():
    image = ["push1.png", "push2.png", "push3.png"]
    id = 0
    while True:
        # mousePosX, mousePosY = pag.position() #найти координаты по расположению мышки
        try:
            template = pag.locateOnScreen("img/" + image[id])
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
       
