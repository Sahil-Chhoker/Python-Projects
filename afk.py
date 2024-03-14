import pyautogui as pag
import random
import time

afk_counter = 0
curr_pos = pag.position()

while True:
    if pag.position() == curr_pos:
        afk_counter += 1
    else:
        afk_counter = 0
        curr_pos = pag.position()

    if afk_counter > 5:
        x = random.randint(0, 1920)
        y = random.randint(0, 1080)

        pag.moveTo(x, y, 0.5)
        curr_pos = pag.position()

    print(f"AFK Counter: {afk_counter}")
    time.sleep(2)