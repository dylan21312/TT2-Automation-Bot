import random
import pyautogui
import time
import mss

def human_drag(start, end, duration=0.4):
    sx, sy = start
    ex, ey = end

    # 加入微抖動
    #ex += random.randint(-5, 5)
    #ey += random.randint(-5, 5)

    pyautogui.moveTo(sx, sy)
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.03, 0.08))
    pyautogui.moveTo(ex, ey, duration=duration)
    time.sleep(random.uniform(1, 1.2))
    pyautogui.mouseUp()

MONITOR_INDEX = 2  # BS 在副螢幕
MONITER2 = mss.mss().monitors[MONITOR_INDEX]
human_drag((MONITER2["left"] + 234, 952), (MONITER2["left"] + 234, 714))
