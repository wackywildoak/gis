import pyautogui as pag
from time import sleep

delay = 1

# screenWidth, screenHeight = pag.size()
# print(screenHeight, screenWidth)
mousePosX, mousePosY = pag.position() #найти координаты по расположению мышки
print(mousePosX, mousePosY)
# # pag.moveTo(1411, 841)
# # pag.click()

def update_tab(): #переход на основую вкладку и обновление запросов на ней
    pag.moveTo(48, 14)
    pag.click()
    sleep(delay)
    pag.moveTo(198, 471)
    sleep(delay)
    pag.scroll(5000)
    sleep(delay)
    pag.moveTo(1394, 650)
    pag.click()
    sleep(delay)

def close_tabs(): #закрытие вкладок
    for i in range(0, 10):
        pag.moveTo(293, 11)
        pag.click()
        sleep(delay)

def add_tab(): #открытие новых вкладок
    for i in range(0, 10):
        pag.moveTo(509, 790)
        pag.click(button="right")
        pag.moveTo(591, 794)
        pag.click()
        pag.moveTo(509, 790)
        pag.scroll(-229)

def clicks(): #ответ за запрос
    sleep(delay)
    pag.moveTo(1411, 875) #добавить ответ
    pag.click()
    sleep(delay)
    pag.moveTo(1023, 270) #нет
    pag.click()
    sleep(delay)
    pag.moveTo(1287, 489) #сохранить ответ
    pag.click()
    sleep(delay)
    pag.moveTo(1415, 932) #отправить ответ
    pag.click()
    sleep(delay)
    pag.moveTo(1011, 283) #да
    pag.click()
    sleep(delay)
    pag.moveTo(949, 275) #ок
    pag.click()
    sleep(delay)

def tabs(): #открытие вкладки
    pag.moveTo(237, 15) #1 запрос
    pag.click()
    clicks()
    pag.moveTo(363, 17) #2 запрос
    pag.click()
    clicks()
    pag.moveTo(505, 14) #3 запрос
    pag.click()
    clicks()
    pag.moveTo(663, 14) #4 запрос
    pag.click()
    clicks()
    pag.moveTo(796, 17) #5 запрос
    pag.click()
    clicks()
    pag.moveTo(963, 15) #6 запрос
    pag.click()
    clicks()
    pag.moveTo(1091, 11) #7 запрос
    pag.click()
    clicks()
    pag.moveTo(1240, 5) #8 запрос
    pag.click()
    clicks()
    pag.moveTo(1415, 14) #9 запрос
    pag.click()
    clicks()
    pag.moveTo(1571, 17) #10 запрос
    pag.click()
    clicks()

def main():
    for j in range(0, 50):
        update_tab()
        add_tab()
        tabs()
        close_tabs()
        print("Отвечено на", (j + 1) * 10, "запросов")

if __name__ == "__main__":
    main()
    
#при использовании, ставить масштаб в хроме 90%